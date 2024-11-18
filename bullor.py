import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Fetch the article
url = "https://www.tipranks.com/news/the-fly/tesla-put-buyer-realizes-35-same-day-gains"
response = requests.get(url)
html_content = response.text

# Parse the HTML content and extract text
soup = BeautifulSoup(html_content, 'html.parser')
article_text = soup.get_text()

# Perform sentiment analysis
analysis = TextBlob(article_text)
polarity = analysis.sentiment.polarity

# Determine Bullish or Bearish
if polarity > 0:
    sentiment = "Bullish"
elif polarity < 0:
    sentiment = "Bearish"
else:
    sentiment = "Neutral"

print(f"The article sentiment is: {sentiment}")
