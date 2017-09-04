from PyEVALIDator import fetchTable
import csv
from EVALIDatorVars import *

def main():
    #define inputs for fetchTable
    #fetchTable(st, yr, nm, dn, pg, r, c, of)
    stateFile = open('NStates.csv')
    states = csv.reader(stateFile)
    ev = EVALIDatorVars()
    ev.nmDict.keys()
    st = 'NJ'
    yr = '2015'
    nm = "Net volume of live trees (at least 5 inches d.b.h./d.r.c.), in cubic feet, on forest land"
    dn = 'No denominator - just produce estimate.'
    pg = 'None'
    r = 'Stand-size%20class'
    c = 'Ownership%20group%20-%20Major'
    of = ''

    print "Let's make some tables!"
    for state in states:
        st = state[1]
        of = 'output'+st+'.html'
        fetchTable(st, yr, nm, dn, pg, r, c, of)
    print 'DONE!'
    stateFile.close()

if __name__ == '__main__':
    main()
