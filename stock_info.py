import urllib2
from bs4 import BeautifulSoup
import threading
file_lock = threading.Lock()
def main(stock, f):
    quote_page = 'https://www.bloomberg.com/quote/' + stock 
    page = urllib2.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
    name = name_box.text.strip() # strip() is used to remove starting and trailing


    current_price_box = soup.find('span', attrs={'class': 'priceText__1853e8a5'})
    current_price = current_price_box.text.strip()

    change_absolute_box = soup.find('span', attrs={'class': 'changeAbsolute__395487f7'});
    change_absolute = change_absolute_box.text.strip()

    change_percent_box = soup.find('span', attrs={'class': 'changePercent__2d7dc0d2'});
    change_percent = change_percent_box.text.strip()

    file_lock.acquire();
    f.write(name + ',' + current_price + ',' + change_absolute + ',' + change_percent + '\n')
    file_lock.release()

if __name__ == "__main__":
    main()
