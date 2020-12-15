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



def politico_article_parse_for_collapsed (url, page, soup,headline_class, headline_tag, summary_tag, summary_class):
  article = soup.find(headline_tag, class_= headline_class)
   
  headline = article.h3.a.text
  print(colored("\n" + headline, attrs=['bold']))
  

  article_link = article.h3.a
  for link in article_link:
      href =article_link.get("href")
      

  url = (href)
  page = requests.get(url)
  soup= BeautifulSoup(page.content, 'lxml')
  article = soup.find(summary_tag, class_= summary_class)
  headline = article.text
  print (headline)


  


"""
politico_one_collapased_headline_class = 'content-group tag-latest'
politico_one_collapased_headline_tag = 'div'
politico_one_collapased_summary_tag = 'p'
politico_one_collapased_summary_class = 'dek'

politico_article_parse_for_collapsed(url, page, soup, politico_one_collapased_headline_class, politico_one_collapased_headline_tag, politico_one_collapased_summary_tag, politico_one_collapased_summary_class)  #Politico 1st Collapsed
"""






def politico_article_parse_for_collapsed_two (url, page, soup,headline_class, headline_tag, article):
  article = soup.find_all('div', class_= "stor-frag format-m")
  
  
  headline = article.find('a', class_= 'summary')
  #print(colored("\n" + headline, attrs=['bold']))
  article_print = colored("\n" + (article.text), attrs=['bold'])
  print(article) 

  

article_link = article.h3.a
for link in article_link:
    href =article_link.get("href")
    


headline = article.text
print (href)
  




