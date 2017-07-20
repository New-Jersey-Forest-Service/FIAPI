#Example done on FA in Connecut
#import necessary libraries
import urllib2
import pandas as pd

#specify URL
table = "file:///C:/Users/TMccw/Anaconda2/FiaAPI/outFArea9.html"

#Query the website & return the html to the variable 'page'
page = urllib2.urlopen(table)

#import the bs4 functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable & store it in bs4 format
soup = BeautifulSoup(page, 'html.parser')

#Print out the html code with the function prettify
print soup.prettify()

#Find the tables & check type
table2 = soup.find_all('table')
print(table2)
print type(table2)

#Create new table as a dataframe
new_table = pd.DataFrame(columns=range(0,4))

#Pull the info from the three tables: Estimate, Sampleing Error, and # of non-zero plots in estimates
soup.find('table').find_all('td'),{'align':'right'}

#Remove tags from HTML code
## NOT COMPLETELY WORKING YET!
import re
from HTMLParser import HTMLParser
from htmlentitydefs import entitydefs

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
        self.entityref = re.compile('&[a-zA-Z][-.a-zA-Z0-9]*[^a-zA-Z0-9]')

    def handle_data(self, d):
        self.fed.append(d)

    def handle_starttag(self, tag, attrs):
        self.fed.append(' ')

    def handle_endtag(self, tag):
        self.fed.append(' ')

    def handle_entityref(self, name):
        if entitydefs.get(name) is None:
            m = self.entityref.match(self.rawdata.splitlines()[self.lineno - 1][self.offset:])
            entity = m.group()
            # semicolon is consumed, other chars are not.
            if entity[-1] != ';':
                entity = entity[:-1]
            self.fed.append(entity)
        else:
            self.fed.append(' ')

    def get_data(self):
        self.close()  # N.B. ensure all buffered data has been processed
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


print strip_tags('html &zzz; tags<p>&zzz &zz: will be&amp;replaced</p>with space. NOT this &abc')
