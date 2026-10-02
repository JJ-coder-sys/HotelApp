
from tkinter import *
from tkinter import ttk
import control as connect
from tkinter import messagebox as msg
import os
import sqlite3
def manager():
     os.system('python manager.py')
def rec():
      os.system('python rec.py')

def login():
      root.destroy()
      os.system('python intro.py')

def log():
    username=entu.get()
    password=entp.get()
    role=user_role.get()

    if username=="" and password=="" and role=="":
            msg.showinfo("Alert", "Empty field")
            return
    
    
    connect.con
    connect.cur
    result=connect.cur.execute("""SELECT * FROM users WHERE username=? AND password=? AND role=?""", (username, password, role))
    if result:
          msg.showinfo("Success","Record found")
          root.destroy()
          if role.lower()=="hotel manager":
                manager()
    elif role.lower()=="receptionist":
          rec()
          return
    else:
          msg.showinfo("Alert","Unauthorized Login")

          
          
root=Tk()
root.title("Loginpage")
root.geometry('400x400+500+0')
root.configure(background="#DDD3DD")
root.resizable(0,0)
lblhead=Label(root,text="Login Page", font=("verdana",20,"bold"),bg="#DDD3DD", fg="black")
lblhead.pack(pady=(60,20))


#username
fr=Frame(root, width=50, height=50, bg="#DDD3DD" )
lblu=Label(fr, text="Username: ", font=("verdana",14),bg="#DDD3DD",fg="black")
lblu.grid(row=0, column=0)
entu=Entry(fr,width=40, relief="flat")
entu.grid(row=0, column=1)

#Password
lblp=Label(fr, text="Password: ", font=("verdana",14),bg="#DDD3DD",fg="black")
lblp.grid(row=1, column=0)
entp=Entry(fr,width=40, relief="flat", show="*")
entp.grid(row=1, column=1)

#User role
lblr=Label(fr, text="Role: ", font=("verdana",14),bg="#DDD3DD",fg="black")
lblr.grid(row=2, column=0)
role=["hotel manager","receptionist"]
user_role=ttk.Combobox(fr,width=38, values=role)
user_role.grid(row=2, column=1)





btnReg=Button(fr, width=10, bg="white", fg="black", text="Login" , command=log)
btnReg.grid(row=10, column=1, pady=5)

already=Button(fr, width=40,bg="#DDD3DD", fg="black", text="Dont have account? sign up", command=login, relief="flat")
already.grid(row=4, column=1)


fr.pack(pady=20)
root.mainloop()