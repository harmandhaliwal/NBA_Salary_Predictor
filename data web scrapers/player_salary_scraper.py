#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:02:26 2020

@author: NavD
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/contracts/players.html"
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

#Unable to extract headers using findAll(), may require updating headers for specific year
headers = ['Player', 'Team', '2019-20', '2020-21', '2021-22', '2022-23', '2023-24', '2024-25', 'Signed Using', 'Guaranteed']
headers

# avoid the first two header rows
rows = soup.findAll('tr')[2:]
player_contract_stats = [[td.getText() for td in rows[i].findAll('td')]
    for i in range(len(rows))]

contract_stats = pd.DataFrame(player_contract_stats, columns = headers)
contract_stats.head(10)

contract_stats.to_csv(r'Users\NavD\Desktop\nba_player_contract_stats.csv', header=True)