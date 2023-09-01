import requests
from send_email import send_email

api_key = "a0cc6556f72142ff868ceb690ef177bc"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "a0cc6556f72142ff868ceb690ef177bc"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
