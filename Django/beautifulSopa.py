import requests as req
from bs4 import BeautifulSoup
url="https://www.bbc.com/news"
response=req.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.text,"html.parser")
    requiredTag='h3'
    headlines=soup.find_all(requiredTag)
    if headlines:
        for headline in headlines:
            print(f"Headline: {headline.text}")
    else:
        print(f"No {requiredTag} tags found in the website.")
else:
    print("Failed to retrieve the page.")