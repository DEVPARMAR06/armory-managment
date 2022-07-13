#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 17:12:19 2021

@author: devumeshkumarparmar
"""

from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import back_window_1 as b_w
class w_1_1:
    def __init__(self,root):
        self.root=root
        self.root.title("ADD-NEW-GUN")
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
        
        self.window()
    def window(self):
        self.gunname=False
        self.brandname=False
        self.quantity=False
        self.gu=True
        self.br=True
        self.qu=True
        
        
        self.gun=StringVar()
        self.gun_name=Entry(self.root,textvariable=self.gun,bg="black",fg="white")
        self.gun_name.place(x=450, y=250)
        
        #---Place Holder Thing
        self.gun_name.insert(0, "Gun-Name")
        self.gun_name.configure(state=DISABLED)
        self.gun_name.bind("<Button>",self.gunn)
        
        
        self.brand=StringVar()
        self.brand_name=Entry(self.root,textvariable=self.brand,bg="black",fg="white")
        self.brand_name.place(x=450, y=300)
        
        #place-holder Thing
        self.brand_name.insert(0, "Brand-Name")
        self.brand_name.configure(state=DISABLED)
        self.brand_name.bind("<Button>",self.brandd)
        #--
        self.qun=StringVar()
        self.qun1=Entry(self.root,textvariable=self.qun,bg="black",fg="white")
        self.qun1.place(x=450, y=350)
        
        #---
        self.qun1.insert(0, "Quantity")
        self.qun1.configure(state=DISABLED)
        self.qun1.bind("<Button>",self.qunn)
        
        
        self.enter=Button(self.root,text="ENTER",bg="black",activebackground="black",command=self.enter)
        self.enter.place(x=450,y=400)
        
        self.reset=Button(self.root,text="RESET",bg="black",activebackground="black",command=self.reset)
        self.reset.place(x=450,y=450)
        
        self.but_img3=PhotoImage(file="back.png")
        self.bw3=Button(self.root,bg="white",activebackground="white",command=self.back)
        self.bw3.config(image=self.but_img3)
        self.bw3.place(x=50,y=70)
        
    def gunn(self,event):
        
        self.gun_name.configure(state=NORMAL)
        self.gun_name.delete(0,END)
        self.gunname=True
        self.gu=False

    def brandd(self,event):
        
        self.brand_name.configure(state=NORMAL)
        self.brand_name.delete(0, END)
        self.brandname=True
        self.br=False
        
    def qunn(self,event):
        self.qun1.configure(state=NORMAL)
        self.qun1.delete(0, END)
        self.quantity=True
        self.qu=False
        
    def back(self):
        self.rakh()
        b_w.bw_1(self.root)
        
    def enter(self):
        if self.check_Null():
            tkmb.showinfo(title='Message Box', message='ENTER ALL FIELD!!!', icon='info')
        elif 0>=int(self.qun.get()):
            tkmb.showinfo(title='Message Box', message='QUANTITY IS ALWAYS IN POSITIVE NUMBER!!!', icon='info')
        else:
            ch=self.check()
            a=self.gun.get()
            b=self.brand.get()
            c=self.qun.get()
            if ch[0]:
                f=open('gun_database.txt','r')
                list_of_lines=f.readlines()
                print(list_of_lines)
                list_of_lines[ch[2]]=a+" | "+b+" | "+ch[1]+"\n"
                f=open('gun_database.txt','w')
                f.writelines(list_of_lines)
                f.close()
            else:
                f=open('gun_database.txt','a')
                f.write(a+" | "+b+" | "+c+"\n")
                f.close
            tkmb.showinfo(title='Message Box', message='ENTERED IN DATABASE', icon='info')
            self.reset_submit()
    def reset_submit(self):
        self.rakh()
        b_w.res(self.root)
    def reset(self):
        self.rakh()
        b_w.res(self.root)
    def rakh(self):
        self.gun_name.destroy()
        self.brand_name.destroy()
        self.enter.destroy()
        self.reset.destroy()
        self.bw3.destroy()
        self.qun1.destroy()
        self.d1.destroy()
    def check(self):
        f=open('gun_database.txt','r')
        a=self.gun.get()
        b=self.brand.get()
        c=int(self.qun.get())
        line_no=0
        for line in f.readlines():
            d=line.split("|")
            if a == d[0].strip(" ") and b == d[1].strip(" "):
                f.close()
                return True,str(int(d[2].strip(" "))+c),line_no
            line_no=line_no+1
        else:
            return False,0
    def check_Null(self):
        a=self.gun.get()
        b=self.brand.get()
        c=self.qun.get()
        if self.gu or self.qu or self.br or a=='' or b=='' or c=='':
            return True
        else:
            return False
        
                
                
            
        
        
        
        
        
        
        
