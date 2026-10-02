import tkinter
import control as connect
from tkinter import messagebox as msg
import sqlite3
from datetime import datetime
from tkinter import ttk
from PIL import Image,ImageTk
root=tkinter.Tk()
root.title("Receptionist Account")
root.geometry('1350x1200+0+0')
root.configure(bg="#DDD3DD")

class hotel_app():
    def __init__(self,root):
        self.root=root

        self.root.title("Reception account")
        self.root.geometry('1350x1200+0+0')
        self.root.configure(bg="#fff")
        self.style=ttk.Style()
        self.main_ui()



def main_ui(self):
        img=Image.open('images/logo.png')
        img=img.resize((200,100))
        img_tk=ImageTk.PhotoImage(img)
        img=Image.open('images/logo.png')
        img=img.resize((200,100))
        img_tk=ImageTk.PhotoImage(img)

        self.head=ttk.Frame(self.root,padding=12)
        self.head.pack(fill="x")
        lbl=tkinter.Label(self.head, image=img_tk)
        lbl.image = img_tk 
        lbl.place(x=0, y=0)

        ttk.Label(
            self.head,text="Receptionist",font=("verdana",20,"bold"),
            foreground="#000"
            ).pack(side="top")

        ttk.Label(self.head,text="logged in",font=("verdana",10,"bold"),
        ).pack(side="right", padx=10)
        ttk.Button(self.head,text="log out",command=self.logout).pack(side="right", padx=10)




root.resizable(0,0)
root.mainloop()