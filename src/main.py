from tkinter import *
root=Tk()
root.title("Rajat Prakashan")

root.geometry("1280x720")
bg_color="#4D0039"

title = Label(root,text="Billing Software",font=("times new roman",40,"bold"),bg=bg_color,fg='white', relief=GROOVE)
title.pack(fill=X)

#==========================Customer Details Frame=========================

F1 = LabelFrame(root,text="Customer Details",font=("times new roman",18,"bold"),fg="gold",bg=bg_color, bd=10, relief=GROOVE)
F1.place(x=0,y=80,relwidth=1)

cname_lbl = Label(F1, text="Customer Name",font=("times new roman",18,"bold"),bg=bg_color,fg='white')
cname_lbl.grid(row=0,column=0,padx=20,pady=5)

cname_txt = Entry(F1,width=15,font="arial 15",bd=3,relief=SUNKEN)
cname_txt.grid(row=0,column=1,padx=10,pady=5)

cphone_lbl = Label(F1, text="Phone Number",font=("times new roman",18,"bold"),bg=bg_color,fg='white')
cphone_lbl.grid(row=0,column=2,padx=20,pady=5)

cphone_txt = Entry(F1,width=15,font="arial 15",bd=3,relief=SUNKEN)
cphone_txt.grid(row=0,column=3,padx=10,pady=5)


#==========================Product Details Frame=========================

F2 = LabelFrame(root,text="Product Details",font=("times new roman",18,"bold"),fg="gold",bg=bg_color, bd=10, relief=GROOVE)
F2.place(x=20,y=180,width=630, height=500)

itm_lbl = Label(F2, text="Product name",font=("times new roman",18,"bold"),bg=bg_color,fg='light green')
itm_lbl.grid(row=0,column=0,padx=30,pady=20)

itm_txt = Entry(F2,width=20,font="arial 15",bd=3,relief=SUNKEN)
itm_txt.grid(row=0,column=1,padx=10,pady=20)

rate_lbl = Label(F2, text="Product price",font=("times new roman",18,"bold"),bg=bg_color,fg='light green')
rate_lbl.grid(row=1,column=0,padx=30,pady=20)

rate_txt = Entry(F2,width=20,font="arial 15",bd=3,relief=SUNKEN)
rate_txt.grid(row=1,column=1,padx=10,pady=20)

qty_lbl = Label(F2, text="Product quantity",font=("times new roman",18,"bold"),bg=bg_color,fg='light green')
qty_lbl.grid(row=2,column=0,padx=30,pady=20)

qty_txt = Entry(F2,width=20,font="arial 15",bd=3,relief=SUNKEN)
qty_txt.grid(row=2,column=1,padx=10,pady=20)


#==========================Button=========================

btn1 = Button(F2,text="Add Item",font="arial 15 bold",bg="lime",fg="black",width=15, padx=10)
btn1.grid(row=3,column=0,padx=10,pady=20)

btn2 = Button(F2,text="Generate bill",font="arial 15 bold",bg="lime",fg="black",width=15, padx=10)
btn2.grid(row=3,column=1,padx=10,pady=20)

btn3 = Button(F2,text="Clear",font="arial 15 bold",bg="lime",fg="black",width=15, padx=10)
btn3.grid(row=4,column=0,padx=10,pady=20)

btn4 = Button(F2,text="Exit",font="arial 15 bold",bg="lime",fg="black",width=15, padx=10)
btn4.grid(row=4,column=1,padx=10,pady=20)


#==========================Bill Area=========================

F3=Frame(root, relief=GROOVE, bd=10)
F3.place(x=700, y=180, width=500, height=500)

bill_title = Label(F3, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
bill_title.pack(fill=X)

scroll_y = Scrollbar(F3, orient=VERTICAL)

text_area = Text(F3, yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)

scroll_y.config(command=text_area.yview)
text_area.pack(fill=BOTH, expand=1)


root.mainloop()