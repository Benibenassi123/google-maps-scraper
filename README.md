# Google Maps Scraper

An efficient web scraper for extracting business data from Google Maps using Playwright.

## Features

- 🚀 **Async/Await**: Fast scraping with async operations
- 🎭 **Playwright-based**: Handles JavaScript-heavy Google Maps interface
- 🔄 **Auto-scrolling**: Automatically loads all results
- 🛡️ **Anti-detection**: User-agent rotation and webdriver property removal
- 💾 **Multiple formats**: Export to CSV or JSON
- ⚙️ **Configurable**: Easy configuration via environment variables
- 🎯 **Comprehensive data**: Extracts name, rating, reviews, category, address, coordinates, and more

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Benibenassi123/google-maps-scraper.git
cd google-maps-scraper
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

5. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your preferred settings
```

## Usage

### Basic Usage

```python
import asyncio
from scraper import GoogleMapsScraper

async def main():
    scraper = GoogleMapsScraper()
    
    # Scrape restaurants in a city
    results = await scraper.scrape(
        query="restaurants",
        location="San Francisco, CA"
    )
    
    # Save results
    scraper.save_results()
    
    print(f"Found {len(results)} businesses")

if __name__ == "__main__":
    asyncio.run(main())
```

### Command Line

Run the example:
```bash
python scraper.py
```

## Configuration

Edit the `.env` file to customize behavior:

```env
# Run browser in headless mode (true/false)
HEADLESS=false

# Delay between actions (seconds)
DELAY_MIN=2
DELAY_MAX=5

# Maximum number of results to scrape
MAX_RESULTS=100

# Output format (csv or json)
OUTPUT_FORMAT=csv
```

## Data Extracted

The scraper extracts the following fields for each business:

- **name**: Business name
- **rating**: Star rating (e.g., "4.5")
- **reviews**: Number of reviews
- **category**: Business category/type
- **address**: Physical address (when available)
- **latitude**: GPS latitude coordinate
- **longitude**: GPS longitude coordinate
- **url**: Google Maps URL
- **search_query**: The query used to find this business
- **scraped_at**: Timestamp of when data was collected

## Output

Results are saved to the `output/` directory in your chosen format:

- **CSV**: `output/google_maps_results_YYYYMMDD_HHMMSS.csv`
- **JSON**: `output/google_maps_results_YYYYMMDD_HHMMSS.json`

## Legal Disclaimer

⚠️ **Important**: Web scraping may violate Google's Terms of Service. This tool is provided for educational purposes only. Users are responsible for ensuring their use complies with:

- Google Maps Terms of Service
- Applicable laws and regulations
- Website robots.txt policies
- Rate limiting and respectful scraping practices

**Recommendations**:
- Consider using the official Google Places API for production use
- Implement appropriate delays between requests
- Respect rate limits
- Only scrape publicly available data

## Troubleshooting

### Browser not launching
```bash
playwright install chromium
```

### No results found
- Try running with `HEADLESS=false` to see what's happening
- Check if Google Maps is loading correctly
- Verify your search query is valid

### Rate limiting/blocking
- Increase `DELAY_MIN` and `DELAY_MAX`
- Reduce `MAX_RESULTS`
- Consider using proxies (not included in this basic version)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Author

Built with ❤️ using Playwright and Python

---

**Note**: For production use, consider using the official Google Places API instead of web scraping.
