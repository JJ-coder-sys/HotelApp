#print("Hello world")
#print(4+3)
# 2a=40
# @s=40
#_a=50
#print(_a)
#totalsum=40
#def add():
#    a=40
#num=3000
#num1=3000.4
#print(num)
#print(type(num))
#print(type(num1))
#num2=50j
#num3=500j
#print(type(num2))
#print(num2 + num1)
#name="Emmanuel james"
#print(name)
#print(type(name))
#email='johnmail.com'
#print(email)
#print(type(email))

#age=True
#print(age)
#print(type(age))
#print(age)

# type conversion
#a='john'
#b='emmanuel'
#c=500
#str()
#int()
#float()

#print(a + b + str(c))

from tkinter import*
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox as msg
import sqlite3 as sql
import control as connect

import os

def login():
      root.destroy()
      os.system('python login.py')

def reg():
    username=entu.get()
    name=entn.get()
    password=entp.get()
    email=entem.get()
    gender=entg.get()
    address=enta.get(1.0, "end")
    age=date_entry.get()
    role=user_role.get()

    
    if "@" not in email:
        msg.showerror("prompt","email must contain '@'")
    if name=="" and username=="" and password=="" and email=="" and role=="":
        msg.showinfo("Alert","Empty field")
    try:
        connect.con
        connect.cur
        connect.cur.execute(""" insert into users(
        name, username, email, password, gender, address, age, role) values(?,?,?,?,?,?,?,?)
        """,(name,username,email,password,gender,address,age,role))
        connect.con.commit()
        msg.showinfo("success","mesage sent successfully")
        login()
        entu.delete(0,'end')
        entn.delete(0,'end')
        entp.delete(0,'end')
        entem.delete(0,'end')
        entg.delete(0,'end')
        enta.delete(1.0,'end')
        date_entry.delete(1.0,'end')
    except sql.IntegrityError:
        msg.showerror('error',f"{username} and {email} already exists")


         




root=Tk()
root.title("Introduction to GUI")
root.geometry('400x700+500+0')
root.configure(background="#DDD3DD")
root.resizable(0,0)

lblhead=Label(root, text="Registration Page", font=("verdama",20,"bold"), bg="#DDD3DD",fg="black")
lblhead.pack()

#Name age gender email password username address
#Name
fr=Frame(root, width=50, height=50, bg="#DDD3DD")
lbln=Label(fr, text="Name:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lbln.grid(row=0, column=0)
entn=Entry(fr, width=40, relief="flat")
entn.grid(row=0, column=1)

#email
lblem=Label(fr, text="Email:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lblem.grid(row=1, column=0)
entem=Entry(fr, width=40, relief="flat")
entem.grid(row=1, column=1)

#Username
lblu=Label(fr, text="Username:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lblu.grid(row=2, column=0)
entu=Entry(fr, width=40, relief="flat")
entu.grid(row=2, column=1)

#Password
lblp=Label(fr, text="Password:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lblp.grid(row=3, column=0)
entp=Entry(fr, width=40, relief="flat", show="*")
entp.grid(row=3, column=1)

#Gender
gender=["Male","Female"]
lblg=Label(fr, text="Gender:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lblg.grid(row=4, column=0)
entg=ttk.Combobox(fr, width=37, values=gender)
entg.grid(row=4, column=1)

#Address
lbla=Label(fr, text="Address:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lbla.grid(row=5, column=0)
enta=Text(fr, width=30, height=5, relief="flat")
enta.grid(row=5, column=1)

#Age
lblag=Label(fr, text="DOB:", font=("verdana", 14), bg="#DDD3DD", fg="black")
lblag.grid(row=6, column=0)
date_entry= DateEntry(fr, width=37, borderwidth=2)
date_entry.grid(row=6, column=1)
enta.grid(row=5, column=1)

#User role
lblr=Label(fr, text="Role: ", font=("verdana",14),bg="#DDD3DD",fg="black")
lblr.grid(row=6, column=0)
role=["hotel manager","receptionist"]
user_role=ttk.Combobox(fr,width=37, values=role)
user_role.grid(row=6, column=1)

already=Button(fr, width=40, bg="#DDD3DD", fg="black", text="Already have an account? login", command=login, relief="flat")
already.grid(row=11,column=1)


btnReg=Button(fr, width=10, font=("verdana" , 9), bg="white", fg="black", text="sign up" , command=reg)
btnReg.grid(row=10, column=1, pady=5)

fr.pack()





root.mainloop()




