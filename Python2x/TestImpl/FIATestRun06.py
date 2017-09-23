'''
This implementation tests fetchTable() from
PyEVALIDator and adds row and column variable
tests from EVALIDatorVars
'''
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
    nm = ev.nmDict['atl']
    dn = ev.dmDict['nodenominator']
    pg = 'None'
    #r = 'Stand age 10 yr classes'
    #c = 'Reserved status class'
    r = ev.rowDict['sa10']
    c = ev.colDict['rss']
    of = ''

    print "Let's make some tables!"
    for state in states:
        st = ev.stateDict[state]
        of = 'output'+st+'.html'
        fetchTable(st, yr, nm, dn, pg, r, c, of)
    print 'DONE!'

if __name__ == '__main__':
    main()
