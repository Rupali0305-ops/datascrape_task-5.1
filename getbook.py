
from utils.getprice import extractPrice
def extractbook(book):
    img = book.find('div', attrs = {'class':'image_container'}).a.img
    imgdata = {
        'src': img.attrs['src'],
        'alt': img.attrs['alt']
    }
    price = extractPrice(book)
    ratings = book.find('p',attrs={'class': 'star-rating'}).attrs['class'][1]


    title = book.find('h3').a.attrs['title']
    bookdata = {
        'imgdata': imgdata,
        'price': price,
        'rating': ratings,
        'title': title
        
    }

    return bookdata