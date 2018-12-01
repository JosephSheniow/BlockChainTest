import tkinter as tk 
from tkinter import *
import os

#window
win=tk.Tk()
win.title("哲哲")
win.geometry("600x800")
win.configure(bg='gray20')


#Label
titleLabel=Label(win,text="請輸入以下Address",font=('微軟正黑體 bold',25),fg='steelblue2',bg='gray20')
titleLabel.place(x=300,y=80,anchor=N)

Importer=Label(win,text="進口商",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Importer.place(x=300,y=200,anchor=N)

Exporter=Label(win,text="出口商",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Exporter.place(x=300,y=300,anchor=N)

Bank=Label(win,text="銀行",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
Bank.place(x=300,y=400,anchor=N)


#Entry
setAddr_Importer = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Importer.place(x=100,y=250,width=400,height=40)

setAddr_Exporter = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Exporter.place(x=100,y=350,width=400,height=40)

setAddr_Bank = tk.Entry(win,font=('微軟正黑體 bold',14))
setAddr_Bank.place(x=100,y=450,width=400,height=40)

#Button
def buttonlisten():
    os.system("./runscript.sh public-contract.js")

bt_Send=tk.Button(win,text="送出",font=('微軟正黑體 bold',20),fg='gray10',bg='SeaGreen2',command=buttonlisten)
bt_Send.place(x=150,y=600,width=300,height=50)


win.mainloop()


