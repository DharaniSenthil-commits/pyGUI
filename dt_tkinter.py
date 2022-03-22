import os.path
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.ttk import Combobox
from tkinter import filedialog
import pandas as pd
from pandastable import Table
import datatable as dt
import sys

filename = "test_file.txt"
#splt_percentage = 50
'''mem_limit = 500
temp_dir = ""

'''

delimiter = "|"
df = dt.fread(filename, sep=delimiter, na_strings=[''], quotechar="")
print(df)

class app :
    def __init__(self, win):

        self.b1 = Button(win, text='Get Data', width=10, command=self.browse)
        self.b1.place(x=10, y=10)


        self.lbl5 = Label(win, text='SPLIT PERCENTAGE(%) :')
        self.lbl5.place(x=50, y=50)
        n=tkinter.IntVar()
        cn1 = self.cb2 = Combobox(win, width=10, state="readonly",textvariable=n)
        self.cb2.place(x=180, y=50)
        cn1['values'] = (100, 50, 25)
        #self.cb2.bind(self.browse)

        '''self.lbl1 = Label(win, text='INPUT FILE:')
        self.lbl1.place(x=50, y=190)
        self.t_msg = Entry(win, width=15)
        self.t_msg.place(x=150, y=190)'''

        self.lbl2 = Label(win, text='ROW COUNT :')
        self.lbl2.place(x=50, y=100)
        self.t_rc = Entry(win, width=15)
        self.t_rc.place(x=150, y=100)
        self.lbl3 = Label(win, text='COLUMN COUNT :')
        self.lbl3.place(x=250, y=100)
        self.t_cc = Entry(win,width=15)
        self.t_cc.place(x=360,y=100)
        self.lbl4 = Label(win, text='COLUMN NAME :')
        self.lbl4.place(x=50, y=150)

        self.b2 = Button(win, text='Show',command=self.output)
        self.b2.place(x=280, y=50)
        #self.lbl6.bind("U have clicked", self.output)

        self.lbl_size = Label(win, text='FILE SIZE :')
        self.lbl_size.place(x=350, y=50)
        self.t_size = Entry(win,width=15)
        self.t_size.place(x=410,y=50)
        self.f4 = LabelFrame(win, text='File_Data')
        self.f4.pack(fill=BOTH, expand=1)
        self.f4.place(x=550, y=40, height=200, width=400)


    def output(self):
        global file1, file2, file3, file4
        self.lbl_split = Label(win, text='Splited File :')
        self.lbl_split.place(x=550, y=300)
        cn4 = self.cb4 = Combobox(win, width=10, state="readonly")
        self.cb4.place(x=630, y=300)
        self.b_view = Button(win, text='View',command=self.View_data)
        self.b_view.place(x=730, y=300)
        self.f_viewdata = LabelFrame(win, text='View_Data')
        self.f_viewdata.pack(fill=BOTH, expand=1)
        self.f_viewdata.place(x=550, y=350, height=200, width=400)
        #n=self.var.get()
        if self.cb2.get() == '100':
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
            self.t1 = Entry(self.f1, width=15)
            self.t1.place(relx=0.3,rely=0.5)
            self.b_show = Button(self.f1,text="GET",width=10,command=self.result_100)
            self.b_show.place(relx=0.6,rely=0.3)
            cn4['values'] = ('file')

        elif self.cb2.get() =='50':
            df = pd.read_csv(filename, sep="|")
            rs1 = 0
            re1 = int(int(rowcount) / 2)
            rs2 = re1
            re2 = rowcount
            file1 = df.iloc[rs1:re1]
            file2 = df.iloc[rs2:re2]
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
            self.t2 = Entry(self.f2, width=15)
            self.t2.place(relx=0.40, rely=0.5)
            self.lbl8 = Label(self.f2, text='OUTPUT_FILE_2 :')
            self.lbl8.place(relx=0.1, rely=0.7)
            self.t3 = Entry(self.f2, width=15)
            self.t3.place(relx=0.40, rely=0.7)
            self.b_show = Button(self.f2, text="GET",width=10, command=self.result_50)
            self.b_show.place(relx=0.6, rely=0.3)
            cn4['values'] = ('file1', 'file2')

        else:
            df = pd.read_csv(filename, sep="|")
            rs1 = 0
            re1 = int(int(rowcount) / 4)
            rs2 = re1
            re2 = re1 + re1
            rs3 = re2
            re3 = re1 + re2
            rs4 = re3
            re4 = rowcount
            file1 = df.iloc[rs1:re1]
            file2 = df.iloc[rs2:re2]
            file3 = df.iloc[rs3:re3]
            file4 = df.iloc[rs4:re4]
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
            self.t2 = Entry(self.f3, width=15)
            self.t2.place(relx=0.45, rely=0.3)
            self.lbl8 = Label(self.f3, text='OUTPUT_FILE_2 :')
            self.lbl8.place(relx=0.1, rely=0.45)
            self.t3 = Entry(self.f3, width=15)
            self.t3.place(relx=0.45, rely=0.45)
            self.lbl7 = Label(self.f3, text='OUTPUT_FILE_3 :')
            self.lbl7.place(relx=0.1, rely=0.60)
            self.t4 = Entry(self.f3, width=15)
            self.t4.place(relx=0.45, rely=0.60)
            self.lbl8 = Label(self.f3, text='OUTPUT_FILE_4 :')
            self.lbl8.place(relx=0.1, rely=0.75)
            self.t5 = Entry(self.f3, width=15)
            self.t5.place(relx=0.45, rely=0.75)
            self.b_show = Button(self.f3, text="GET",width=5, command=self.result_25)
            self.b_show.place(relx=0.8, rely=0.3)
            cn4['values'] = ('file1', 'file2', 'file3', 'file4')

    def browse(self):
        global filename, headers,rowcount,df

        filepath = os.path.abspath(filename)
        self.lbl1 = Label(win, text="FilePath:  "+filepath)
        self.lbl1.place(x=100, y=10)

        '''self.t_msg.delete(0, END)
        self.t_msg.insert(END, 'File Choosed')'''
        df = pd.read_csv(filename,sep="|")
        rowcount = len(df.axes[0])
        colcount = len(df.axes[1])
        self.t_rc.delete(0, END)
        self.t_rc.insert(END, str(rowcount))
        self.t_cc.delete(0, END)
        self.t_cc.insert(END, str(colcount))

        filesize = os.path.getsize(filename)
        size = int(filesize / 1024)
        self.t_size.delete(0, END)
        self.t_size.insert(END, str(size) + 'KB')

        self.table = Table(self.f4, dataframe=df, read_only=True)
        self.table.show()

        cn = self.cb1 = Combobox(win, width=15, state="readonly")
        self.cb1.place(x=150, y=150)

        file_CN = pd.read_csv(filename, delimiter='|')
        columns = list(file_CN.head(0))
        cn['values'] = columns

    def result_100(self):
        agg = pd.read_csv(filename,sep="|")
        temp = self.cb3.get()
        if temp == 'MIN':
            min  = agg[self.cb1.get()].min()
            self.t1.delete(0, END)
            self.t1.insert(END, str(min))
        elif temp == 'SUM':
            sum = agg[self.cb1.get()].sum()
            self.t1.delete(0, END)
            self.t1.insert(END, str(sum))
        elif temp == 'MAX':
            max = agg[self.cb1.get()].max()
            self.t1.delete(0, END)
            self.t1.insert(END, str(max))
        elif temp == 'COUNT':
            count = agg[self.cb1.get()].count()
            self.t1.delete(0, END)
            self.t1.insert(END, str(count))
        elif temp == 'NULL':
            null = agg[self.cb1.get()].isnull().sum().sum()
            self.t1.delete(0, END)
            self.t1.insert(END, str(null))
        else:
            nnull = agg[self.cb1.get()].notnull().sum().sum()
            self.t1.delete(0, END)
            self.t1.insert(END, str(nnull))

    def result_50(self):
        temp = self.cb3.get()
        if temp == 'MIN':
            min1 = file1[self.cb1.get()].min()
            min2 = file2[self.cb1.get()].min()
            self.t2.delete(0, END)
            self.t2.insert(END, str(min1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(min2))
        elif temp == 'SUM':
            sum1 = file1[self.cb1.get()].sum()
            sum2 = file1[self.cb1.get()].sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(sum1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(sum2))
        elif temp == 'MAX':
            max1 = file1[self.cb1.get()].max()
            max2 = file2[self.cb1.get()].max()
            self.t2.delete(0, END)
            self.t2.insert(END, str(max1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(max2))
        elif temp == 'COUNT':
            count1 = file1[self.cb1.get()].count()
            count2 = file2[self.cb1.get()].count()
            self.t2.delete(0, END)
            self.t2.insert(END, str(count1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(count2))
        elif temp == 'NULL':
            null1 = file1[self.cb1.get()].isnull().sum().sum()
            null2 = file2[self.cb1.get()].isnull().sum().sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(null1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(null2))
        else:
            nnull1 = file1[self.cb1.get()].notnull().sum().sum()
            nnull2 = file2[self.cb1.get()].notnull().sum().sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(nnull1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(nnull2))

    def result_25(self):
        temp = self.cb3.get()
        if temp == 'MIN':
            min1 = file1[self.cb1.get()].min()
            min2 = file2[self.cb1.get()].min()
            min3 = file3[self.cb1.get()].min()
            min4 = file4[self.cb1.get()].min()
            self.t2.delete(0, END)
            self.t2.insert(END, str(min1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(min2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(min3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(min4))
        elif temp == 'SUM':
            sum1 = file1[self.cb1.get()].sum()
            sum2 = file1[self.cb1.get()].sum()
            sum3 = file2[self.cb1.get()].sum()
            sum4 = file3[self.cb1.get()].sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(sum1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(sum2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(sum3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(sum4))
        elif temp == 'MAX':
            max1 = file1[self.cb1.get()].max()
            max2 = file2[self.cb1.get()].max()
            max3 = file3[self.cb1.get()].max()
            max4 = file4[self.cb1.get()].max()
            self.t2.delete(0, END)
            self.t2.insert(END, str(max1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(max2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(max3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(max4))
        elif temp == 'COUNT':
            count1 = file1[self.cb1.get()].count()
            count2 = file2[self.cb1.get()].count()
            count3 = file3[self.cb1.get()].count()
            count4 = file4[self.cb1.get()].count()
            self.t2.delete(0, END)
            self.t2.insert(END, str(count1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(count2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(count3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(count4))
        elif temp == 'NULL':
            null1 = file1[self.cb1.get()].isnull().sum().sum()
            null2 = file2[self.cb1.get()].isnull().sum().sum()
            null3 = file3[self.cb1.get()].isnull().sum().sum()
            null4 = file4[self.cb1.get()].isnull().sum().sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(null1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(null2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(null3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(null4))
        else:
            nnull1 = file1[self.cb1.get()].notnull().sum().sum()
            nnull2 = file2[self.cb1.get()].notnull().sum().sum()
            nnull3 = file3[self.cb1.get()].notnull().sum().sum()
            nnull4 = file4[self.cb1.get()].notnull().sum().sum()
            self.t2.delete(0, END)
            self.t2.insert(END, str(nnull1))
            self.t3.delete(0, END)
            self.t3.insert(END, str(nnull2))
            self.t4.delete(0, END)
            self.t4.insert(END, str(nnull3))
            self.t5.delete(0, END)
            self.t5.insert(END, str(nnull4))

    def View_data(self):
        temp1 = self.cb4.get()
        temp2 = self.cb2.get()
        if temp1 == 'file':
            self.table = Table(self.f_viewdata, dataframe=df, read_only=True)
            self.table.show()
        elif temp2 == '50':
            if temp1 == 'file1':
                self.table = Table(self.f_viewdata, dataframe=file1, read_only=True)
                self.table.show()
            elif temp1 == 'file2':
                self.table = Table(self.f_viewdata, dataframe=file2, read_only=True)
                self.table.show()
        else:
            if temp1 == 'file1':
                self.table = Table(self.f_viewdata, dataframe=file1, read_only=True)
                self.table.show()
            elif temp1 == 'file2':
                self.table = Table(self.f_viewdata, dataframe=file2, read_only=True)
                self.table.show()
            elif temp1 == 'file3':
                self.table = Table(self.f_viewdata, dataframe=file3, read_only=True)
                self.table.show()
            elif temp1 == 'file4':
                self.table = Table(self.f_viewdata, dataframe=file4, read_only=True)
                self.table.show()


if __name__ == "__main__":
    win=Tk()
    App = app(win)
    win.title('GUI Python')
    win.geometry("1000x600")
    win.mainloop()