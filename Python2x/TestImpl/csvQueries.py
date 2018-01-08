import Tkinter
import tkMessageBox
import tkFileDialog
import csv
import Python2x.PyEVALIDator

class GUITest04Class(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.entry = Tkinter.Entry(self)
        self.geometry("450x300")

        def infile():
            inf = tkFileDialog.askopenfilenames()
            if inf == '':
                tkMessageBox.showwarning("Filename", "No file selected!")
            #else:
                #tkMessageBox.showinfo("Filename", inf)
            global filename
            filename = inf
            app.quit()
            #return inf

        def hello():
            tkMessageBox.showinfo("Say Hello", "Hello World")

        flist = ['']
        l1 = Tkinter.Label(self, text='Hello App')
        b1 = Tkinter.Button(self, text="Say Hello", command=hello)
        b2 = Tkinter.Button(self, text="Open File", command=infile)
        l1.pack()
        b1.pack()
        b2.pack()
        if flist[0] != '':
            print flist[0]


filename = ''
global app
app = GUITest04Class(None)

if __name__ == '__main__':
    app.title('Test GUI')
    app.mainloop()
    print(filename[0])
    with open(filename[0],'rb') as csvfile:
        queries = csv.reader(csvfile)
        counter =0
        for val in queries:#this puts one csv line into val
            Python2x.PyEVALIDator.fetchTable(val[0], val[1], val[2], val[3], val[4], val[5], val[6], "output" + str(counter) + ".html")
            counter +=1
