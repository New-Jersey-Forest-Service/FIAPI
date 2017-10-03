Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Master Scrape 
# V1.0
# Python 2.7
# Abi Arya & Tim McWilliams

# Import needed packages 
import urlib2
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
url ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
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
url2 ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html2 = urllib2.urlopen(url2).read()
soup2 =BeautifulSoup(html2, "html.parser")
output2 = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title2=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col2 = map(cell_text2, row.find_all(re.compile('t[dh]')))
            output.writerow(col2)
        output.writerow([])
        
# Var 3
def cell_text3(cell):
    return " ".join(cell.stripped_strings)
url3 ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html3 = urllib2.urlopen(url3).read()
soup3 =BeautifulSoup(html3, "html.parser")
output3 = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title3=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col3 = map(cell_text3, row.find_all(re.compile('t[dh]')))
            output.writerow(col3)
        output.writerow([])

# Var 4
def cell_text4(cell):
    return " ".join(cell.stripped_strings)
url4 ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html4 = urllib2.urlopen(url4).read()
soup4 =BeautifulSoup(html4, "html.parser")
output4 = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title4=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col4 = map(cell_text4, row.find_all(re.compile('t[dh]')))
            output.writerow(col4)
        output.writerow([])
        
# Var 5
def cell_text5(cell):
    return " ".join(cell.stripped_strings)
url5 ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html5 = urllib2.urlopen(url5).read()
soup5 =BeautifulSoup(html5, "html.parser")
output5 = csv.writer(sys.stdout)

for table in soup.find_all('table'):
   # title=table.find('caption')
    title5=table.b
    if(title != None):
        print(title.string.extract())

        for row in table.find_all('tr'):
            col5 = map(cell_text5, row.find_all(re.compile('t[dh]')))
            output.writerow(col5)
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
    main()
