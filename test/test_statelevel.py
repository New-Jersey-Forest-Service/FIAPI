#approx port of FiaTestRun08.py for CI; stripped out read csv to remove deps
# test for ?

import unittest
import pytest

from Python2x.PyEVALIDator import *
import csv 
from Python2x.EVALIDatorVars import *

""" ev = EVALIDatorVars()
st = '34'
yr = '2015'
nm = 'Area of timberland, in acres'
dn = ev.dmDict['nodenominator']
pg = 'None'
r = 'Stand age 10 yr classes'
c = 'Reserved status class'
of = ''
otj = 'JSON'
#oth = 'HTML'
#otx = 'XML'
of = 'TESTINGoutput'+st+'.txt' 

t1=fetchTable(st, yr, nm, dn, pg, r, c, of, otj, 0, 0, 0)
#t2=fetchTable(st, yr, nm, dn, pg, r, c, of, oth, 0, 0, 0)
#t3=fetchTable(st, yr, nm, dn, pg, r, c, of, otx, 0, 0, 0) """



#https://www.reddit.com/r/learnprogramming/comments/30kbfy/how_are_api_wrapper_unit_tests_written/
class TestHTTPcodes():
    def test_httpcode(self):
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