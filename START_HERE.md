# ⭐ START HERE - Complete Setup Guide

## 🎯 What This Does
Extracts business data from Google Maps into an Excel spreadsheet. **No coding required!**

You'll get a beautiful web interface where you just click buttons and fill forms.

---

## 📋 What You Need (One-Time Setup)
- A computer (Mac or Windows)
- Python installed ([Download here](https://www.python.org/downloads/))
- 10 minutes

---

## 🚀 Installation (Copy & Paste These Commands)

### Step 1: Download the Project
Go to https://github.com/Benibenassi123/google-maps-scraper and click **"Code" → "Download ZIP"**

Unzip it to your Desktop.

### Step 2: Open Terminal/Command Prompt

**On Mac:**
- Press `Cmd + Space`
- Type "Terminal"
- Press Enter

**On Windows:**
- Press `Windows Key`
- Type "cmd"
- Press Enter

### Step 3: Navigate to the Project
```bash
cd Desktop/google-maps-scraper-main
```

### Step 4: Install Dependencies (One-Time)
```bash
pip install -r requirements.txt
playwright install chromium
```

This will take 2-3 minutes. Just wait for it to finish.

---

## ▶️ Running the Scraper

### Every time you want to use it:

1. **Open Terminal/Command Prompt**

2. **Navigate to folder:**
```bash
cd Desktop/google-maps-scraper-main
```

3. **Start the web interface:**
```bash
python app.py
```

4. **You'll see:**
```
🚀 Google Maps Scraper - Web Interface
✓ Server starting...

👉 Open your browser and go to:
   http://localhost:5000

❌ Press CTRL+C to stop the server
```

5. **Open your web browser** and go to:
```
http://localhost:5000
```

---

## 🖱️ Using the Web Interface

You'll see a beautiful purple interface with:

### Quick Start:
1. **Click** one of the quick examples:
   - 🍕 Pizza places in Chicago
   - ☕ Coffee shops in Seattle
   - 🏋️ Gyms in Los Angeles
   - 🏨 Hotels in Miami

2. **Or type your own:**
   - What: "restaurants", "dentists", "hotels", etc.
   - Where: "New York, NY", "Miami, FL", etc.

3. **Click "Start Scraping 🚀"**

4. **Wait** (1-2 minutes)

5. **Download** your Excel file!

---

## 📊 What You Get

An Excel file with columns:
- Business Name
- Rating (★ 4.5)
- Number of Reviews
- Category (Restaurant, Coffee Shop, etc.)
- Address
- GPS Coordinates
- Google Maps URL
- And more!

---

## 💡 Real Examples

### Example 1: Find Competitors
"I want all coffee shops in Seattle"
1. Type: `coffee shops`
2. Location: `Seattle, WA`
3. Click "Start Scraping"
4. Get Excel file with all coffee shops!

### Example 2: Market Research
"I need the best restaurants in Miami"
1. Scrape: `restaurants` in `Miami, FL`
2. Open Excel file
3. Sort by rating
4. Find the top ones!

### Example 3: Contact List
"I need gyms to contact"
1. Scrape: `gyms` in `Los Angeles, CA`
2. Get addresses + websites
3. Build your contact list!

---

## 🛑 Stopping the Scraper

When you're done:
1. Go back to Terminal/Command Prompt
2. Press `CTRL + C`
3. Close the browser tab

---

## ❓ Common Issues

### "Python not found"
Install Python from https://www.python.org/downloads/

### "pip not found"
Python should include pip. Try reinstalling Python.

### "Can't open localhost:5000"
- Make sure `python app.py` is running
- Try http://127.0.0.1:5000 instead
- Check if another program is using port 5000

### "Browser opens but nothing happens"
This is normal! The scraper works in the background. Just wait for the green checkmark.

### "No results found"
- Check your spelling
- Try a simpler search ("restaurants" instead of "fine dining restaurants")
- Make sure the location exists

---

## 🎓 Tutorial Videos

**For Mac Users:**
1. Open Terminal (Spotlight → Terminal)
2. Type: `cd Desktop/google-maps-scraper-main`
3. Type: `python app.py`
4. Open browser: http://localhost:5000

**For Windows Users:**
1. Open Command Prompt (Win Key → cmd)
2. Type: `cd Desktop\google-maps-scraper-main`
3. Type: `python app.py`
4. Open browser: http://localhost:5000

---

## 📞 Need More Help?

Read the detailed guide: [VISUAL_GUIDE.md](VISUAL_GUIDE.md)

---

## ✅ Quick Checklist

Before running, make sure you:
- [ ] Downloaded and unzipped the project
- [ ] Installed Python
- [ ] Ran `pip install -r requirements.txt`
- [ ] Ran `playwright install chromium`
- [ ] Opened Terminal/Command Prompt
- [ ] Navigated to project folder
- [ ] Ran `python app.py`
- [ ] Opened http://localhost:5000 in browser

---

## 🎉 You're Ready!

That's it! No coding knowledge needed. Just:
1. Start the app
2. Click buttons
3. Get your data

**Happy scraping!** 🚀
