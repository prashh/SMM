# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

## In the following segment, we show how you can get a list of news article URLs based on a keyword search.
## We use Jacobin mag as an example but we recommend you scrape more mainstream/well-known and neutral news sources.

list_url = "https://www.nytimes.com/search?query=election+2020"

uClient = uReq(list_url)
read_html = uClient.read()
uClient.close()
page_soup = soup(read_html, "html.parser")
domain_url = "https://nytimes.com"
text_sections = page_soup.find("div", {"class": "css-46b038"}).find_all("a")
## The previous line will not be the same for all websites. Go to the desired website on your browser, right-click and do "Inspect element"
## to see how the website HTML is structured. This will take a bit of time and patience
article_urls = []

for i in text_sections:
    if "/2020/" in i.get("href"):
        t = domain_url + i.get("href")
        article_urls.append(t)


### The following is some code to show how you would extract each news article. For multiple URLs,
### iterate over the list of URLs you scraped in the previous step.

cnn_url = "https://www.nytimes.com/2020/09/16/us/politics/michael-caputo-hhs-leave-of-absence.html"



# for CNN:
# <div class="zn-body__paragraph"> text </div>
# for Jacobin:
# <div id="post-content" class="po-cn__intro.po-wp__intro">


'''def text_from_html(read_html, site):
    page_soup = soup(read_html, "html.parser")
    if site == "nytimes":
        #find which div
        text_sections = page_soup.find_all("div", {"class": "css-1fanzo5 StoryBodyCompanionColumn"})
        joined_texts = ""
        for i in text_sections:
            joined_texts += i.text
        return joined_texts
'''

## main
for i in article_urls:
    cnn_url = i
    uClient = uReq(cnn_url)
    read_html = uClient.read()
    uClient.close()
    page_soup = soup(read_html, "html.parser")

    headline = page_soup.find("h1", {"class": "css-rsa88z e1h9rw200"})

    text_sections = page_soup.find("div", {"class": "css-53u6y8"}).find_all("p")
    # These two lines will also vary across websites. Inspect element to find out how you should extract the text.

    article = ""
    for i in text_sections:
        article += i.text

    with open('elections.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([headline.text, article])
    print(headline.text)  # headline printed for demo
    print(article)  # printed just for demo, you need to store it, maybe in a csv file'''

