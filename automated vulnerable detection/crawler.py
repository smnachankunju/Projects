import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def crawl(url):
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        print(f"[!] Error connecting to {url}: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")

    print(f"[+] Found {len(forms)} form(s) on {url}")
    return forms
