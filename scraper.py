# import required packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from datetime import datetime


# create Webpage class
class Webpage:
    def __init__(self, name, url, element, sep1, sep2):
        self.name = name
        self.url = url
        self.element = element
        self.sep1 = sep1
        self.sep2 = sep2

    # method to parse tabular webpage and return chosen tags as an array for further processing
    def raw(self):
        try:
            raw = []
            content = BeautifulSoup(requests.get(self.url).text, 'html.parser')
            # loop through all chosen tags
            for tag in content.find_all(self.element):
                # append each parsed tag according to the chosen separators to raw list
                raw.append(tag.get_text(separator=self.sep1).split(self.sep2))
            return np.array(raw, dtype='object')
        # return an error message if the page doesn't allow scraping or there's some connection error
        except:
            return "Connection error, the page might not allow scraping!"

    # method similar to raw() but exports data as a .csv file for later use
    def raw_csv(self):
        try:
            raw = []
            content = BeautifulSoup(requests.get(self.url).text, 'html.parser')
            for tag in content.find_all(self.element):
                raw.append(tag.get_text(separator=self.sep1).split(self.sep2))
            # save file named with its time stamp
            return pd.DataFrame(raw).to_csv(self.name + '_' + datetime.now().strftime("%d_%m_%Y_%H_%M") + '.csv')
        except:
            return "Connection error, the page might not allow scraping!"


if __name__ == '__main__':
    # show use cases of the script
    yahoo_finance = Webpage('yahoo_finance', 'https://finance.yahoo.com/cryptocurrencies/', 'tr', ' ', ' ')

    binance = Webpage('binance', 'https://https://www.binance.com/en/markets/', 'div', ' ', ' ')

    coin_gecko = Webpage('coin_gecko', 'https://www.coingecko.com/', 'tr', ' ', '\n')

    crypto = Webpage('crypto.com', 'https://crypto.com/price', 'tr', ' ', ' ')

    # return raw data
    yahoo_finance.raw()

    binance.raw()

    coin_gecko.raw()

    crypto.raw()

    # export raw data to csv
    yahoo_finance.raw_csv()

    binance.raw_csv()

    coin_gecko.raw_csv()

    crypto.raw_csv()
