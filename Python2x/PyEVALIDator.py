#PyEVALIDator.py
#V 1.3
#NJ Forest Service, 11/2016
#Python 2.7
#dependencies: requests, bs4
import requests, sys
from bs4 import BeautifulSoup
#testing push
#fetches table using FIA EVALIDator
#Batch URL for a given state
'''
st = FIA state code, yr = year, nm = numerator, dn = denominator,
pg = page variable, r = row variable, c = column variable,
of = output file name (currently html file)
all arguments are strings
'''
def fetchTable (st, yr, nm, dn, pg, r, c, of, lat = 0, lon =0, rad =0):
    outfile = open(of, 'wb')
    BASEADDR = 'http://apps.fs.fed.us/Evalidator/batcheval.jsp?'
    if(lat==0 and lon ==0 and rad ==0):
        RETYPE = 'reptype=State'
    else:
        RETYPE = 'reptype=Circle'
    LAT = '&lat=' + str(lat)
    LON = '&lon=' + str(lon)
    RAD = '&radius=' + str(rad)
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
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
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
