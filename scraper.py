from lxml import html
import requests

# Make a request to the webpage
url = "https://www.walmart.com/"
response = requests.get(url)

# Parse the HTML content
tree = html.fromstring(response.content)

# Extract data using XPath
title = tree.xpath('//title/text()')[0]
print(title)
