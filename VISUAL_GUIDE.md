# 🎨 Visual Interface Guide - For Non-Developers

## 🚀 Super Simple 3-Step Setup

### Step 1: Download the Project
1. Go to: https://github.com/Benibenassi123/google-maps-scraper
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Unzip the file to your Desktop

### Step 2: Install Everything (One-Time Only)
Open Terminal (Mac) or Command Prompt (Windows) and type:

```bash
cd Desktop/google-maps-scraper-main
pip install -r requirements.txt
playwright install chromium
```

### Step 3: Start the Web Interface
Type this in Terminal/Command Prompt:

```bash
python app.py
```

You'll see:
```
🚀 Google Maps Scraper - Web Interface
👉 Open your browser and go to: http://localhost:5000
```

---

## 🖥️ Using the Beautiful Web Interface

### What You'll See:

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│         🗺️ Google Maps Scraper                     │
│    Extract business data - No coding required!     │
│                                                     │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│                                                     │
│  What are you looking for? 🔍                      │
│  [________________restaurants_________________]    │
│                                                     │
│  Where? 📍                                         │
│  [________________New York, NY________________]    │
│                                                     │
│  Maximum Results 📊                                │
│  [________50________]                              │
│                                                     │
│  Output Format 💾                                  │
│  [▼ CSV (Excel)    ]                               │
│                                                     │
│         ┌─────────────────────┐                    │
│         │  Start Scraping 🚀  │                    │
│         └─────────────────────┘                    │
│                                                     │
│  💡 Quick Examples (click to use):                 │
│  • 🍕 Pizza places in Chicago                      │
│  • ☕ Coffee shops in Seattle                      │
│  • 🏋️ Gyms in Los Angeles                         │
│  • 🏨 Hotels in Miami                              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## ✨ How to Use It (Click & Type!)

### Option 1: Use Quick Examples
1. **Just CLICK** on any example like "🍕 Pizza places in Chicago"
2. Click the **"Start Scraping 🚀"** button
3. Wait for it to finish (you'll see a spinner)
4. Download your file!

### Option 2: Custom Search
1. **Type** what you want in "What are you looking for?"
   - Examples: "dentists", "hair salons", "pet stores"
   
2. **Type** where you want to search
   - Examples: "Boston, MA", "Austin, TX", "Portland, OR"
   
3. **Choose** how many results (default is 50)

4. **Choose** format:
   - **CSV** = Opens in Excel ✅ (Recommended)
   - **JSON** = For developers

5. Click **"Start Scraping 🚀"**

---

## 📊 What Happens Next?

### While Scraping:
You'll see messages like:
- "🔄 Starting scraper..."
- "🔄 Searching for restaurants in New York..."
- "🔄 Scrolling to load more results..."
- "🔄 Extracting business data..."

### When Done:
- "✓ Complete! Found 50 businesses"
- Your file appears in the **"Your Downloaded Files"** section
- Click **"⬇️ Download"** to save it

---

## 📁 Your Downloaded Files

After scraping, you'll see something like:

```
┌─────────────────────────────────────────────────────┐
│  📁 Your Downloaded Files                           │
├─────────────────────────────────────────────────────┤
│                                                     │
│  📄 restaurants_NewYork.csv                         │
│  Size: 23.4 KB | Modified: 2026-02-07 10:30:15    │
│                          [⬇️ Download]              │
│                                                     │
│  📄 coffee_shops_Seattle.csv                        │
│  Size: 15.2 KB | Modified: 2026-02-07 10:25:43    │
│                          [⬇️ Download]              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 📈 What's Inside the Files?

When you open the CSV in Excel, you'll see columns like:

| name | rating | reviews | category | address | latitude | longitude | url |
|------|--------|---------|----------|---------|----------|-----------|-----|
| Joe's Pizza | 4.5 | 1,234 | Pizza restaurant | 123 Main St | 40.7580 | -73.9855 | [link] |
| Pizza Palace | 4.2 | 856 | Italian, Pizza | 456 Broadway | 40.7589 | -73.9851 | [link] |

You can:
- ✅ Sort by rating
- ✅ Filter by reviews
- ✅ Copy addresses
- ✅ Click URLs to visit businesses
- ✅ Use for business research
- ✅ Import into other tools

---

## 🎯 Real-World Examples

### Example 1: Finding Competitors
**Want:** All coffee shops in Seattle
1. Type: "coffee shops"
2. Location: "Seattle, WA"
3. Max Results: 100
4. Click "Start Scraping"
5. Get Excel file with 100 coffee shops!

### Example 2: Market Research
**Want:** Best-rated restaurants in Miami
1. Scrape "restaurants" in "Miami, FL"
2. Open CSV in Excel
3. Sort by "rating" column (highest first)
4. Filter for 4+ stars
5. Boom! List of top restaurants

### Example 3: Building Contact List
**Want:** Gyms to contact for marketing
1. Scrape "gyms" in "Los Angeles, CA"
2. Get addresses and URLs
3. Visit URLs to find contact info
4. Build your outreach list

---

## ❓ Troubleshooting

### "It's not working!"
1. Make sure you ran: `pip install -r requirements.txt`
2. Make sure you ran: `playwright install chromium`
3. Try closing and reopening Terminal

### "I can't open localhost:5000"
- Make sure `python app.py` is still running
- Try: http://127.0.0.1:5000 instead

### "Browser opens but nothing happens"
- This is normal! The browser works in the background
- Just wait for the green "Complete!" message

### "The download button doesn't work"
- Check your Downloads folder - it might already be there!
- Try right-click → "Save Link As..."

---

## 🛑 How to Stop

When you're done:
1. Go to Terminal/Command Prompt
2. Press **CTRL+C** to stop the server
3. Close the browser tab

---

## 💡 Pro Tips

1. **Start small**: Try 20-30 results first, then increase
2. **Use CSV**: It's easier to work with in Excel
3. **Be patient**: Scraping takes time (1-2 minutes for 50 results)
4. **Save often**: Download files as soon as they're ready
5. **Respect Google**: Don't scrape thousands at once

---

## 🎉 You're All Set!

No coding knowledge needed! Just:
1. Start the app: `python app.py`
2. Open browser: http://localhost:5000
3. Fill the form & click buttons
4. Download your data

**It's that simple!** 🚀
