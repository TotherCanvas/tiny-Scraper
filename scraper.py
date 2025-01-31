from lxml import html
import requests

# Fetch webpage
url = "https://www.walmart.com/"
response = requests.get(url)

# Parse HTML
tree = html.fromstring(response.content)

# Use CSS selector to get the title
title_element = tree.cssselect('title')[0]  # CSS selector "title"
title = title_element.text_content()        # Get text inside the tag

print(title)
