from bs4 import BeautifulSoup
import requests

#scraping indeed.com
search = input("Enter job search:")
job_title_params = {"q": search, "l": 10314}
r = requests.get("http://indeed.com/jobs", params=job_title_params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("td", {"id": "resultsCol"})
links = results.findAll("div", {"class": "jobsearch-SerpJobCard"})

for item in links:
    indeed = "www.indeed.com"
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(indeed + item_href)
        print("Summary:", item.find("a").parent.parent.find("li").text)

#scraping monster.com
job_title_params = {"q": search, "where": 10314}
r = requests.get("https://www.monster.com/jobs/search", params=job_title_params)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("div", {"id": "SearchResults"})
links = results.findAll("div", {"class": "summary"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)