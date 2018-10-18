# EVALIDatorGUI.py
# V 1.0
# NJ Forest Service, 10/2018
# Python 2.7

from tkinter import *
from PyEVALIDator import fetchTable
from EVALIDatorVars import *

fields = ['State', 'Year', 'Numerator', 'Denominator', 'Page', 'Row', 'Column', 'Lat', 'Long', 'Radius']
ev = EVALIDatorVars()
entries = []


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

    print(entries)
   
  return entries

# def getData():

#   print("you entered")
#   print(entries.get())
  # fetchTable(st, yr, nm, dn, pg, r, c, of, ot, lat = 0, lon =0, rad =0)


def main():

  root = Tk()
  ents = makeForm(root, fields)
  root.bind('<Return>', (lambda event, e=ents: fetch(e)))


  # #define inputs for fetchTable
  # states = ''
  # st = ''
  # yr = ''
  # nm = ev.nmDict[root.bind('<Return>', (lambda event, e=ents: fetch(e)))]
  # dn = ev.nmDict[root.bind('<Return>', (lambda event, e=ents: fetch(e)))]
  # pg = 'None'
  # r = ev.nmDict[root.bind('<Return>', (lambda event, e=ents: fetch(e)))]
  # c = ev.nmDict[root.bind('<Return>', (lambda event, e=ents: fetch(e)))]
  # of = ''
  # ot = 'JSON'

  # print("Let's make some tables!")

  # for state in states:
  #     st = ev.stateDict[state]
  #     of = 'output'+st+'.json' 
  #     fetchTable(st, yr, nm, dn, pg, r, c, of, ot, 0, 0, 0)

  # print('DONE!')

if __name__ == '__main__':
  # main()
  root = Tk()
  ents = makeForm(root, fields)
  root.bind('<Return>', (lambda event, e=ents: fetchFields(e)))

  b1 = Button(root, text='Get Data',
         command=(lambda e=ents: fetchFields   (e)))
  b1.pack(side=LEFT, padx=5, pady=5)

  b2 = Button(root, text='Quit', command=root.quit)
  b2.pack(side=LEFT, padx=5, pady=5)

  # fetch_data = Button(root, text="Retrieve", command=main)
  # fetch_data.pack()
  root.mainloop()