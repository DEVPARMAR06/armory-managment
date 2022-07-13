#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:55:06 2021

@author: devumeshkumarparmar
"""
import back_w_1_1 as b_1_1
import back_w_1_2 as b_1_2
import window1 as win1
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
class bw_1:
    def __init__(self,root):
        self.root=root
        self.root.title("ADD-GUN")
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
        
        self.but_img=PhotoImage(file="B_W1.png")
        self.bw1=Button(self.root,bg="black",activebackground="black",command=self.add_new_gun)
        self.bw1.config(image=self.but_img)
        self.bw1.place(x=325,y=250)
        
        self.but_img2=PhotoImage(file="B_W2.png")
        self.bw2=Button(self.root,bg="black",activebackground="black",command=self.add_alloted_gun)
        self.bw2.config(image=self.but_img2)
        self.bw2.place(x=570,y=250)
        
        self.but_img3=PhotoImage(file="back.png")
        self.bw3=Button(self.root,bg="white",activebackground="white",command=self.back)
        self.bw3.config(image=self.but_img3)
        self.bw3.place(x=50,y=70)
    def add_new_gun(self):
        self.rakh()
        b_1_1.w_1_1(self.root)
    def add_alloted_gun(self):
        self.rakh()
        b_1_2.w_1_2(self.root)
    def back(self):
        self.rakh()
        win1.window1(self.root)
    def rakh(self):
        self.bw1.destroy()
        self.bw2.destroy()
        self.bw3.destroy()
        self.d1.destroy()
    # Reset For back_w_1_1.py 
class res:
    def __init__(self,root):
        self.root=root
        b_1_1.w_1_1(self.root)
        
class res1:
    def __init__(self,root):
        self.root=root
        b_1_2.w_1_2(self.root)        
    