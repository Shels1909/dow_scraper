import urllib2
import stock_info
import threading
from bs4 import BeautifulSoup

# This program gathers information on the DOW Jones industrial average

dow_page = 'https://www.bloomberg.com/quote/INDU:IND/members'

page = urllib2.urlopen(dow_page)

soup = BeautifulSoup(page, 'html.parser')

index_members = soup.find('div', attrs={'class': 'index-members'})

summaries = index_members.find_all('div', attrs={'class': 'security-summary'})

threads = []
for stock in summaries:
    name = stock.find('a' , attrs={'class': 'security-summary__ticker'}).text.strip()
    t = threading.Thread(target = stock_info.main, args=(name,))
    threads.append(t)
    t.start()
