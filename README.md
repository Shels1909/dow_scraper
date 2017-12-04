# Dow Jones Industrial Average Scraper
![alt text](https://upload.wikimedia.org/wikipedia/en/f/f8/Dow_Jones_Logo.svg)

This tool scrapes www.bloomberg.com for data on the Dow Jones Industrial Average. The Dow Jones is a stock market index of 30 large publicly traded US companies.

This script requires Python 2.7. You will also need Beautiful Soup 4, an HTML parsing library. You can download Beautiful Soup 4 with `pip install beautifulsoup4`

---

 If you execute the *dow.py* file in your command line with no arguments, the program will fetch and create a csv file with all 30 Dow Jones Companies including their name, ticker, price, change, and percent change. If you execute the command with a ticker as an argument, for example `./dow.py AAPL:US`, it will grab more detailed information about the company and its stock.  
