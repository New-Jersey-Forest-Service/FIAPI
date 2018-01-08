from bs4 import BeautifulSoup
import sys
import re
import csv
import urllib2
import numpy as np
import matplotlib.pyplot as plt

def cell_text(cell):
    return " ".join(cell.stripped_strings)
url ="http://apps.fs.fed.us/Evalidator/batcheval.jsp?reptype=State&lat=0&lon=-0&radius=0&snum=Area%20of%20forest%20land,%20in%20acres&sdenom=No%20denominator%20-%20just%20produce%20estimate.&wc=92015&pselected=None&rselected=Forest%20type%20group&cselected=Ownership%20group&ptime=Current&rtime=Current&ctime=Current&wf=&wnum=&wnumdenom="
html = urllib2.urlopen(url).read()
soup =BeautifulSoup(html, "html.parser")
output = csv.writer(sys.stdout)
tables=[]
tablecounter=0
for table in soup.find_all('table'):
   # title=table.find('caption')
    rowcounter=0
    title=table.b
    if(title != None):
        graph=[]
       # print(title.string.extract())
        for row in table.find_all('tr'):
            col = map(cell_text, row.find_all(re.compile('t[dh]')))
            for i in range(0,len(col)):
                if(col[i]=='-'):
                    col[i]=0
                else:
                    col[i]=col[i].encode('ascii')
                    col[i]=col[i].replace(',','')

            #print(col)
            graph.append(col)

        output.writerow([])
        tablecounter+=1
    tables.append(graph)

print(tables[0])
xcounter = 0
counter = 0
title = ''
num = [0, 1, 2, 3]
for col in tables[0]:
    if (counter == 0):
        title = col[1]
    elif (counter == 1):
        plt.xlabel(col[0])
    else:
        results = map(int, col[1:])
        plt.bar(num, results, label=col[0])
        #print(col[1:])

        num = [x + 10 for x in num]
    counter += 1

plt.show()


