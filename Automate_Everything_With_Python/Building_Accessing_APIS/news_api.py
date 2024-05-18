import requests
r = requests.get(
    "https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-4-27&to=2024-4-28&sortBy=popularity&language=en&apiKey=993474c5a7264dc4ace54d782f2e76fa")

content = r.json()
print(type(content))
articles = content["articles"]
print(type(articles))

for article in articles:
    print(f"TITLE: {article["title"]}\n DESCRIPTION: {
          article["description"]}\n")
