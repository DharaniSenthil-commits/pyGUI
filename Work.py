import os.path
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
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
        self.lbl4.place(x=50, y=150)
        self.lbl5 = Label(win, text='SPLIT PERCENTAGE(%) :')
        self.lbl5.place(x=50, y=190)
        cn1=self.cb2 = Combobox(win, width=10, state="readonly")
        self.cb2.place(x=200, y=190)
        cn1['values'] = (100,50,25)
        self.b2 = Button(win, text='Show',command=self.output)
        self.b2.place(x=300, y=185)
        self.lbl_size = Label(win, text='FILE SIZE :')
        self.lbl_size.place(x=350, y=50)
        self.t_size = Entry(win,width=15)
        self.t_size.place(x=410,y=50)
        self.f4 = LabelFrame(win, text='File_Data')
        self.f4.pack(fill=BOTH, expand=1)
        self.f4.place(x=550, y=40, height=200, width=400)

    def output(self):
        if self.cb2.get() == '100':
            input_percent = self.cb2.get()
            data = pd.read_csv(filename)
            size = int(float(rowcount) * float(float(input_percent) / 100))
            n = int(100 / int(input_percent))
            for i in range(n):
                df = data[size * i:size * (i + 1)]
                df.to_csv(f'SplitFile_{i + 1}.csv', index=False)
            showinfo(title='Information', message="File Splited Succuessfully !")
            self.f1 = LabelFrame(win, text='OUTPUT_100%')
            self.f1.pack(fill=BOTH, expand=1)
            self.f1.place(x=50, y=250, height=220, width=350)
            self.lbl6 = Label(self.f1, text='AGGREGATION FUNCTION :')
            self.lbl6.place(relx=0.1,rely=0.1)
            cn2 = self.cb3 = Combobox(self.f1, width=15, state="readonly")
            self.cb3.place(relx=0.55,rely=0.1)
            cn2['values'] = ('SUM','MIN','MAX','COUNT','NULL','NOT NULL')
            self.lbl7 = Label(self.f1,text='OUTPUT :')
            self.lbl7.place(relx=0.1,rely=0.5)
            self.t4 = Entry(self.f1, width=15)
            self.t4.place(relx=0.3,rely=0.5)
            self.b_show = Button(self.f1,text="GET",command=self.result)
            self.b_show.place(relx=0.6,rely=0.45)
        elif self.cb2.get() =='50':
            input_percent = self.cb2.get()
            data = pd.read_csv(filename)
            size = int(float(rowcount) * float(float(input_percent) / 100))
            n = int(100 / int(input_percent))
            for i in range(n):
                df = data[size * i:size * (i + 1)]
                df.to_csv(f'SplitFile_{i + 1}.csv', index=False)
            showinfo(title='Information', message="File Splited Succuessfully !")
            self.f2 = LabelFrame(win, text='OUTPUT_50%')
            self.f2.pack(fill=BOTH, expand=1)
            self.f2.place(x=50, y=250, height=220, width=350)
            self.lbl6 = Label(self.f2, text='AGGREGATION FUNCTION :')
            self.lbl6.place(relx=0.1, rely=0.1)
            cn2 = self.cb3 = Combobox(self.f2, width=15, state="readonly")
            self.cb3.place(relx=0.55, rely=0.1)
            cn2['values'] = ('SUM', 'MIN', 'MAX', 'COUNT', 'NULL', 'NOT NULL')
            self.lbl7 = Label(self.f2, text='OUTPUT_FILE_1 :')
            self.lbl7.place(relx=0.1, rely=0.5)
            self.t4 = Entry(self.f2, width=15)
            self.t4.place(relx=0.40, rely=0.5)
            self.lbl8 = Label(self.f2, text='OUTPUT_FILE_2 :')
            self.lbl8.place(relx=0.1, rely=0.7)
            self.t5 = Entry(self.f2, width=15)
            self.t5.place(relx=0.40, rely=0.7)

        else:
            input_percent = self.cb2.get()
            data = pd.read_csv(filename)
            size = int(float(rowcount) * float(float(input_percent) / 100))
            n = int(100 / int(input_percent))
            for i in range(n):
                df = data[size * i:size * (i + 1)]
                df.to_csv(f'SplitFile_{i + 1}.csv', index=False)
            showinfo(title='Information', message="File Splited Succuessfully !")
            self.f3 = LabelFrame(win, text='OUTPUT_25%')
            self.f3.pack(fill=BOTH, expand=1)
            self.f3.place(x=50, y=250, height=220, width=350)
            self.lbl6 = Label(self.f3, text='AGGREGATION FUNCTION :')
            self.lbl6.place(relx=0.1, rely=0.1)
            cn2 = self.cb3 = Combobox(self.f3, width=15, state="readonly")
            self.cb3.place(relx=0.55, rely=0.1)
            cn2['values'] = ('SUM', 'MIN', 'MAX', 'COUNT', 'NULL', 'NOT NULL')
            self.lbl7 = Label(self.f3, text='OUTPUT_FILE_1 :')
            self.lbl7.place(relx=0.1, rely=0.3)
            self.t4 = Entry(self.f3, width=15)
            self.t4.place(relx=0.40, rely=0.3)
            self.lbl8 = Label(self.f3, text='OUTPUT_FILE_2 :')
            self.lbl8.place(relx=0.1, rely=0.4)
            self.t5 = Entry(self.f3, width=15)
            self.t5.place(relx=0.40, rely=0.4)
            self.lbl7 = Label(self.f3, text='OUTPUT_FILE_3 :')
            self.lbl7.place(relx=0.1, rely=0.5)
            self.t4 = Entry(self.f3, width=15)
            self.t4.place(relx=0.40, rely=0.5)
            self.lbl8 = Label(self.f3, text='OUTPUT_FILE_4 :')
            self.lbl8.place(relx=0.1, rely=0.6)
            self.t5 = Entry(self.f3, width=15)
            self.t5.place(relx=0.40, rely=0.6)

    def browse(self):
        global filename, headers,rowcount
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("csv files","*.csv*"),("all files","*.*")))
        if filename == '':
            showwarning(title='Warning', message='Select a File first')
        else:
            showinfo(title='Information', message="File Uploaded !")
            self.t1.delete(0, END)
            self.t1.insert(END, 'File Choosed')
            df = pd.read_csv(filename)
            rowcount = len(df.axes[0])
            colcount = len(df.axes[1])
            self.t2.delete(0, END)
            self.t2.insert(END, str(rowcount))
            self.t3.delete(0, END)
            self.t3.insert(END, str(colcount))

            filesize = os.path.getsize(filename)
            size = int(filesize / 1024)
            self.t_size.delete(0, END)
            self.t_size.insert(END,str(size)+'KB')

            cn = self.cb1 = Combobox(win, width=15, state="readonly")
            self.cb1.place(x=150, y=150)
            with open(filename, 'r') as f:
                d_reader = csv.DictReader(f)
                headers = d_reader.fieldnames
            cn['values'] = headers

            df1 = pd.read_csv(filename)
            self.table = Table(self.f4, dataframe=df1, read_only=True)
            self.table.show()


    def download(self):

        input_percent = self.cb2.get()
        data = pd.read_csv(filename)
        size = int(float(rowcount) * float(float(input_percent) / 100))
        n = int(100 / int(input_percent))
        for i in range(n):
            df = data[size * i:size * (i + 1)]
            df.to_csv(f'SplitFile_{i + 1}.csv', index=False)
        showinfo(title='Information', message="File Splited Succuessfully !")
        self.msg = Label(win,text="File Splited Succuessfully..!")
        self.msg.place(relx=0.2, rely=0.7)

    def result(self):
        temp = self.cb3.get()
        agg = pd.read_csv(filename)
        if temp == 'MIN':
            min = agg[self.cb1.get()].min()
            self.t4.delete(0, END)
            self.t4.insert(END, str(min))
        elif temp == 'SUM':
            sum = agg[self.cb1.get()].sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(sum))
        elif temp == 'MAX':
            max = agg[self.cb1.get()].max()
            self.t4.delete(0, END)
            self.t4.insert(END, str(max))
        elif temp == 'COUNT':
            count = agg[self.cb1.get()].count()
            self.t4.delete(0, END)
            self.t4.insert(END, str(count))
        elif temp == 'NULL':
            null = agg[self.cb1.get()].isnull().sum().sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(null))
        else:
            nnull = agg[self.cb1.get()].notnull().sum().sum()
            self.t4.delete(0, END)
            self.t4.insert(END, str(nnull))



if __name__ == "__main__":
    win=Tk()
    App = app(win)
    win.title('GUI Python')
    win.geometry("1000x600")
    win.mainloop()
