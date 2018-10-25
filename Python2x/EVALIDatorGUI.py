# EVALIDatorGUI.py
# V 1.0
# NJ Forest Service, 10/2018
# Python 2.7

import pandas as pd
from tkinter import *
from PyEVALIDator import fetchTable
from EVALIDatorVars import *

## TODO: input an excel file with parameters and then hit fetchtable()

## TODO: make fields a dictionary?? 
fields = ['State', 'Year', 'Numerator', 'Denominator', 'Page', 'Row', 'Column', 'Lat', 'Long', 'Radius']
ev = EVALIDatorVars()
entries = []

def excelData(filename):
  excel_file = pd.read_csv(filename)
  

def fetchFields(entries):
  for entry in entries:
    field = entry[0]
    text  = entry[1].get()
    print('%s: "%s"' % (field, text)) 

def makeForm(root, fields):

  for field in fields:
    row = Frame(root)
    lab = Label(row, width=15, text=field, anchor='w')
    ent = Entry(row)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    entries = ent.pack(side=RIGHT, expand=YES, fill=X)
    # entries.append((field, ent))
    # print(fields)
   
  return entries

def main():
    states = fields.get(entries)
    st = ''
    yr = fields.get(entries)
    nm = ev.nmDict[fields.get(entries)]
    dn = ev.dmDict[fields.get(entries)]
    pg = 'None'
    r = ev.rowDict[fields.get(entries)]
    c = ev.colDict[fields.get(entries)]
    of = ''
    ot = 'JSON'

    print("Let's make some tables!")
    for state in states:
        st = ev.stateDict[state]
        of = 'output'+st+'.json' 
        fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)
    print('DONE!')


if __name__ == '__main__':
  root = Tk()
  ents = makeForm(root, fields)
  root.bind('<Return>', (lambda event, e=ents: fetchFields(e)))
  root.bind('<Return>', (lambda eff: main()))

  b1 = Button(root, text='Get Data',
         command=(lambda:main()))
  b1.pack(side=LEFT, padx=5, pady=5)

  b2 = Button(root, text='Quit', command=root.quit)
  b2.pack(side=LEFT, padx=5, pady=5)

  root.mainloop()