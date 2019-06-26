from PyEVALIDator import fetchPlots
from EVALIDatorVars import *

def main():
    ev = EVALIDatorVars()
    print ("Let's query some FIA plots!")
    state = input('Input a state: ')
    sc = ev.stateDict[state]
    yrs = []
    stop = False
    while stop == False:
        year = input('Input a year (if no more years, enter x): ')
        if year == 'x':
            stop = True
        else:
            yrs.append(year)
    of = input('Input an output filename .csv: ')
    print ('Fetching plots!')
    fetchPlots(sc, yrs, of)
    print ('Plots fetched!')
if __name__ == '__main__':
    main()
