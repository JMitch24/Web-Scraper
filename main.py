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
print(politico_zero_href)

politico_main_article_parse(url, page, soup, topic_selection)


def politico_article_parse_for_collapsed(url, page, soup, headline_class,headline_tag, summary_tag,summary_class):
  article = soup.find(headline_tag, class_=headline_class)

  headline = article.h3.a.text
  print(colored("\n [1] \t" + headline, attrs=['bold']))

  article_link = article.h3.a
  for link in article_link:
    href = article_link.get("href")

  url = (href)
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'lxml')
  article = soup.find(summary_tag, class_=summary_class)
  summary = article.text
  print("\n" + summary)
  politico_two_href = (href)
  return politico_two_href


politico_one_collapased_headline_class = 'content-group tag-latest'
politico_one_collapased_headline_tag = 'div'
politico_one_collapased_summary_tag = 'p'
politico_one_collapased_summary_class = 'dek'

politico_article_parse_for_collapsed(
    url, page, soup, politico_one_collapased_headline_class,
    politico_one_collapased_headline_tag, politico_one_collapased_summary_tag,
    politico_one_collapased_summary_class)  #Politico 1st Collapsed


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


def npr_article_podcast(url):
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
  return npr_one_href


npr_article_podcast('https://www.npr.org/podcasts/510310/npr-politics-podcast')


def npr_article_podcast_uf(url):
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
  return npr_two_href


npr_article_podcast_uf('https://www.npr.org/podcasts/510318/up-first')

dividing_line()


def washpost_article_podcast(topic_selection):
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
  return wp_one_href


washpost_article_podcast(topic_selection)

dividing_line()

user_article_choice = int(input(
    "\n Which of the Articles Above do ya\' want to see: "))
def article_selection (user_article_choice, politico_zero_href, politico_one_href, npr_one_href, npr_two_href, wp_one_href):
  if user_article_choice == "0":
    article_url = politico_zero_href
    print(article_url)
  elif user_article_choice == "1":
    article_url = politico_one_href
    print(article_url)
  elif user_article_choice == "2":
    article_url = npr_one_href 
    print(article_url)
  elif user_article_choice == "3":
    article_url =  npr_two_href 
    print(article_url)
  elif user_article_choice == "4":
    article_url = wp_one_href 
    print(article_url)
  else:
    "Sorry that's not a valid article  number to chose from. Try again."
    user_article_choice()
    if user_article_choice == "0":
      article_url = politico_zero_href
      print(article_url)
    elif user_article_choice == "1":
      article_url = politico_one_href
      print(article_url)
    elif user_article_choice == "2":
      article_url = npr_one_href 
      print(article_url)
    elif user_article_choice == "3":
      article_url =  npr_two_href 
      print(article_url)
    elif user_article_choice == "4":
      article_url =wp_one_href 
      print(article_url)

article_selection(politico_zero_href, politico_one_href, npr_one_href, npr_two_href, wp_one_href)