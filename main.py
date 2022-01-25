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
        self.r1 =Radiobutton(win,text="SUM",variable=v, value='SUM',command=self.aggregate1)
        self.r1.place(x=200,y=350)
        self.r2 = Radiobutton(win, text='MIN',variable=v,value='MIN',command=self.aggregate2)
        self.r2.place(x=200, y=370)
        self.r3 = Radiobutton(win, text='MAX',variable=v,value='MAX',command=self.aggregate3)
        self.r3.place(x=200, y=390)
        self.r4 = Radiobutton(win, text='NULL',variable=v,value='NULL',command=self.aggregate4)
        self.r4.place(x=200, y=410)
        self.r5 = Radiobutton(win, text='NOT NULL',variable=v,value='NOT NULL',command=self.aggregate5)
        self.r5.place(x=200, y=430)
        self.r6 = Radiobutton(win, text='COUNT',variable=v,value='COUNT',command=self.aggregate6)
        self.r6.place(x=200, y=450)
        self.lbl6 = Label(win, text='OUTPUT :')
        self.lbl6.place(x=50, y=480)
        self.t4 = Entry(win, width=20)
        self.t4.place(x=120, y=480)



    def aggregate1(self):
        temp=self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            sum = agg[self.cb1.get()].sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(sum))
        else:
            showinfo(title='Error message', message="Upload a file first!")

    def aggregate2(self):
        temp = self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            min = agg[self.cb1.get()].min()
            self.t4.delete(0,END)
            self.t4.insert(END, str(min))
        else:
            showinfo(title='Error message', message="Upload a file first!")

    def aggregate3(self):
        temp = self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            max = agg[self.cb1.get()].max()
            self.t4.delete(0, END)
            self.t4.insert(END, str(max))

        else:
            showinfo(title='Error message', message="Upload a file first!")

    def aggregate4(self):
        temp = self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            null = agg[self.cb1.get()].isnull().sum().sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(null))

        else:
            showinfo(title='Error message', message="Upload a file first!")

    def aggregate5(self):
        temp = self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            nnull = agg[self.cb1.get()].notnull().sum().sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(nnull))
        else:
            showinfo(title='Error message', message="Upload a file first!")

    def aggregate6(self):
        temp = self.t1.get()
        if temp != '':
            agg = pd.read_csv(filename)
            count = agg[self.cb1.get()].count()
            self.t4.delete(0, END)
            self.t4.insert(END, str(count))
        else:
            showinfo(title='Error message', message="Upload a file first!")


    def browse(self):
        global filename, headers
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("csv files","*.csv*"),("all files","*.*")))
        showinfo(title='Select a File', message="File Uploaded !")
        self.t1.delete(0,END)
        self.t1.insert(END, 'File Choosed')
        #print(self.t1.get())
        df = pd.read_csv(filename)
        rowcount = len(df.axes[0])
        colcount = len(df.axes[1])
        self.t2.delete(0, END)
        self.t2.insert(END, str(rowcount))
        self.t3.delete(0, END)
        self.t3.insert(END, str(colcount))

        df1 = pd.read_csv(filename)
        self.f1 = Frame(win, height=100, width=100)
        self.f1.pack(fill=BOTH, expand=1)
        self.f1.place(x=10, y=150)
        self.table = Table(self.f1, width=370, height=100, dataframe=df1, read_only=True)
        self.table.show()

        cn = self.cb1 = Combobox(win, width=15)
        self.cb1.place(x=150, y=300)
        with open(filename,'r') as f:
            d_reader = csv.DictReader(f)
            headers = d_reader.fieldnames
        cn['values'] = headers


if __name__ == "__main__":
    win=Tk()
    App = app(win)
    win.title('GUI Python')
    win.geometry("500x600")
    win.mainloop()