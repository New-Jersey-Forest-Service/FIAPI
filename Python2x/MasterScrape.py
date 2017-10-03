Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
# Master Scrape 
# V1.0
# Python 2.7
# Abi Arya & Tim McWilliams

# Import needed packages 
import urllib2
import sys
import re
import csv
from bs4 import BeautifulSoup 

# Create mulitple def's for each variable 

## NOTE: url's are the same. Can not currently access the website!! ##
######################################################################

# Section 1: Scraping functions

# Var 1
def cell_text1(cell):
    return " ".join(cell.stripped_strings)
url ="file:///C:/Users/TMccw/OneDrive/StateForestService/FIAPI/GitHub/FIAPI_Local/Python2x/outFArea10.html"
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text1, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])

# Var 2
def cell_text2(cell):
    return " ".join(cell.stripped_strings)
url ="file:///C:/Users/TMccw/OneDrive/StateForestService/FIAPI/GitHub/FIAPI_Local/Python2x/outFArea17.html"
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text2, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])
        
# Var 3
def cell_text3(cell):
    return " ".join(cell.stripped_strings)
url ="file:///C:/Users/TMccw/OneDrive/StateForestService/FIAPI/GitHub/FIAPI_Local/Python2x/outFArea18.html"
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text3, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])

# Var 4
def cell_text4(cell):
    return " ".join(cell.stripped_strings)
url ="file:///C:/Users/TMccw/OneDrive/StateForestService/FIAPI/GitHub/FIAPI_Local/Python2x/outFArea19.html"
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text4, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])
        
# Var 5
def cell_text5(cell):
    return " ".join(cell.stripped_strings)
url ="file:///C:/Users/TMccw/OneDrive/StateForestService/FIAPI/GitHub/FIAPI_Local/Python2x/outFArea20.html"
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col = map(cell_text5, row.find_all(re.compile('t[dh]')))
            output.writerow(col)
        output.writerow([])
        
# Final function that brings together and calls the functions in Section 1     
def main():
    cell_text1(cell)
    cell_text2(cell)
    cell_text3(cell)
    cell_text4(cell)
    cell_text5(cell)

# Calling the function 'main'
if __name__ == '__main__':
    print(main())
