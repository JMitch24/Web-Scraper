#This part of the code installs the nessacariy modules and libraries it needs to run
import requests
from bs4 import BeautifulSoup
from termcolor import colored
# This function below create a little decreative line to go inbettwen the diffrent News Source parsings. It returns a 40 long line pattern of "-_" when called. 
def dividing_line():
    x = 0
    while x < (100):
        print("-_", end='')
        x = x + 5


#This part of the code is the maininput from the user. It gets the users topic selection which with the code at it's current state destides between "congress" or "white-house". It reurtns the user's input in topic_selection which can gget tagged along at the end of url commands to find that specific news page based off of that topic. 
topic_selection = input("What topics are ya\' lookin\' for today for today?: ")
print("\n")

dividing_line()
print("Politco Articles: ")
#This code below crates the url form politico's base url plus it's adition /tags which topic_selection perfectly solted into. In the end cretes the url to Politco's Congrees or White House sections. 
url = "https://www.politico.com/" + topic_selection
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')


#The varible article below is what holds the parsed html from the website. 
article = soup.find('div', class_='summary')
#In the code blow headline searches throught the html stored in 'article' and finds the first h3 then a tag which it then removes its formating and outputs stright text
headline = article.h3.a.text
print("\n[0] \t" + colored(headline, attrs=['bold']))
#Below is where an article's summary is found and prased from 'article' defined above.
summary = article.p.text
print("\n" + summary)
#Below this code parse the href links brurrowed within a tags apart of the Article's headline and summary. 
article_link = article.h3.a
for link in article_link:
  href = article_link.get("href")
politico_zero_href = href



#This code section below works very siliar to that of the one above it. However what's unique about this block of code is that it parses from a diffrent location within url which allows for two articles to be parsed without findAll() and without the same reults being repeated. 
article = soup.find('div', class_='content-group tag-latest')
headline = article.h3.a.text
print(colored("\n [1] \t" + headline, attrs=['bold']))
article_link = article.h3.a
for link in article_link:
  href = article_link.get("href")
url = (href)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
#With the way html works something I never knew was the classifiactions that diffrent parts of it get. So below 'dek' is a class in which more information is stored underneth it but it was unuqie enough I could parse it wihout having to break it down furter. Then the 'p'stnads for the parargaph text identification the part of the code we want has on their website. 
article = soup.find('p', class_='dek')
summary = article.text
print("\n" + summary)
politico_one_href = href


dividing_line()
print("NPR Daily Podcasts: ")



#These next two chuncks of code below are the ones responsible for parrsing the urls to their audio recordings for their respecitive topics. The code directly below parses information from NPR Politics Podcast.
url = 'https://www.npr.org/podcasts/510310/npr-politics-podcast'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_='item-info')
headline = article.h2.a.text
#Below the colored(headline, attrs=['bold'])) code is a super amazing text module and library I found that allows for text to be easily bolded which allows the article titles to stand out. 
print("\n [2] \t" + colored(headline, attrs=['bold']))
summary = article.p.text
print(summary)
article_link = article.h2.a
for link in article_link:
  href = article_link.get("href")
npr_one_href = (href)
  


#This code bit beneath is what parse the most recent podcast headline and summary headline from NPR's own Up First podcast. 
url = 'https://www.npr.org/podcasts/510318/up-first'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')
article = soup.find('div', class_='item-info')
#What's super amazing and diffrent about the way NPR has their html set up. Within thier basic h2 and a tags as seen below is the Date of the release of the Podcast. My intial reaction was how quickly can I get rid of it but I kept it because the other two media sources are hard artticles and news that update more reguarly. But Podcasts are more spratic and distanced in times when they come out so it was left it to be a reference. 
headline = article.h2.a.text
print("\n [3] \t" + colored(headline, attrs=['bold']))
summary = article.p.text
print(summary)
article_link = article.h2.a
for link in article_link:
  href = article_link.get("href")
npr_two_href = (href)
#

dividing_line()
print("Washington Post Articles: ")

#Below in this next section of code is where the Waashinton Post's new's article is parsed from.
#Washington Post has their url and liks set up so weirdly that their 'congress' tab is actually called 'powerpost' so a create if else statment was needed as seen below to translate it to useable terms for the code and website. 
if topic_selection == "congress":
    topic_selection = "powerpost"
else:
    topic_selection = topic_selection
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
print("Links To The Articles: ")
#This code below is the what takes the user's input form the input question below and outputs the corresponding link to the article the user wanted to see.
user_article_choice =input("\n Which of the Articles Above do ya\' want to see: ")
#These if/else statments match up the links outut by each of the code sections above with the article headlines numerical value that was assigned to them
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
  print("Sorry that's not a valid article number to chose from.")



