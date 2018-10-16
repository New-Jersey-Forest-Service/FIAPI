# EVALIDatorGUI.py
# V 1.0
# NJ Forest Service, 10/2018
# Python 2.7

from tkinter import *
from PyEVALIDator import fetchTable
from EVALIDatorVars import *

fields = 'State', 'Year', 'Numerator', 'Denominator', 'Page', 'Row', 'Column', 'Lat', 'Long', 'Radius'

def fetch_fields(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def make_form(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

def get_data():
 
    state = ev.stateDict[text[0]] + ev.get()
    year = text[1]
    num = ev.nmDict[text[2]] + ev.get()
    den = ev.dmDict[text[3]] + ev.get()
    page = text[4]
    row = ev.rowDicttext[text[5]] + ev.get()
    col = ev.colDicttext[text[6]] + ev.get()
    lat = text[7]
    lon = text[8]
    rad = text[9]
 
    lbl.configure(text= res)

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))

   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)

   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()