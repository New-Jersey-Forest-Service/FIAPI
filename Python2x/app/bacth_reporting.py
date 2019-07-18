#This is an example using a csv file for inputs.
#This example was created for use as a demo at the FIA NRMT 2018.
import pandas as pd
from PyEVALIDator import fetchTable
from EVALIDatorVars import *

## Bring in data
def create_data(filename):
    ''' Bring in raw data file '''
    rdr = pd.read_excel(filename) 

    return rdr

def query_data(rdr):
    '''
    read inputs for fetchTable from inputFile.csv
    fetchTable(st, yr, nm, dn, pg, r, c, of, ot, lat, lon, rad)
    ----------[0,   1,  2   3,  4, 5, 6,  7,  8,   9,  10,  11]
    '''
    ev = EVALIDatorVars()
    firstLine = True
    n = 1
    #print("Let's get some data!")
    #read the rows of the input csv
    #skip the first row as headers
    for row in rdr:
        if firstLine == True:
            firstLine = False
        else:
            #assign and cast each input variable from csv
            print('Reading line '+str(n))
            st = ev.stateDict[row[0]]
            yr = str(row[1])
            nm = str(row[2])
            dn = str(row[3])
            pg = str(row[4])
            r = str(row[5])
            c = str(row[6])
            of = str(row[7])
            ot = str(row[8])
            lat = int(row[9])
            lon = int(row[10])
            rad = int(row[11])
            #go fetch!
            fetchTable(st,yr,nm,dn,pg,r,c,of,ot,lat,lon,rad)
            n+=1
    inFile.close()
    #print('DONE!')
    
    
    

## Dentist States 
def generate_tables(INPUT_FILENAME, OUTPUT_FILENAME):
    '''
    Method to generate the output for queryes data in csv to send to server.R
    INPUT_FILENAME -> The name of the input file 
    OUTPUT_FILENAME -> The name of the output file 
    '''
    ## Generate output for positive
    rdr = create_data(filename=INPUT_FILENAME)
    ## Queried data
    bacth_query_output = query_data(rdr)
    save_xlsx(bacth_query_output, OUTPUT_FILENAME)
    

