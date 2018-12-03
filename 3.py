import tkinter as tk 
from tkinter import *

class secondpage():
    def __init__(self,root,myTitle,flag):    
        #window
        win=tk.Tk()
        win.title("哲哲小GG")
        win.geometry("1000x1000")
        win.configure(bg='gray20')


        #Label
        buyer=Label(win,text="買家",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        buyer.place(x=250,y=50,anchor=N)
        #Entry
        setAddr_buyer = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_buyer.place(anchor=N,x=250,y=90,width=300,height=40)

        #Label
        seller=Label(win,text="賣家",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        seller.place(x=250,y=140,anchor=N)
        #Entry
        setAddr_seller = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_seller.place(anchor=N,x=250,y=180,width=300,height=40)

        #Label
        item=Label(win,text="項目",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        item.place(x=250,y=230,anchor=N)
        #Entry
        setAddr_item = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_item.place(anchor=N,x=250,y=270,width=300,height=40)

        #Label
        money=Label(win,text="金額",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        money.place(x=250,y=320,anchor=N)
        #Entry
        setAddr_money = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_money.place(anchor=N,x=250,y=360,width=300,height=40)

        #Label
        time=Label(win,text="時間",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        time.place(x=250,y=410,anchor=N)
        #Entry
        setAddr_time = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_time.place(anchor=N,x=250,y=450,width=300,height=40)

        #Label
        export=Label(win,text="出貨港",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        export.place(x=250,y=500,anchor=N)
        #Entry
        setAddr_export = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_export.place(anchor=N,x=250,y=540,width=300,height=40)

        #Label
        Import=Label(win,text="到貨港",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Import.place(x=250,y=590,anchor=N)
        #Entry
        setAddr_Import = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Import.place(anchor=N,x=250,y=630,width=300,height=40)

        #Label
        detail=Label(win,text="其他細節",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        detail.place(x=250,y=680,anchor=N)
        #Entry
        setAddr_detail = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_detail.place(anchor=N,x=250,y=720,width=300,height=40)

        #Label
        Deposit=Label(win,text="訂金",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Deposit.place(x=250,y=770,anchor=N)
        #Entry
        setAddr_Deposit = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Deposit.place(anchor=N,x=250,y=810,width=300,height=40)

        #Label
        Balance=Label(win,text="尾款",font=('微軟正黑體 bold',20),fg='steelblue2',bg='gray20')
        Balance.place(x=250,y=860,anchor=N)
        #Entry
        setAddr_Balance = tk.Entry(win,font=('微軟正黑體 bold',14))
        setAddr_Balance.place(anchor=N,x=250,y=900,width=300,height=40)


        #Button
        bt_Send=tk.Button(win,text="送出",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Send.place(x=620,y=780,width=200,height=40,anchor=N)

        bt_Check=tk.Button(win,text="驗證",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Check.place(x=620,y=840,width=200,height=40,anchor=N)

        bt_Pay=tk.Button(win,text="付款",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Pay.place(x=620,y=900,width=200,height=40,anchor=N)

        bt_Bargain=tk.Button(win,text="起爭議",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Bargain.place(x=850,y=780,width=200,height=40,anchor=N)

        bt_Ship=tk.Button(win,text="出貨",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Ship.place(x=850,y=840,width=200,height=40,anchor=N)

        bt_Receive=tk.Button(win,text="完成收費",font=('微軟正黑體 bold',16),fg='gray10',bg='SeaGreen2')
        bt_Receive.place(x=850,y=900,width=200,height=40,anchor=N)

        #button
        bt_Show=tk.Button(win,text="顯示目前合約資訊",font=('微軟正黑體 bold',16),fg='gray10',bg='spring green')
        bt_Show.place(x=735,y=70,width=300,height=40,anchor=N)

        #label
        ShowContract=Label(win,font=('微軟正黑體 bold',20),bg='steel blue')
        ShowContract.place(x=735,y=140,width=445,height=600,anchor=N)

        win.mainloop()


root=tk.Tk()
root.title("小GG")
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