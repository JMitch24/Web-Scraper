import requests
from bs4 import BeautifulSoup
from lxml import html
import requests
from termcolor import colored 
# Big thank you to SixBeeps(3265) who helped me out with figuring out how to import beautifulsoup module. Repl Forrum Disscussion that helped me: https://repl.it/talk/ask/How-do-i-download-beautifulsoup-to-my-repl/27035.  
topic_selection = input("What topics are ya\' lookin\' for today for today?: ")

url = "https://www.politico.com/"+topic_selection
page = requests.get(url)

soup= BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_= 'summary')

headline = article.h3.a.text
print(colored(headline, attrs=['bold']))


summary = article.p.text 
print(summary)



def politico_article_parse_for_collapsed (url, page, soup,):
  article = soup.find('div', class_= 'content-group tag-latest')

  headline = article.h3.a.text
  print(colored("\n" + headline, attrs=['bold']))
  

  article_link = article.h3.a
  for link in article_link:
      href =article_link.get("href")
      # print(href)

  url = (href)
  page = requests.get(url)
  soup= BeautifulSoup(page.content, 'lxml')
  article = soup.find('p', class_= 'dek')
  headline = article.text
  print (headline)

""""
  url = "https://www.politico.com/"+topic_selection
  page = requests.get(url)

  soup= BeautifulSoup(page.content, 'lxml')
  article = soup.find('div', class_= 'summary')

  
  
  print(article)
#summary = article.p.text 
"""
  




politico_article_parse_for_collapsed(url, page, soup)