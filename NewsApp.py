import requests
api_key = "65666a6225614240b961b9a667893363"
url = "https://newsapi.org/v2/top-headlines"

dict1 = {"country": "in","apiKey": api_key,"pageSize": 2
             ,"category":"health"}
response = requests.get(url, params=dict1)

if response.status_code == 200:
    news_data = response.json()
    articles = news_data["articles"]
    if articles:
        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("-" * 40)
    else:
        print("No articles found for the query(q).")
else:
    print("Failed to retrieve news")
