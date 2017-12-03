#!/usr/bin/python

import urllib2
import threading
import sys
from bs4 import BeautifulSoup
file_lock = threading.Lock()

# This program gathers information on the DOW Jones industrial average

def main():
    if(len(sys.argv) > 1):
        get_ticker_info(sys.argv[1])    
    
    else:
        get_agg_info()

def get_agg_info():
    dow_page = 'https://www.bloomberg.com/quote/INDU:IND/members'

    page = urllib2.urlopen(dow_page)

    soup = BeautifulSoup(page, 'html.parser')

    index_members = soup.find('div', attrs={'class': 'index-members'})

    summaries = index_members.find_all('div', attrs={'class': 'security-summary'})

    # clear the results csv file
    open('results.csv', 'w').close()

    # write the correct header for the file
    f = open('results.csv', 'a')
    f.write("Name,Ticker,Price,Change,% Change\n")
    threads = []
    for stock in summaries:
        ticker = stock.find('a' , attrs={'class': 'security-summary__ticker'}).text.strip()
        t = threading.Thread(target = stock_info, args=(ticker,f,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    f.close()
def stock_info(ticker, f):

    quote_page = 'https://www.bloomberg.com/quote/' + ticker
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
    f.write(name + ',' + ticker + ',' + current_price + ',' + change_absolute + ',' + change_percent + '\n')
    file_lock.release()


def get_ticker_info(ticker):
    quote_page = 'https://www.bloomberg.com/quote/' + ticker
    page = urllib2.urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')
    
    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
    name = name_box.text.strip() # strip() is used to remove starting and trailing


    current_price_box = soup.find('span', attrs={'class': 'priceText__1853e8a5'})
    current_price = current_price_box.text.strip()

    change_absolute_box = soup.find('span', attrs={'class': 'changeAbsolute__395487f7'})
    change_absolute = change_absolute_box.text.strip()

    change_percent_box = soup.find('span', attrs={'class': 'changePercent__2d7dc0d2'})
    change_percent = change_percent_box.text.strip()
    
    open_price_box = soup.find('section', attrs={'class': 'dataBox open__4a13b8c3 numeric'}).find('div', attrs={'class': 'value__b93f12ea'})
    open_price = open_price_box.text.strip()

    close_prev_box = soup.find('section', attrs={'class': 'dataBox prev-close__08d99bee numeric'}).find('div', attrs={'class': 'value__b93f12ea'})
    close_prev = close_prev_box.text.strip()
    
    volume_box = soup.find('section', attrs={'class': 'dataBox volume__d82b3d8c numeric'}).find('div', attrs={'class': 'value__b93f12ea'})
    volume = volume_box.text.strip()

    market_cap_box = soup.find('section', attrs={'class': 'dataBox market-cap__a8440c6b numeric'}).find('div', attrs={'class': 'value__b93f12ea'})
    market_cap = market_cap_box.text.strip()

    print name + "\n"
    print "Current Price: " + current_price + "\n"
    print "Change Absolute: " + change_absolute + "\n"
    print "Change Percent: " +  change_percent + "\n"
    print "Opening Price: " + open_price + "\n"
    print "Prev Close Price: " + close_prev + "\n"
    print "Volume: " + volume + "\n"
    print "Market Cap: " + market_cap + "\n"
if __name__ == "__main__":
    main()
