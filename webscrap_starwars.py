# import non-built-in modules to make http requests
import requests

# ger html from site
url = 'https://www.starwars.com/news/15-star-wars-quotes-to-use-in-everyday-life'
response = requests.get(url)
print(response)
print(response.status_code)
url = response.headers
print(url)
headers = response.headers
print(headers)
body = response.text[:2000]
print(body) # Grabs the HTML from the page!! 
