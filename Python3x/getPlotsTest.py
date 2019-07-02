from PyEVALIDator import fetchPlots
from EVALIDatorVars import *
from SpatialJoin import *
from DeletePrevious import*

def main():
    deleteoldfiles()
    ev = EVALIDatorVars()
    print ("Let's query some FIA plots!")
    state = input('Input a state: ')
    state = state.upper()
    sc = ev.stateDict[state]
    yrs = []
    stop = False
    while stop == False:
        year = input('Input a year (if no more years, enter x): ')
        if year == 'x':
            stop = True
        else:
            yrs.append(year)
    of ="reftable.csv"
    print ('Fetching plots!')
    fetchPlots(sc, yrs, of)
    print ('Plots fetched!')

    print('Plotting Points')
    Plotting_points()

    print('Doing Spatial Join')
    spatialjoin()
    print("Finished")

    
if __name__ == '__main__':
    main()

