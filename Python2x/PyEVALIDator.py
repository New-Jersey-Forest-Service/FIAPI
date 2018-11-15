
# PyEVALIDator.py
# V 2.0
# NJ Forest Service, 09/2018
# Python 2.7
# dependencies: requests, bs4
import requests, sys, json
from bs4 import BeautifulSoup
# fetches table using FIA EVALIDator
# Batch URL for a given state

'''
***This version of PyEVALIDator is stable as of 09/16.  It
is designed to correct issues with the EVALIDator URL changes.***

st = FIA state code, yr = year, nm = numerator, dn = denominator,
pg = page variable, r = row variable, c = column variable,
of = output file name (currently html file), ot = output file type (json)
all arguments are strings
'''

def fetchTable (st, yr, nm, dn, pg, r, c, of, ot, lat = 0, lon =0, rad =0):
    #outfile = open(of, 'w')
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
    page = '&pselected='+pg
    row = '&rselected='+r
    col = '&cselected='+c
    OTHER = '&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom=&FIAorRPA=FIADEF&outputFormat='+ot+'&estOnly=N&schemaName=FS_FIADB.'
    url = BASEADDR+RETYPE+LAT+LON+RAD+num+den+stcode+yr+page+row+col+OTHER
    url = spaceReplace(url)
    response = requests.get(url)
    jsonVar = response.json()
    return response
    #return jsonVar
    #json.dump(jsonVar, outfile)

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
