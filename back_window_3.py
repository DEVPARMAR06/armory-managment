#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:30:00 2021

@author: devumeshkumarparmar
"""
import back_w_3_1 as b_3_1
import back_w_3_2 as b_3_2
import window1 as win1
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
class bw_3:
    def __init__(self,root):
        self.root=root
        self.root.title("GUN-ALLOTMENT")
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
        
        self.but_img=PhotoImage(file="B_W_3_1.png")
        self.bw1=Button(self.root,bg="black",activebackground="black",command=self.list_of_allocated)
        self.bw1.config(image=self.but_img)
        self.bw1.place(x=325,y=250)
        
        self.but_img2=PhotoImage(file="B_W_3_2.png")
        self.bw2=Button(self.root,bg="black",activebackground="black",command=self.to_allot)
        self.bw2.config(image=self.but_img2)
        self.bw2.place(x=570,y=250)
        
        self.but_img3=PhotoImage(file="back.png")
        self.bw3=Button(self.root,bg="white",activebackground="white",command=self.back)
        self.bw3.config(image=self.but_img3)
        self.bw3.place(x=50,y=70)
    def list_of_allocated(self):
        self.rakh()
        b_3_1.w_3_1(self.root)
    def to_allot(self):
        self.rakh()
        b_3_2.w_3_2(self.root)
    def back(self):
        self.rakh()
        win1.window1(self.root)
    def rakh(self):
        self.bw1.destroy()
        self.bw2.destroy()
        self.bw3.destroy()
        self.d1.destroy()
    # Reset For back_w_3_2.py 
class res:
    def __init__(self,root):
        self.root=root
        b_3_2.w_3_2(self.root)
              
    