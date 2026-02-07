import asyncio
import random
import time
from typing import List, Dict, Optional
from playwright.async_api import async_playwright, Page, Browser
import pandas as pd
import json
from datetime import datetime
import os
from config import Config


class GoogleMapsScraper:
    """Scraper for extracting business data from Google Maps"""
    
    def __init__(self):
        self.config = Config()
        self.browser: Optional[Browser] = None
        self.results: List[Dict] = []
        
    async def init_browser(self):
        """Initialize Playwright browser"""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(
            headless=self.config.HEADLESS,
            args=['--disable-blink-features=AutomationControlled']
        )
        return playwright
    
    async def create_page(self) -> Page:
        """Create a new page with anti-detection measures"""
        context = await self.browser.new_context(
            user_agent=random.choice(self.config.USER_AGENTS),
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        # Anti-detection: Remove webdriver property
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        return page
    
    async def random_delay(self):
        """Add random delay to mimic human behavior"""
        delay = random.uniform(self.config.DELAY_MIN, self.config.DELAY_MAX)
        await asyncio.sleep(delay)
    
    async def scroll_results(self, page: Page):
        """Scroll through the results panel to load all businesses"""
        print("Scrolling to load more results...")
        
        # Find the scrollable results container
        scrollable_div = await page.query_selector('div[role="feed"]')
        
        if not scrollable_div:
            print("Could not find scrollable container")
            return
        
        previous_height = 0
        scroll_attempts = 0
        
        while scroll_attempts < self.config.MAX_SCROLL_ATTEMPTS:
            # Scroll within the results panel
            await page.evaluate("""
                (element) => {
                    element.scrollTo(0, element.scrollHeight);
                }
            """, scrollable_div)
            
            await asyncio.sleep(self.config.SCROLL_PAUSE_TIME)
            
            # Check if new content loaded
            current_height = await page.evaluate(
                "(element) => element.scrollHeight",
                scrollable_div
            )
            
            if current_height == previous_height:
                # Check if we've reached the end
                end_message = await page.query_selector('text="You\'ve reached the end of the list."')
                if end_message:
                    print("Reached end of results")
                    break
                scroll_attempts += 1
            else:
                scroll_attempts = 0  # Reset if we found new content
            
            previous_height = current_height
            
            # Check current number of results
            current_results = await page.query_selector_all('div[role="feed"] > div > div > a')
            print(f"Loaded {len(current_results)} results so far...")
            
            if len(current_results) >= self.config.MAX_RESULTS:
                print(f"Reached maximum results limit: {self.config.MAX_RESULTS}")
                break
    
    async def extract_business_data(self, page: Page, element) -> Optional[Dict]:
        """Extract data from a single business listing"""
        try:
            data = {}
            
            # Extract name
            name_elem = await element.query_selector('div[role="img"]')
            if name_elem:
                data['name'] = await name_elem.get_attribute('aria-label')
            
            # Extract rating
            rating_elem = await element.query_selector('span[role="img"]')
            if rating_elem:
                rating_text = await rating_elem.get_attribute('aria-label')
                if rating_text:
                    # Parse "4.5 stars" format
                    data['rating'] = rating_text.split()[0]
            
            # Extract number of reviews
            reviews_elem = await element.query_selector('span[aria-label*="reviews"]')
            if reviews_elem:
                reviews_text = await reviews_elem.inner_text()
                data['reviews'] = reviews_text.strip('()')
            
            # Extract category/type
            category_elems = await element.query_selector_all('div > div > div > div:nth-child(2) > span')
            if len(category_elems) > 0:
                categories = []
                for cat_elem in category_elems[:3]:  # Get first 3 category spans
                    cat_text = await cat_elem.inner_text()
                    if cat_text and '·' not in cat_text:
                        categories.append(cat_text)
                if categories:
                    data['category'] = ', '.join(categories)
            
            # Extract address (if visible)
            address_spans = await element.query_selector_all('span')
            for span in address_spans:
                text = await span.inner_text()
                if text and any(keyword in text.lower() for keyword in ['street', 'avenue', 'road', 'blvd']):
                    data['address'] = text
                    break
            
            # Extract URL
            link = await element.query_selector('a')
            if link:
                href = await link.get_attribute('href')
                data['url'] = href
                
                # Extract coordinates from URL if available
                if '@' in href:
                    coords_part = href.split('@')[1].split(',')[:2]
                    if len(coords_part) == 2:
                        data['latitude'] = coords_part[0]
                        data['longitude'] = coords_part[1]
            
            # Only return if we have at least a name
            if 'name' in data:
                return data
            
        except Exception as e:
            print(f"Error extracting business data: {e}")
        
        return None
    
    async def scrape(self, query: str, location: str = "") -> List[Dict]:
        """Main scraping method"""
        print(f"Starting scrape for: {query} in {location}")
        
        playwright = await self.init_browser()
        page = await self.create_page()
        
        try:
            # Construct search query
            search_query = f"{query} {location}".strip()
            url = f"{self.config.GOOGLE_MAPS_BASE_URL}{search_query}"
            
            print(f"Navigating to: {url}")
            await page.goto(url, timeout=self.config.PAGE_LOAD_TIMEOUT)
            
            # Wait for results to load
            await page.wait_for_selector('div[role="feed"]', timeout=10000)
            await self.random_delay()
            
            # Scroll to load all results
            await self.scroll_results(page)
            
            # Extract all business listings
            print("Extracting business data...")
            business_elements = await page.query_selector_all('div[role="feed"] > div > div')
            
            print(f"Found {len(business_elements)} potential businesses")
            
            for idx, element in enumerate(business_elements[:self.config.MAX_RESULTS]):
                business_data = await self.extract_business_data(page, element)
                if business_data:
                    business_data['search_query'] = search_query
                    business_data['scraped_at'] = datetime.now().isoformat()
                    self.results.append(business_data)
                    print(f"Extracted {idx + 1}/{len(business_elements)}: {business_data.get('name', 'Unknown')}")
            
            print(f"\nSuccessfully scraped {len(self.results)} businesses")
            
        except Exception as e:
            print(f"Error during scraping: {e}")
            raise
        
        finally:
            await page.close()
            await self.browser.close()
            await playwright.stop()
        
        return self.results
    
    def save_results(self, filename: Optional[str] = None):
        """Save results to file"""
        if not self.results:
            print("No results to save")
            return
        
        # Create output directory if it doesn't exist
        os.makedirs(self.config.OUTPUT_DIR, exist_ok=True)
        
        # Generate filename if not provided
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"google_maps_results_{timestamp}"
        
        filepath = os.path.join(self.config.OUTPUT_DIR, filename)
        
        if self.config.OUTPUT_FORMAT == 'csv':
            df = pd.DataFrame(self.results)
            csv_path = f"{filepath}.csv"
            df.to_csv(csv_path, index=False)
            print(f"Results saved to {csv_path}")
        else:
            json_path = f"{filepath}.json"
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            print(f"Results saved to {json_path}")


async def main():
    """Example usage"""
    scraper = GoogleMapsScraper()
    
    # Example: Scrape restaurants in New York
    results = await scraper.scrape(
        query="restaurants",
        location="New York, NY"
    )
    
    # Save results
    scraper.save_results()
    
    # Print summary
    print(f"\nScraping complete! Found {len(results)} businesses")
    if results:
        print("\nSample result:")
        print(json.dumps(results[0], indent=2))


if __name__ == "__main__":
    asyncio.run(main())
