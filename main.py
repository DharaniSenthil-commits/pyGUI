from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter import filedialog
import pandas as pd
from pandastable import Table
import csv

class app :
    def __init__(self, win):
        self.lbl1 = Label(win, text='INPUT FILE :')
        self.lbl1.place(x=50, y=50)
        self.t1 = Entry(win, width=15)
        self.t1.place(x=150, y=50)
        self.b1 = Button(win, text='Upload a file',command=self.browse)
        self.b1.place(x=250, y=45)
        self.lbl2 = Label(win, text='ROW COUNT :')
        self.lbl2.place(x=50, y=100)
        self.t2 = Entry(win, width=15)
        self.t2.place(x=150, y=100)
        self.lbl3 = Label(win, text='COLUMN COUNT :')
        self.lbl3.place(x=250, y=100)
        self.t3 = Entry(win,width=15)
        self.t3.place(x=360,y=100)
        self.lbl4 = Label(win, text='COLUMN NAME :')
        self.lbl4.place(x=50, y=300)
        self.lbl5 = Label(win, text='AGGREATION FUNCTION :')
        self.lbl5.place(x=50, y=350)
        v = IntVar()
        #cn=self.cb1=ComboBox
        self.r1 =Radiobutton(win,text="SUM",variable=v, value='SUM')
        self.r1.place(x=200,y=350)
        self.r2 = Radiobutton(win, text='MIN',variable=v,value='MIN')
        self.r2.place(x=200, y=370)
        self.r3 = Radiobutton(win, text='MAX',variable=v,value='MAX')
        self.r3.place(x=200, y=390)
        self.r4 = Radiobutton(win, text='NULL',variable=v,value='NULL')
        self.r4.place(x=200, y=410)
        self.r5 = Radiobutton(win, text='NOT NULL',variable=v,value='NOT NULL')
        self.r5.place(x=200, y=430)
        self.r6 = Radiobutton(win, text='COUNT',variable=v,value='COUNT')
        self.r6.place(x=200, y=450)
        self.cb1 = Combobox(win, width=15)
        self.cb1.place(x=150, y=300)
        self.lbl6 = Label(win, text='OUTPUT :')
        self.lbl6.place(x=50, y=480)
        self.t4 = Entry(win, width=20)
        self.t4.place(x=120, y=480)





    def browse(self):

            global filename
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("csv files","*.csv*"),("all files","*.*")))
            showinfo(title='Select a File', message="File Uploaded !")
            self.t1.insert(END, 'File Choosed')
            df = pd.read_csv(filename)
            rowcount = len(df.axes[0])
            colcount = len(df.axes[1])
            self.t2.insert(END, str(rowcount))
            self.t3.insert(END, str(colcount))

            df1 = pd.read_csv(filename)
            self.f1 = Frame(win, height=50, width=50)
            self.f1.pack(fill=BOTH, expand=1)
            self.f1.place(x=60, y=140)
            self.table = Table(self.f1, width=370, height=100, dataframe=df1, read_only=True)
            self.table.show()

            with open(filename) as csv :
                df = pd.read_csv(filename)
                cn = list(df.columns)
                print(cn[0])
                for i in range(len(cn)) :
                    cn[i] =(self.cb1.insert(END,str(cn[i])))  # add option

                print(cn)
               #foo.append(row)





if __name__ == "__main__":
    win=Tk()
    App = app(win)
    win.title('GUI Python')
    win.geometry("500x600")
    win.mainloop()