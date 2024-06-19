############ Libraries ############

import re
from io import StringIO
import json
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from wordcloud import WordCloud, STOPWORDS
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import numpy as np
from collections import Counter
import unicodedata
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
stemmer = WordNetLemmatizer()
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import Request
import lxml



############ Code ############

# Testing server answer
try:
    html = urlopen("")
except HTTPError as e:
    print("The server returned an HTTP error")
except URLError as e:
    print("The server could not be found!")
else:
    print(html.read())


#### Auxiliar functions ####

# Getting title function
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


# Number of pages per state function
def numberOfpagesPerstate(bs):
    numPags = bs.find('select', class_="sorting nativeDropdown js-pagination-dropdown").get('data-pagination-end')
    if numPags is not None:
        num = int(numPags)
    else:
        num = 0
    return num


# Creating list of Main URL's 
def listMainURLs(nomState):
    MainUrls = []
    listURLs = list(MainUrls)
    n = numberOfpagesPerstate(bs)
    i=1
    while i<=n:
        aux = '........'+nomState+'........../?page='+ str(i)
        listURLs.append(aux)
        i+=1
    return listURLs

# Auxiliar function
def lM(bs):
    l = []
    lista= list(l)

    links = bs.find('div', class_ = "small-12 crosslinkTitle-links")
    arr = links.find_all('a')
    for pit in arr:
        ka = pit.get('href')
        lista.append(ka)
    return lista


#### Declaring variables ####

# Our DataFrame
df = pd.DataFrame()
df['tipo'] = None
df['precio'] = None
df['currency'] = None
df['metros_cuadrados'] = None
df['direccion'] = None
df['estado'] = None
df['latitud'] = None
df['longitud'] = None
df['link'] = None


# Temporal arrays
tipo = []
precio = []
currency = []
m2 = []
units = []
direccion = []
estado = []
latitud = []
longitud = []
link = []

# States names list
est = ['aguascalientes','baja-california', 
       'baja-california-sur', 'campeche', 
       'chiapas', 'chihuahua' , 
       'coahuila-de-zaragoza', 'colima', 
       'distrito-federal', 'durango', 
       'guanajuato' , 'guerrero',  
       'hidalgo', 'jalisco', 
       'mexico' , 'michoacan-de-ocampo', 
       'morelos', 'nayarit', 
       'nuevo-leon', 'oaxaca', 
       'puebla', 'queretaro-arteaga', 
       'quintana-roo', 'san-luis-potosi', 
       'sinaloa', 'sonora', 
       'tabasco','tamaulipas',
       'tlaxcala', 'veracruz-llave', 
       'yucatan', 'zacatecas']