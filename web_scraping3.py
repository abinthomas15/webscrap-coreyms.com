from bs4 import BeautifulSoup
import requests
import csv


url = "https://coreyms.com/"

page = requests.get(url).text
doc = BeautifulSoup(page,"html.parser")

csv_file = open('scraped.csv','w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Headline','Summary','Video-link'])

for article in doc.find_all('article'):

    headline = article.a.text
    print(headline)

    para = article.find('div',class_='entry-content').p.text
    print(para)

    try:
        link = article.find('span',class_='embed-youtube').iframe['src']
        link1 = link.split('/')[4]
        link2 = link1.split('?')[0]
        yt_link = f"https://youtube.com/watch?v={link2}"
    except:
        yt_link = None
    
    print(yt_link)

    print()

    csv_writer.writerow([headline,para,yt_link])

csv_file.close()