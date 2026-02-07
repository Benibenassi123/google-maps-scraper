"""
Simple Web Interface for Google Maps Scraper
No coding required - just open in browser and click!
"""

from flask import Flask, render_template, request, jsonify, send_file
import asyncio
from scraper import GoogleMapsScraper
import os
import json
from datetime import datetime
import threading

app = Flask(__name__)

# Store scraping status
scraping_status = {
    'running': False,
    'progress': '',
    'results': [],
    'error': None
}

def run_scraper(query, location, max_results, output_format):
    """Run the scraper in background"""
    global scraping_status
    
    try:
        scraping_status['running'] = True
        scraping_status['progress'] = 'Initializing...'
        scraping_status['error'] = None
        
        # Create scraper
        scraper = GoogleMapsScraper()
        scraper.config.MAX_RESULTS = max_results
        scraper.config.OUTPUT_FORMAT = output_format
        
        # Run async scraper
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        scraping_status['progress'] = f'Searching for {query} in {location}...'
        results = loop.run_until_complete(scraper.scrape(query, location))
        
        scraping_status['progress'] = 'Saving results...'
        filename = f"{query.replace(' ', '_')}_{location.replace(' ', '_').replace(',', '')}"
        scraper.save_results(filename)
        
        scraping_status['results'] = results
        scraping_status['progress'] = f'✓ Complete! Found {len(results)} businesses'
        scraping_status['running'] = False
        
    except Exception as e:
        scraping_status['error'] = str(e)
        scraping_status['running'] = False
        scraping_status['progress'] = f'Error: {str(e)}'

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    """Start scraping"""
    global scraping_status
    
    if scraping_status['running']:
        return jsonify({'error': 'Scraper is already running'}), 400
    
    data = request.json
    query = data.get('query', '')
    location = data.get('location', '')
    max_results = int(data.get('max_results', 50))
    output_format = data.get('output_format', 'csv')
    
    if not query or not location:
        return jsonify({'error': 'Please provide both query and location'}), 400
    
    # Reset status
    scraping_status = {
        'running': True,
        'progress': 'Starting...',
        'results': [],
        'error': None
    }
    
    # Run in background thread
    thread = threading.Thread(target=run_scraper, args=(query, location, max_results, output_format))
    thread.daemon = True
    thread.start()
    
    return jsonify({'message': 'Scraping started'})

@app.route('/status')
def status():
    """Get current status"""
    return jsonify(scraping_status)

@app.route('/files')
def list_files():
    """List output files"""
    output_dir = 'output'
    if not os.path.exists(output_dir):
        return jsonify([])
    
    files = []
    for filename in os.listdir(output_dir):
        filepath = os.path.join(output_dir, filename)
        files.append({
            'name': filename,
            'size': os.path.getsize(filepath),
            'modified': datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify(sorted(files, key=lambda x: x['modified'], reverse=True))

@app.route('/download/<filename>')
def download(filename):
    """Download a file"""
    filepath = os.path.join('output', filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return 'File not found', 404

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Google Maps Scraper - Web Interface")
    print("="*60)
    print("\n✓ Server starting...")
    print("\n👉 Open your browser and go to:")
    print("\n   http://localhost:5000")
    print("\n❌ Press CTRL+C to stop the server")
    print("\n" + "="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
