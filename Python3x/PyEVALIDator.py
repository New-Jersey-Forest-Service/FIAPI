
# PyEVALIDator.py
# V 2.5
# NJ Forest Service, 09/2018
# Python 2.7, Python 3.X
# dependencies: requests, bs4
import requests, sys, json
from bs4 import BeautifulSoup
# fetches table using FIA EVALIDator
# Batch URL for a given state

'''
***This version of PyEVALIDator is stable as of 06/20/2019.***

st = FIA state code, yr = year, nm = numerator, dn = denominator,
pg = page variable, r = row variable, c = column variable,
of = output file name (currently html file), ot = output file type (json)
all arguments are strings
'''

def fetchTable (st, yr, nm, dn, pg, r, c, of, ot, lat = 0, lon =0, rad =0):
    outfile = open(of, 'w')
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
    if ot == 'JSON':
        jsonVar = response.json()
        json.dump(jsonVar, outfile)
    elif ot == 'HTML':
        soup = BeautifulSoup(response.content, 'html.parser')
        outfile.write(soup.prettify())
        outfile.close()
    elif ot == 'XML':
        soup = BeautifulSoup(response.content, 'html.parser')
        outfile.write(soup.prettify())
        outfile.close()
    else:
        print ("Please specify a valid output type")
        pass

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
'''
fetches unique plot CN's along with latitudes
and longitues in csv format
provide st = state, yrs = [year1,year2, year3...], of = outputfile.csv
'''
def fetchPlots(st, yrs, of):
    outfile = open(of, 'w')
    BASEADDR = 'https://apps.fs.usda.gov/Evalidator/rest/Evalidator/'
    BASEADDR += 'refTable?colList=CN,LON,LAT&tableName=PLOT&whereStr=statecd='
    stcode = str(st)+' and invyr in('
    numYrs = len(yrs)
    years = ''
    for year in yrs:
        numYrs -= 1
        if numYrs > 0:
            years += str(year)+','
        else:
            years += str(year)
    OTHER = ')&outputFormat=csv'
    url = BASEADDR+stcode+years+OTHER
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    outfile.write(soup.prettify())
    outfile.close()

if __name__ == '__main__':
   fetchTable()
