# Web Scraper Example

## Libraries

- ***re:*** This module provides regular expression matching operations similar to those found in Perl. It is used for complex string searching and manipulation. You can define search patterns and use them to find, replace, or split data based on specified criteria.
  
- ***io.StringIO:*** Part of Python’s io module, StringIO is used to manage streams of text data. It allows you to treat a string as a file, which makes it useful for processes that expect file-like objects.

- ***json:*** This module implements JSON (JavaScript Object Notation) encoders and decoders for Python. It is commonly used for parsing JSON data into Python dictionaries or outputting Python dictionaries into JSON format.

- ***datetime, timedelta:*** Modules from Python’s datetime library for handling dates and times. datetime is used to create, manipulate, and format date and time data in a more flexible and powerful way than Python’s time module. timedelta is used for calculating differences in dates and times or for date manipulations in Python.

- ***seaborn (sns):*** A Python data visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.

- ***matplotlib.pyplot (plt):*** This module in the matplotlib library is used for plotting graphs. It offers functions for making a variety of static, animated, and interactive visualizations in Python.

- ***matplotlib.dates (mdates):*** A submodule of matplotlib that provides helper functions to handle date formatting in plots.

- ***wordcloud.WordCloud, wordcloud.STOPWORDS:*** These classes are part of the wordcloud library, which is used to generate word clouds from text. WordCloud lets you create the word cloud, while STOPWORDS provides a set of default words to exclude from it.

- ***plotly.express (px), plotly.graph_objects (go), plotly.io (pio):*** These modules are part of the Plotly library, which is used for making interactive and publication-quality graphs online. plotly.express is a simpler, high-level interface for Plotly, while plotly.graph_objects offers more flexibility and control over the graph objects.

- ***pandas (pd):*** A library providing high-performance, easy-to-use data structures, and data analysis tools for Python. DataFrame and Series are the primary data structures of pandas.

- ***numpy (np):*** Stands for Numerical Python, and it is the foundational package for scientific computing in Python. It provides a high-performance multidimensional array object and tools for working with these arrays.

- ***collections.Counter:*** A part of the collections module, Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

- ***unicodedata:*** This module provides access to the Unicode Character Database which defines character properties for all Unicode characters. It is used for testing properties of characters or for normalizing Unicode data.

- ***nltk.corpus.stopwords, nltk.stem.WordNetLemmatizer:*** Part of the Natural Language Toolkit (nltk), these modules are used for natural language processing. stopwords provides lists of overly common words (like "the", "is", etc.) that can be filtered out from text. WordNetLemmatizer is used for lemmatization, which reduces words to their base or root form.

- ***bs4.BeautifulSoup:*** A library for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.

- ***urllib.request.urlopen, urllib.request.Request:*** These functions from the urllib.request module are used to open URLs. urlopen is used to fetch URLs, and Request is used to create a request object with additional parameters.

- ***urllib.error.HTTPError, urllib.error.URLError:*** These are exception handling classes in the urllib.error module to handle exceptions raised by urllib.request functions.

-***lxml:*** the lxml library is a powerful and feature-rich library in Python used for parsing XML and HTML documents very quickly, even handling large files. It provides a simple and straightforward API for XML and HTML parsing using the real-world-tested and flexible libraries behind it. 

```python
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
```