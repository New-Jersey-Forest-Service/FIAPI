from Python2x.PyEVALIDator import fetchTable
import csv

def main():


    st = '55'
    yr = '2015'
    nm = 'Area of timberland, in acres'
    dn = 'No denominator - just produce estimate.'
    pg = 'None'
    r = 'Stand-size class'
    c = 'Ownership group'
    ofprfix = 'FArea'
    of = 'out' + ofprfix + st + '.html'

    fetchTable(st, yr, nm, dn, pg, r, c, of,45,-93,50)
    print 'DONE!'

if __name__ == '__main__':
    main()
