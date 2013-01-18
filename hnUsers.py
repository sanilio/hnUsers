# quick script to gather user names
# of submitters that are currently
# on the front page of hacker news

from bs4 import BeautifulSoup
import urllib2

soup = BeautifulSoup(urllib2.urlopen('http://news.ycombinator.com'))

users = []
                
for link in soup.find_all('a'):

    tmp = link.get('href')

    if 'user' in tmp:
            r = tmp.partition('=')
            users.append(r[2])


for u in users: print u
