#This is a throwback to earlier implementations for testing
#changes to the FIA API URL
from PyEVALIDator import fetchTable
from bs4 import BeautifulSoup
import csv
from EVALIDatorVars import *

def main():
    #define inputs for fetchTable
    #fetchTable(st, yr, nm, dn, pg, r, c, of)
    states = ['NJ','NY','MD']
    ev = EVALIDatorVars()
    st = ''
    yr = '2015'
    nm = 'Area of timberland, in acres'
    dn = ev.dmDict['nodenominator']
    pg = 'None'
    #r = 'Stand age 10 yr classes'
    #c = 'Reserved status class'
    r = 'Stand age 10 yr classes'
    c = 'Reserved status class'
    of = ''
    ot = 'JSON'

    print("Let's get some data!")
    for state in states:
        st = ev.stateDict[state]
        of = 'output'+st+'.json' 
        fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)

    print ('...and now for the html!')
    ot = 'HTML'
    for state in states:
        st = ev.stateDict[state] 
        of = 'output'+st+'.html' 
        fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)

    print('DONE!')

if __name__ == '__main__':
    main()
