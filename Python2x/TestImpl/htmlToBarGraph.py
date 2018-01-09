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
        tmptitle=[]
        tmptitle.append(title.string.extract())
        graph.append(tmptitle)
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


graphstuff=[]
for table in tables:
   # print table
    xcounter = 0
    counter = 0
    labels=[]
    barLabels=[]
    barLabelPos=[]
    graphstuff.append(plt.figure())
    tmp = graphstuff[len(graphstuff) - 1].add_subplot(1, 1, 1)
    for col in table:
        if (counter == 0):
            tmp.set_title(col[0])

        elif (counter == 1):
            tmp.set_xlabel(col[0])
        elif(counter ==2):
            labels=col
           # plt.xlabel(col[0])
        else:
            barLabels.append(col[0])
            results = map(float, col[1:])
            num=[]
            for i in range(xcounter,xcounter+len(col[1:])):
                num.append(i)
            barLabelPos.append(xcounter)
            rects=tmp.bar(num, results)
            for rect in rects:
                height = rect.get_height()
                tmp.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%d' % int(height),
                        ha='center', va='bottom',fontsize=5)
            xcounter+=10
        counter += 1
    tmp.set_xticks(barLabelPos)
    #print(barLabels)
    #tmp.set_xticklabels(barLabels)
    print(barLabels)

# Get current size
plt.rcParams['figure.figsize']=(20,20)
plt.show()


