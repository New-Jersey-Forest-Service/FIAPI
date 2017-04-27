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
soup = BeautifulSoup(page, 'lxml')

#Print out the html code with the function prettify
print soup.prettify()

#Find the table & check type
table2 = soup.find_all('table')
print(table2)
print type(table2)

#Create new table as a dataframe
new_table = pd.DataFrame(columns=range(0-4))


for row in table2('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1

