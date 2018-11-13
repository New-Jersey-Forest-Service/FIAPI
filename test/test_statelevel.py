#approx port of FiaTestRun08.py for CI; stripped out read csv to remove deps
# test for ?

import unittest
import pytest

from Python2x.PyEVALIDator import *
import csv 
from Python2x.EVALIDatorVars import *

"""
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

"""

ev = EVALIDatorVars()
st = '34'
yr = '2015'
nm = 'Area of timberland, in acres'
dn = ev.dmDict['nodenominator']
pg = 'None'
r = 'Stand age 10 yr classes'
c = 'Reserved status class'
of = ''
ot = 'JSON'
of = 'TESTINGoutput'+st+'.txt' 
t1=fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)
#print t1
print t1.status_code
print t1.encoding
print t1.raise_for_status()
#print t1.json()
#print type(t1.json)
#print type(t1)
#print t1.status_code == 200

#https://www.reddit.com/r/learnprogramming/comments/30kbfy/how_are_api_wrapper_unit_tests_written/
#Class def 
def test_httpcode():
    ev = EVALIDatorVars()
    st = '34'
    yr = '2015'
    nm = 'Area of timberland, in acres'
    dn = ev.dmDict['nodenominator']
    pg = 'None'
    r = 'Stand age 10 yr classes'
    c = 'Reserved status class'
    of = ''
    ot = 'JSON'
    of = 'TESTINGoutput'+st+'.txt' 
    t1=fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)

    assert t1.status_code == 200

test_httpcode()