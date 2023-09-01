import requests

api_key = "a0cc6556f72142ff868ceb690ef177bc"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "a0cc6556f72142ff868ceb690ef177bc"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])