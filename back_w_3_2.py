#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 17:52:32 2021

@author: devumeshkumarparmar
"""

from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import back_window_3 as b_w3
class w_3_2:
    def __init__(self,root):
        self.root=root
        self.root.title("ALLOT-A-GUN")
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
        
        
        self.window()
    def window(self):
        self.idnum=False
        self.gunname=False
        self.brandname=False
        self.quantity=False
        
        self.idn=True
        self.gu=True
        self.br=True
        self.qu=True
        
        self.id=StringVar()
        self.id1=Entry(self.root,textvariable=self.id,bg="black",fg="white")
        self.id1.place(x=450, y=200)
        
        #---Place Holder Thing
        self.id1.insert(0, "ID")
        self.id1.configure(state=DISABLED)
        self.id1.bind("<Button>",self.idd)
        
        
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
        
    def idd(self,event):
        
        self.id1.configure(state=NORMAL)
        self.id1.delete(0,END)
        self.idnum=True
        self.idn=False
        
    def back(self):
        self.rakh()
        b_w3.bw_3(self.root)
        
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
            d=self.id.get()
            if ch[0]:
                if ch[3]:
                    tkmb.showinfo(title='Message Box', message='ALLOTMENT QUANTITY IS NOT GRATER THEN IN STOCK!!!', icon='info')
                elif ch[4]:
                    tkmb.showinfo(title='Message Box', message='GUN IS OUT OF STOCK!!!', icon='info')
                else:
                    f=open('gun_database.txt','r')
                    list_of_lines=f.readlines()
                    print(list_of_lines)
                    list_of_lines[ch[2]]=a+" | "+b+" | "+ch[1]+"\n"
                    f=open('gun_database.txt','w')
                    f.writelines(list_of_lines)
                    f.close()
                    tkmb.showinfo(title='Message Box', message='ALLOTTED SUCCESSFULLY ', icon='info')
                    self.update_data_base()
                    self.reset_submit()
            else:
                tkmb.showinfo(title='Message Box', message='GUN DETAILS NOT FOUND!!!', icon='info')
    def reset_submit(self):
        self.rakh()
        b_w3.res(self.root)
    def reset(self):
        self.rakh()
        b_w3.res(self.root)
    def rakh(self):
        self.gun_name.destroy()
        self.brand_name.destroy()
        self.enter.destroy()
        self.reset.destroy()
        self.bw3.destroy()
        self.qun1.destroy()
        self.id1.destroy()
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
                if 0==int(d[2].strip(" ")):
                    return True,str(int(d[2].strip(" "))-c),line_no,False,True
                if c>int(d[2].strip(" ")):
                    return True,str(int(d[2].strip(" "))-c),line_no,True,False
                else: 
                   return True,str(int(d[2].strip(" "))-c),line_no,False,False
            line_no=line_no+1
        else:
            return False,0 
    def check_Null(self):
        a=self.gun.get()
        b=self.brand.get()
        c=self.qun.get()
        d=self.id.get()
        if self.gu or self.qu or self.br or self.idn or a=='' or b=='' or c==''or d=='':
            return True
        else:
            return False
    def update_data_base(self):
        f1=open('gun_allotment.txt','r')
        a=self.gun.get()
        b=self.brand.get()
        c=int(self.qun.get())
        d=self.id.get()
        ln=0
        X=0
        for line in f1.readlines():
            d1=line.split("|")
            if d == d1[0].strip(" ") and a == d1[1].strip(" ") and b == d1[2].strip(" "):
                f1.close()
                f1=open('gun_allotment.txt','r')
                list_of_lines=f1.readlines()
                print(list_of_lines)
                list_of_lines[ln]=d+" | "+a+" | "+b+" | "+str(int(d1[3].strip(" "))+c)+"\n"
                f1=open('gun_allotment.txt','w')
                f1.writelines(list_of_lines)
                f1.close()
                X=1
            ln=ln+1
        if X==0:
            f1=open('gun_allotment.txt','a')
            f1.write(d+" | "+a+" | "+b+" | "+str(c)+"\n")
            f1.close()
            
        
        
        
                
                
            
        
        
        
        
        
        
        
