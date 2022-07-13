#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 22:33:32 2021

@author: devumeshkumarparmar
"""
""" PAGE IS COMPLITED """

from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import window1 as win1

class bw_2:
    def __init__(self,root):
        self.root=root
        self.root.config(bg="black")
        self.root.title("LIST-OF-ALL-GUN")
      
        self.but_img3=PhotoImage(file="back.png")
        self.bw3=Button(self.root,bg="white",activebackground="white",command=self.back)
        self.bw3.config(image=self.but_img3)
        self.bw3.place(x=985,y=0)
        
        self.photo=Image.open("back_wid.png")
        self.bg=ImageTk.PhotoImage(self.photo)
        self.d1=Label(self.root,image=self.bg,bg="black",fg="black")
        self.d1.place(x=0,y=0)
        #-----------
        self.file_setup()
        
        #textbox to display data
        f1=open("list_of_all.txt",'r')
        a=f1.readlines()
        self.text = Text(self.root,bg="black",fg="white",relief=SUNKEN)
        for i in range(len(a)):
            self.text.insert(INSERT,a[i])
        self.text.config(state=DISABLED,font =("Courier", 20))
        self.text.pack(padx=110,pady=110,expand=True,fill=BOTH,side=RIGHT)

        self.Scroll = Scrollbar(self.text)
        self.Scroll.pack(side=RIGHT,fill=Y)
        self.Scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.Scroll.set)
        
        
        
        
    def rakh(self):
        self.bw3.destroy()
        self.Scroll.destroy()
        self.text.destroy()
        self.d1.destroy()
    def back(self):
        self.rakh()
        win1.window1(self.root)
    def file_setup(self):
        f=open("gun_database.txt",'r')
        f1=open("list_of_all.txt",'w')
        f1.write("GUN NAME".rjust(15," "))
        f1.write("BRAND NAME".rjust(15," "))
        f1.write("QUANTITY".rjust(15," "))
        f1.write("\n")
        f1.write("\n")
        a=f.readlines()
        for i in range(len(a)):
            d=a[i].split("|")
            for i in range(len(d)):
                f1.write(d[i].rjust(15," "))
            f1.write("\n")
        f.close()
        f1.close()
        
            
                
        