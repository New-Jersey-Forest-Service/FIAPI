#PyEVALIDator.py
#V 1.1
#William Zipse, NJ Forest Service, 11/2016
#Python 2.7
#dependencies: urllib2, BeautifulSoup
import urllib2, sys
from BeautifulSoup import BeautifulSoup

#fetches table using FIA EVALIDator
#Batch URL for a given state
'''
st = FIA state code, yr = year, nm = numerator, dn = denominator,
pg = page variable, r = row variable, c = column variable,
of = output file name (currently html file)
all arguments are strings
'''
def fetchTable (st, yr, nm, dn, pg, r, c, of):
    outfile = open(of, 'wb')
    BASEADDR = 'http://apps.fs.fed.us/Evalidator/batcheval.jsp?'
    RETYPE = 'reptype=State'
    LAT = '&lat=0'
    LON = '&lon=-0'
    RAD = '&radius=0'
    num = '&snum='+nm
    den = '&sdenom='+dn
    stcode = '&wc='+st
    #yr = yr
    page = '&pselected='+pg
    row = '&rselected='+r
    col = '&cselected='+c
    OTHER = '&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom='
    url = BASEADDR+RETYPE+LAT+LON+RAD+num+den+stcode+yr+page+row+col+OTHER
    url = spaceReplace(url)
    html = urllib2.urlopen(url).read()
    soup =BeautifulSoup(html)
    outfile.write(soup.prettify())
    outfile.close()

#replaces spaces with %20 for clean processing of URL's
#takes a string argument
def spaceReplace(s):
    string = s
    newStr = ''
    for char in string:
        if (char == ' '):
            newStr += '%20'
        else:
            newStr += char
    return newStr

    
    
