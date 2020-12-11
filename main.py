import requests
from bs4 import BeautifulSoup
from lxml import html
import requests
# Big thank you to SixBeeps(3265) who helped me out with figuring out how to import beautifulsoup module. Repl Forrum Disscussion that helped me: https://repl.it/talk/ask/How-do-i-download-beautifulsoup-to-my-repl/27035.  
topic_selection = input("What topics are ya\' lookin\' for today for today?: ")

url = "https://www.politico.com/congress"+topic_selection
page = requests.get(url)

