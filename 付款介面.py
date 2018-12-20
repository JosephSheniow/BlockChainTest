import tkinter as tk 
from tkinter import *

class secondpage():
    def __init__(self,root,myTitle,flag):    
        #window
        win=tk.Tk()
        win.title("付款介面")
        win.geometry("600x350")
        win.configure(bg='gray20')


        #Label
        enter_amount=Label(win,text="付款金額",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        enter_amount.place(x=300,y=70,anchor=N)
        #Entry
        Pay_Amount = tk.Entry(win,font=('微軟正黑體 bold',14))
        Pay_Amount.place(anchor=N,x=300,y=120,width=350,height=40)


        #Button
        bt_Send=tk.Button(win,text="Send",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Send.place(x=300,y=270,width=200,height=40,anchor=N)


        win.mainloop()


root=tk.Tk()
root.title("輸入合約地址")
root.geometry("400x400")
root.configure(bg='gray20')
window1=tk.IntVar(root,value=0)

#Label
InsertAdd=Label(root,text="輸入 Contract Address",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
InsertAdd.place(x=200,y=60,anchor=N)

#Entry
ContractAdd = tk.Entry(root,font=('微軟正黑體 bold',14))
ContractAdd.place(anchor=N,x=200,y=170,width=300,height=40)

#Button
def buttonClick():
    if window1.get()== 0:
        window1.set(1)
        w1 = secondpage(root,'Send',1)
        bt_Send.wait_window(w1.top)
        window1.set(0)


bt_Send=tk.Button(root,text="Send",font=('微軟正黑體 bold',16),fg='gray10',bg='spring green',command=buttonClick)
bt_Send.place(x=200,y=300,width=100,height=40,anchor=N)


root.mainloop()