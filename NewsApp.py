import requests
from colorama import Fore, Style, init

init(autoreset=True)  

api_key = "65666a6225614240b961b9a667893363"
url = "https://newsapi.org/v2/top-headlines"
allowed_categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

print("allowed_categories =", allowed_categories)

category = input("Enter the category of news from allowed categories :").strip().lower()

while category not in allowed_categories:
    print("Invalid category. Please enter one of the following categories: ")
    category = input("Enter the category of news from allowed categories :").strip().lower()

while True:
    try:
        pgSize = int(input("Enter the no. of articles to retrieve :"))
        if pgSize > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

param = {"apiKey": api_key, "pageSize": pgSize, "category": category}
response = requests.get(url, params=param)

if response.status_code == 200:
    news = response.json()
    articles = news.get("articles", [])
    print("-"*100 )
    
    if articles:
        for index, article in enumerate(articles, start=1):         
            print(Fore.YELLOW + f"{index}. Title: {article.get('title', 'No Title')}")
            print(Fore.CYAN + f"   Source: {article.get('source', {}).get('name', 'Unknown Source')}")
            print(Style.BRIGHT + f"   Description: {article.get('description', 'No Description')}")
            print(Fore.BLUE + f"   URL: {article.get('url', 'No URL')}")

            print(Style.RESET_ALL + "-" * 100)
    else:
        print(Fore.RED + "No articles found for the given category.")
else:
    print(Fore.RED + f"Failed to retrieve news. Status code: {response.status_code}")
    print("Message:", response.text)
