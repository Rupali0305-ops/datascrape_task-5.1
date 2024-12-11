import requests as rq
from bs4 import BeautifulSoup
from bs4.element import NavigableString

import pandas as pd

from getbook import extractbook

bookurl = 'https://books.toscrape.com/'

bookheader = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}

bookresp = rq.get(url=bookurl,headers=bookheader)

booksoup = BeautifulSoup(bookresp.content, "html.parser") 
#booksoup = BeautifulSoup(bookresp.content,'html parser')

ratings = booksoup.find_all('p',attrs={'class': 'star-rating'})

for r in ratings:
    print(r.attrs['class'][1])

bookprice = booksoup.find_all('p',attrs={'class': 'price_color'})

for p in bookprice:
    print(p.text)



books = [extractbook(book) for book in booksoup.find_all('article',{'class':"product_pod"})
]
booksDf = pd.DataFrame(books)

booksDf.to_csv('books.csv')
#print(books)

    
    