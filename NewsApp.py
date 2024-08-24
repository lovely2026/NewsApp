import requests
import json
api_key = "65666a6225614240b961b9a667893363"
url = "https://newsapi.org/v2/top-headlines"
country=input("Enter the country code (e.g. 'in' for india):")
allowed_categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
category=input("Enter the category of news from allowed categories :")
while True:
    if category in allowed_categories:
        break
    else:
        print("Invalid category. Please enter one of the following categories: ")
        category=input("Enter the category of news from allowed categories :")
while True:
    try:
        pgSize=int(input("Enter the no. of articles to retrieve :"))
        if pgSize>0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
dict = {"country": country,"apiKey": api_key,"pageSize": pgSize,"category":category}
response = requests.get(url, params=dict)
if response.status_code == 200:
    news = response.json()
    articles = news["articles"]
    if articles:
        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")      
    else:
        print("No articles found for the query(q).")
else:
    print("Failed to retrieve news")
