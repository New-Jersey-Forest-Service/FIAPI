# PyEVALIDator.py
# V 1.4
# NJ Forest Service, 11/2016
# Python 2.7
# dependencies: requests, bs4
import requests, sys
from bs4 import BeautifulSoup
# fetches table using FIA EVALIDator
# Batch URL for a given state
'''
st = FIA state code, yr = year, nm = numerator, dn = denominator,
pg = page variable, r = row variable, c = column variable,
of = output file name (currently html file), ot = output file type (currently xml)
all arguments are strings
'''
## TODO: add file type to arguments
def fetchTable (st, yr, nm, dn, pg, r, c, of, ot, lat = 0, lon =0, rad =0):
    outfile = open(of, 'wb')
    BASEADDR = 'https://apps.fs.usda.gov/Evalidator/rest/Evalidator/fullreport?'
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
    out = '&outputFormat='+ot
    OTHER = '&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom='
    url = BASEADDR+RETYPE+LAT+LON+RAD+num+den+stcode+yr+page+row+col+out+OTHER
    url = spaceReplace(url)
    json = requests.get(url)
    soup = BeautifulSoup(json.content, 'json.parser')
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
