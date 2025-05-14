import requests
from bs4 import BeautifulSoup
from googlesearch import search

def page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else 'No title'
    return url, title

def main():
    query = input("Entrez votre requête de recherche : ")
    for url in search(query, num_results=100000):
        url, title = page(url)
        print(f"URL: {url}\nTitre: {title}\n")

if __name__ == "__main__":
    main()
