import requests
from bs4 import BeautifulSoup
from lxml import html
import requests
from termcolor import colored


def dividing_line():
    x = 0
    while x < (100):
        print("-_", end='')
        x = x + 5


# Big thank you to SixBeeps(3265) who helped me out with figuring out how to import beautifulsoup module. Repl Forrum Disscussion that helped me: https://repl.it/talk/ask/How-do-i-download-beautifulsoup-to-my-repl/27035.

topic_selection = input("What topics are ya\' lookin\' for today for today?: ")
print("\n")

dividing_line()

url = "https://www.politico.com/" + topic_selection
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')



article = soup.find('div', class_='summary')

headline = article.h3.a.text
print("\n[0] \t" + colored(headline, attrs=['bold']))

summary = article.p.text
print("\n" + summary)
article_link = article.h3.a
for link in article_link:
  href = article_link.get("href")

politico_zero_href = href




article = soup.find('div', class_='content-group tag-latest')

headline = article.h3.a.text
print(colored("\n [1] \t" + headline, attrs=['bold']))

article_link = article.h3.a
for link in article_link:
  href = article_link.get("href")

url = (href)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('p', class_='dek')
summary = article.text
print("\n" + summary)
politico_one_href = href






def dividing_line():
    x = 0
    while x < (100):
        print("-_", end='')
        x = x + 5


dividing_line()
import datetime

date = datetime.datetime.now()

date_year = date.strftime("%Y")
date_month = date.strftime("%m")
date_day = date.strftime("%d")


url = 'https://www.npr.org/podcasts/510310/npr-politics-podcast'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_='item-info')

headline = article.h2.a.text
print("\n [2] \t" + colored(headline, attrs=['bold']))

summary = article.p.text
print(summary)

article_link = article.h2.a
for link in article_link:
  href = article_link.get("href")
npr_one_href = (href)
  



url = 'https://www.npr.org/podcasts/510318/up-first'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_='item-info')

headline = article.h2.a.text
print("\n [3] \t" + colored(headline, attrs=['bold']))

summary = article.p.text
print(summary)

article_link = article.h2.a
for link in article_link:
  href = article_link.get("href")
npr_two_href = (href)
 




dividing_line()



if topic_selection == "congress":
    topic_selection = "powerpost"
else:
    topic_selection = "congress"

url = "https://www.washingtonpost.com/politics/" + topic_selection
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_='story-headline')
headline = article.h2.a.text
print("\n [4] \t" + colored(headline, attrs=['bold']))

article_link = article.h2.a
for link in article_link:
  href = article_link.get("href")

article = soup.find('div', class_='story-description')
summary = article.p.text
print("\n" + summary)
wp_one_href = (href)





dividing_line()

user_article_choice =input("\n Which of the Articles Above do ya\' want to see: ")

if user_article_choice == "0":
  article_url = politico_zero_href
  page = requests.get(article_url)
  soup = BeautifulSoup(page.content, 'lxml')
  article = soup.find('div', class_='story-text')
  print(article.text)
  
  

elif user_article_choice == "1":
  article_url = politico_one_href
  page = requests.get(article_url)
  soup = BeautifulSoup(page.content, 'lxml')
  article = soup.find('div', class_='container__column container__column--story center-horizontally')
  print(article.text)
elif user_article_choice == "2":
  article_url = npr_one_href 
  print(article_url)
elif user_article_choice == "3":
  article_url =  npr_two_href\
  print(article_url) 
elif user_article_choice == "4":
  article_url = wp_one_href
  print(article_url) 
else:
  print("Sorry that's not a valid article number to chose from.")




