import pandas as pd 
import requests 
import json 
from bs4 import BeautifulSoup 

url  = "https://www.flipkart.com"
r = requests.get(url)
print(r)