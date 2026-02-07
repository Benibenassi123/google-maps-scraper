import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the scraper"""
    
    # Browser settings
    HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
    
    # Timing settings (in seconds)
    DELAY_MIN = float(os.getenv('DELAY_MIN', '2'))
    DELAY_MAX = float(os.getenv('DELAY_MAX', '5'))
    PAGE_LOAD_TIMEOUT = 30000  # milliseconds
    
    # Scraping settings
    MAX_RESULTS = int(os.getenv('MAX_RESULTS', '100'))
    SCROLL_PAUSE_TIME = 2  # seconds between scrolls
    MAX_SCROLL_ATTEMPTS = 10
    
    # Output settings
    OUTPUT_FORMAT = os.getenv('OUTPUT_FORMAT', 'csv')  # csv or json
    OUTPUT_DIR = 'output'
    
    # Google Maps URLs
    GOOGLE_MAPS_BASE_URL = 'https://www.google.com/maps/search/'
    
    # User agents for rotation
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    ]
