# Simple Web Scraper with XPath

This is a very simple Python-based web scraper I created for fun to extract the title from any web page using CSS selectors.

## What Inspired Me?

I came across a fascinating [Reddit post](https://www.reddit.com/r/InternetIsBeautiful/comments/118y19p/i_made_a_site_that_tracks_the_price_of_eggs_at/) about someone who built a website to track the price of eggs at every Walmart in the US using a custom scraper. That project piqued my interest in web scraping. I started with XPath but discovered CSS selectors - a more familiar syntax since I already know CSS from web development.

---

## Usage

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
   ```

2. Install the lxml library from pip
   ```bash
   pip install lxml requests
   ```

3. Run the program:
   ```bash
   python scraper.py
   ```

4. In line 5, you can enter any url that you prefer

---

## How It Works

This script demonstrates:
1. Making HTTP requests using `requests`.
2. Parsing the HTML content using `lxml`.
3. Targeting elements using CSS selectors
4. Extracting text content from HTML elements

### Example

If the url we input is:
```python
url = "https://www.unimelb.edu.au/"
```

we would get:
```
The University of Melbourne - Australia's #1 Ranked University
```

since that is the tile of the website.

If the url we input is:
```python
url = "https://www.walmart.com/"
```

we would get:
```
Walmart | Save Money. Live better.
```