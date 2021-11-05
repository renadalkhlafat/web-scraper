import requests
from bs4 import BeautifulSoup

wikipedia_url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):

    res = requests.get(url)       
    b_soup = BeautifulSoup(res.text,"html.parser")
    result = b_soup.find_all("a", title="Wikipedia:Citation needed") 
    return len(result)

def get_citations_needed_report(url):
    citation = []
    res = requests.get(url)       
    b_soup = BeautifulSoup(res.text,"html.parser")
    results = b_soup.find_all("a", title="Wikipedia:Citation needed")

    for result in results:
        citation.append(result.parent.parent.parent.text)

    final = '\n'.join(citation)
    return final

# print(get_citations_needed_count(wikipedia_url))
print(get_citations_needed_report(wikipedia_url))