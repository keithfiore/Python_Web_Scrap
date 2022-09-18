# Reminder! https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
# import non-built-in modules to make http requests
import requests

# You need to use an html parser - so BeautifulSoup is introduced
from bs4 import BeautifulSoup

# Make use of comma separated value feature
import csv

# Used for further data cleansing
import numpy as np
import pandas as pd
import re
import io

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
quotes = soup.find_all('strong') # find the html strong tag, put it in the variable, quotes

# print(quotes) # what is in the quotes variable?? Let's look... This will be commented out after we add BeautilSoup

# Let's clean the data collected, too many <strong></strong> tags!
# This will remove the html tags leaving just plain text - which is what we want!
# for quote in quotes:
#    text_only_quote = quote.text # new variable to hold the text
#    # print(text_only_quote) # TEST - commented out after adding write
#   file.write(text_only_quote + '\n')

# Wow, such clean!! 

# add a way to export the quotes/data for use!
# add \|/ before the for loop to write the data to a local file
# with open('star_wars_html', 'w') as file:
#   file.write(text_only_quote + '\n' )
with open('star_wars', 'w') as file:
    for quote in quotes:
        text_only_quote = quote.text # new variable to hold the text
        print(text_only_quote) # TEST - commented out after adding write
        file.write(text_only_quote + '\n')



# Yuck spaces and gaps ... let's clean some more :)
# Great Reading Material About This! https://webautomation.io/blog/how-to-clean-web-scraping-data-using-python-beautifulsoup/

# You need to review this to be successful: https://docs.python.org/3.12/library/csv.html
with open('star_wars_quotes.csv', 'w') as csv_file:
    for quote in quotes:
        text_only_quote = quote.text.strip()
        writer = csv.writer(csv_file)
        writer.writerow([text_only_quote + '\n'])
