import pandas as pd
percentage = int(input("enter the percentage"))
rowcount=999
df = pd.read_csv("test_file.txt", sep="|")
if percentage == 25 :
    rs1=0
    re1= int(int(rowcount)/4)

    rs2= re1
    re2= re1 + re1

    rs3 = re2
    re3 = re1 + re2

    rs4 = re3
    re4 = rowcount
    file1=df.iloc[rs1:re1]
    print(file1)
    print(file1['count'].max())
    file2 = df.iloc[rs2:re2]
    print(file2)
    print(file2['count'].max())
    file3 = df.iloc[rs3:re3]
    print(file3)
    print(file3['count'].max())
    file4 = df.iloc[rs4:re4]
    print(file4)
    print(file4['count'].max())


else :
    rs1 = 0
    re1 = int(int(rowcount) / 2)

    rs2 = re1
    re2 = rowcount

    file1 = df.iloc[rs1:re1]
    print(file1)
    print(file1['count'].max())
    file2 = df.iloc[rs2:re2]
    print(file2)
    print(file2['count'].max())



'''100 row

25 ==> 4 files


file1 going to 1 tp 25
file2 going to 26 to 50

file =1000 row

50 % ---> 500 + 500 rows

rowcount = len(df.axes[0]) = 1000

2
 1 : 1
 rs1=1
 re1=rowcount/2
 rs2 = (rowcount/2)+1
 re2=rowcount


 1 : 1000 r /2  ; (1000 r/2) +1 : 1000

 1: 500 ; 501 :1000





25 % ---> 250 + 250 + 250 rows

rs1=1
re1=rowcount/4 = 250

rs2= re1+1
re2= re1 + re1

rs3 = re2 + 1
re3 = re1 + re2

rs4 = re3 + 1
re4 = rowcount







f1_rc1 = 1 to 250 = len(f1_rc1)
f2_rc1= 251 to 500 = len(f1_rc1) : len(f2_)
f3_rc1= 501 to 750 = len(f1_rc1) : len(f2_)
f4_rc1= 751 to 1000 = len(f1_rc1) : len(file)



'''