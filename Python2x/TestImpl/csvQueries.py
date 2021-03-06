import re
import sys
from matplotlib import pyplot as plt

import Tkinter
import tkMessageBox
import tkFileDialog
import csv
import Python2x.PyEVALIDator
from bs4 import BeautifulSoup
import matplotlib
matplotlib.use("TkAgg")


def cell_text(cell):
    return " ".join(cell.stripped_strings)


class FirstPage(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.entry = Tkinter.Entry(self)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.geometry("450x300")

        def stateQueries():
            inf = tkFileDialog.askopenfilenames()
            if inf == '':
                tkMessageBox.showwarning("Filename", "No file selected!")
            else:
                filename = inf
#                dir=tkFileDialog.askdirectory()
                with open(filename[0], 'rb') as csvfile:
                    queries = csv.reader(csvfile)
                    counter = 0
                    for val in queries:  # this puts one csv line into val
                        Python2x.PyEVALIDator.fetchTable(val[0], val[1], val[2], val[3], val[4], val[5], val[6],
                                                         "output" + str(counter) + ".html")
                        counter += 1

        def htmlToBargraph():
            inf = tkFileDialog.askopenfilenames()
            if inf == '':
                tkMessageBox.showwarning("Filename", "No file selected!")
            else:
                filename = inf
                for file in filename:
                    soup = BeautifulSoup(open(file), "html.parser")
                    output = csv.writer(sys.stdout)
                    tables = []
                    tablecounter = 0
                    for table in soup.find_all('table'):
                        title = table.b
                        if (title != None):
                            graph = []
                            tmptitle = []
                            tmptitle.append(title.string.extract())
                            graph.append(tmptitle)
                            for row in table.find_all('tr'):
                                col = map(cell_text, row.find_all(re.compile('t[dh]')))
                                for i in range(0, len(col)):
                                    if (col[i] == '-'):
                                        col[i] = 0
                                    else:
                                        col[i] = col[i].encode('ascii')
                                        col[i] = col[i].replace(',', '')

                                graph.append(col)

                            output.writerow([])
                            tablecounter += 1
                            tables.append(graph)

                    graphstuff = []
                    for table in tables:
                        # print table
                        xcounter = 0
                        counter = 0
                        labels = []
                        barLabels = []
                        barLabelPos = []
                        graphstuff.append(plt.figure())
                        tmp = graphstuff[len(graphstuff) - 1].add_subplot(1, 1, 1)
                        for col in table:
                            if (counter == 0):
                                tmp.set_title(col[0])

                            elif (counter == 1):
                                tmp.set_xlabel(col[0])
                            elif (counter == 2):
                                labels = col
                                # plt.xlabel(col[0])
                            else:
                                barLabels.append(col[0])
                                results = map(float, col[1:])
                                num = []
                                for i in range(xcounter, xcounter + len(col[1:])):
                                    num.append(i)
                                barLabelPos.append(xcounter)
                                rects = tmp.bar(num, results)
                                for rect in rects:
                                    height = rect.get_height()
                                    tmp.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                                             '%d' % int(height),
                                             ha='center', va='bottom', fontsize=5)
                                xcounter += 10
                            counter += 1
                        tmp.set_xticks(barLabelPos)
                        # print(barLabels)
                        # tmp.set_xticklabels(barLabels)
                        #print(barLabels)

                    # Get current size
                    plt.rcParams['figure.figsize'] = (20, 20)
                    plt.show()

        def latLonQueries():
            inf = tkFileDialog.askopenfilenames()
            if inf == '':
                tkMessageBox.showwarning("Filename", "No file selected!")
            else:
                # tkMessageBox.showinfo("Filename", inf)
                filename = inf
                for file in filename:
                    with open(file, 'rb') as csvfile:
                        queries = csv.reader(csvfile)
                        counter = 0
                        for val in queries:  # this puts one csv line into val   st, yr, nm, dn, pg, r, c, of,45,-93,50
                            Python2x.PyEVALIDator.fetchTable(val[0], val[1], val[2], val[3], val[4], val[5], val[6], 'latlonoutput' + str(counter) + '.html', val[7], val[8], val[9])
                            counter += 1
                        print("donezo")

        flist = ['']
        b1 = Tkinter.Button(self, text="Html to Bargraph", command=htmlToBargraph)
        b2 = Tkinter.Button(self, text="State Queries", command=stateQueries)
        b3 = Tkinter.Button(self, text="Lat Lon Queries", command=latLonQueries)
        b1.place(x=150, y=140)
        b2.place(x=160, y=80)
        b3.place(x=155, y=200)
        if flist[0] != '':
            print(flist[0])


if __name__ == '__main__':
    app = FirstPage(None)
    app.title('PyEvalidator')
    app.mainloop()
