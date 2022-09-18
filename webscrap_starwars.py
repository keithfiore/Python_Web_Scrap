# Reminder! https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
# import non-built-in modules to make http requests
import requests

# You need to use an html parser - so BeautifulSoup is introduced
from bs4 import BeautifulSoup

# get html from site
url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
response = requests.get(url)
# print(response) //USED for testing 
# print(response.status_code) //USED for testing
# url = response.headers //USED for testing
# print(url)  //USED for testing
headers = response.headers
# print(headers) //USED for testing
body = response.text[:2000]
# print(body) # //TEST Grabs the HTML from the page

# use of Beautfil Soup to identify the HTML tags for desired infor
# info = quotes and characters for the quotes
soup  = BeautifulSoup(response.text, 'html.parser')
quotes = soup.findAll('strong') # find the html strong tag
print(quotes)