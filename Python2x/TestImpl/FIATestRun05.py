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
    r = 'Stand age 10 yr classes'
    c = 'Reserved status class'
    of = ''

    print "Let's make some tables!"
    for state in states:
        st = state[1]
        of = 'output'+st+'.html'
        fetchTable(st, yr, nm, dn, pg, r, c, of)
    print 'DONE!'

if __name__ == '__main__':
    main()
