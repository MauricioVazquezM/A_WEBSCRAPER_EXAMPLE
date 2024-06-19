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
from asyncio.windows_events import NULL
from operator import contains


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
def numberOfpagesPerstate(aux):
    numPags = aux.find('select', class_="sorting nativeDropdown js-pagination-dropdown").get('data-pagination-end')
    if numPags is not None:
        num = int(numPags)
    else:
        num = 0
    return num


# Creating list of Main URL's 
def listMainURLs(nomState, aux):
    MainUrls = []
    listURLs = list(MainUrls)
    n = numberOfpagesPerstate(aux)
    i=1
    while i<=n:
        aux = '..........'+nomState+'...........'+ str(i)
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


#### Scraper ####

# Scraper function
def scraper():

    for st in est:
        
        urlAux = '...........'+st+'.............'
        req = Request(urlAux, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            webpageAux = urlopen(req).read()
        except HTTPError as e:
            print("The server returned an HTTP error in: "+st)
        except URLError as e:
            print("The server could not be found! in: "+st)
        else:
            aux = BeautifulSoup(webpageAux, 'html.parser')
            listURLs = listMainURLs(st, aux)

            for ur in listURLs: 
                
                url = ur
                req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    webpage = urlopen(req).read()
                except HTTPError as e:
                    print("The server returned an HTTP error in: "+ur)
                except URLError as e:
                    print("The server could not be found! in: "+ur)
                else:
                    bs2 = BeautifulSoup(webpage, 'html.parser')

                    terrenos = bs2.find_all('div', class_='row ListingCell-row ListingCell-agent-redesign')

                    print(ur)
                    
                    for terreno in terrenos:
                        price_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit')
                        category_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit')
                        land_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit')
                        state_info = terreno.find('span', class_='ListingCell-KeyInfo-address-text')
                        geo_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit')
                        link_info = terreno.find('a', class_='js-listing-link')
                        second_price = terreno.find('span', class_='PriceSection-SecondPrice')

                        if category_info is not None:
                            category_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-category')
                            tipo.append(category_info)
                        else:
                            tipo.append('NaN')
                            
                        if second_price is not None:
                            second_price = terreno.find('span', class_='PriceSection-SecondPrice').text.replace(' ','')
                            precio.append(second_price.strip().replace('US$','').replace(',',''))
                            currency.append('USD')
                        else:
                            price_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-price')
                            precio.append(price_info)
                            currency.append('MXN')

                        if land_info is not None:
                            land_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-land_size')
                            m2.append(land_info)
                            units.append('m2')
                        else:
                            m2.append('NaN')
                            units.append('NaN')

                        if state_info is not None:
                            state_info = terreno.find('span', class_='ListingCell-KeyInfo-address-text').text.strip().lower().replace(',',' ')
                            direccion.append(state_info)
                        else:
                            direccion.append('NaN')

                        estado.append(st)

                        if geo_info is not None and geo_info is not NULL:
                            geo_info = terreno.find('div', class_='ListingCell-AllInfo ListingUnit').get('data-geo-point').replace(']','').replace('[','').split(',')
                            #print(geo_info)
                            if geo_info is not None and geo_info is not NULL and 'null' not in geo_info:
                                kk = np.float64(geo_info)
                                latitud.append(kk[1])
                                longitud.append(kk[0])
                            else:
                                latitud.append('NaN')
                                longitud.append('NaN')
                        else:
                            latitud.append('NaN')
                            longitud.append('NaN')

                        if link_info is not None:
                            link_info = terreno.find('a', class_='js-listing-link').get('href')
                            link.append(link_info)
                        else:
                            link.append('NaN')



#### Execution ####
scraper()


#### Checking arrays length ####
print(len(tipo))
print(len(precio))
print(len(currency))
print(len(m2))
print(len(direccion))
print(len(estado))
print(len(latitud))
print(len(longitud))
print(len(link))


#### Setting dataframe data ####
df['tipo'] = tipo
df['precio'] = precio
df['currency'] = currency
df['metros_cuadrados'] = m2
df['direccion'] = direccion
df['estado'] = estado
df['latitud'] = latitud
df['longitud'] = longitud
df['link'] = link
units = []
i=0
while i<=49222:
        units.append('m2')
        i+=1
df['units'] = units


#### Parsing dataframe to a CSV ####
df.to_csv('scraping_results.csv')