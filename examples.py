"""
Example usage scripts for the Google Maps Scraper
"""

import asyncio
from scraper import GoogleMapsScraper


async def example_basic():
    """Basic example: Scrape restaurants in a city"""
    print("=== Basic Example ===\n")
    
    scraper = GoogleMapsScraper()
    results = await scraper.scrape(
        query="restaurants",
        location="San Francisco, CA"
    )
    
    scraper.save_results("sf_restaurants")
    print(f"✓ Scraped {len(results)} restaurants in San Francisco")


async def example_multiple_queries():
    """Advanced example: Scrape multiple business types"""
    print("\n=== Multiple Queries Example ===\n")
    
    queries = [
        ("coffee shops", "Seattle, WA"),
        ("gyms", "Austin, TX"),
        ("bookstores", "Portland, OR")
    ]
    
    for query, location in queries:
        scraper = GoogleMapsScraper()
        results = await scraper.scrape(query=query, location=location)
        
        # Custom filename
        filename = f"{location.replace(',', '').replace(' ', '_')}_{query.replace(' ', '_')}"
        scraper.save_results(filename)
        
        print(f"✓ Scraped {len(results)} {query} in {location}")
        
        # Small delay between different searches
        await asyncio.sleep(3)


async def example_specific_area():
    """Example: Scrape businesses in a specific neighborhood"""
    print("\n=== Specific Area Example ===\n")
    
    scraper = GoogleMapsScraper()
    results = await scraper.scrape(
        query="pizza",
        location="Brooklyn, New York, NY"
    )
    
    scraper.save_results("brooklyn_pizza")
    
    # Print some sample data
    if results:
        print(f"\n✓ Found {len(results)} pizza places")
        print("\nSample business:")
        sample = results[0]
        print(f"  Name: {sample.get('name', 'N/A')}")
        print(f"  Rating: {sample.get('rating', 'N/A')}")
        print(f"  Reviews: {sample.get('reviews', 'N/A')}")
        print(f"  Category: {sample.get('category', 'N/A')}")


async def example_custom_config():
    """Example: Using custom configuration"""
    print("\n=== Custom Configuration Example ===\n")
    
    scraper = GoogleMapsScraper()
    
    # You can modify config on the fly
    scraper.config.MAX_RESULTS = 50
    scraper.config.OUTPUT_FORMAT = 'json'
    
    results = await scraper.scrape(
        query="hotels",
        location="Miami, FL"
    )
    
    scraper.save_results("miami_hotels")
    print(f"✓ Scraped {len(results)} hotels (limited to 50, saved as JSON)")


async def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("Google Maps Scraper - Usage Examples")
    print("="*60 + "\n")
    
    # Uncomment the examples you want to run
    
    # Example 1: Basic usage
    await example_basic()
    
    # Example 2: Multiple queries (warning: takes longer)
    # await example_multiple_queries()
    
    # Example 3: Specific area
    # await example_specific_area()
    
    # Example 4: Custom configuration
    # await example_custom_config()
    
    print("\n" + "="*60)
    print("Examples completed! Check the 'output/' directory for results.")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
