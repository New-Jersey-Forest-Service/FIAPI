#This is a throwback to earlier implementations for testing
#changes to the FIA API URL
from PyEVALIDator import fetchTable
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

    print("Let's make some tables!")
    for state in states:
        st = ev.stateDict[state]
        ## TODO: Do we want to output the file as a .txt or .json file?? 
        of = 'output'+st+'.txt' 
        fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)
    print('DONE!')

if __name__ == '__main__':
    main()