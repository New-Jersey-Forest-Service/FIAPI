#approx port of FiaTestRun03.py for CI; stripped out read csv to remove deps
# test for ?

import unittest
import pytest

from PyEVALIDator import fetchTable
#import csv

def main():
    i = 1
    while (i < 4):
        #define inputs for fetchTable
        #fetchTable(st, yr, nm, dn, pg, r, c, of)
        states = ('33','34','35')
        st = ''
        yr = '2015'
        nm = ''
        dn = ''
        pg = 'None'
        r = 'Forest type group'
        c = 'Ownership group'
        of = ''
        if (i == 1):
            nm = 'Area of forest land, in acres'
            dn = 'No denominator - just produce estimate.'
            ofprfix = 'FArea'
        elif (i == 2):
            nm = 'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land'
            dn = 'No denominator - just produce estimate.'
            ofprfix = 'GsTrees'
        else:
            nm = 'Number of growing-stock trees (at least 5 inches d.b.h.), in trees, on forest land'
            dn = 'Area of forest land, in acres'
            ofprfix = 'TPA'
        print "Let's make some tables! Run: "+str(i)
        for state in states:
            st = state[1]
            #st = state
            of = 'out'+ofprfix+st+'.html'
            fetchTable(st, yr, nm, dn, pg, r, c, of)
        print 'DONE!'
        i += 1

if __name__ == '__main__':
    main()

def state_test():
    assert main
