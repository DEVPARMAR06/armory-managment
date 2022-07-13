#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 18:55:32 2021

@author: devumeshkumarparmar
"""


#we want to use place because we want a back ground image
#from window1 import *

#music is added

from pygame import mixer
import window1 as win1
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb

class mainwin:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin Login")
        self.root.iconbitmap()

#geomatry width x length
#set max and min width
        self.root.geometry("1100x688")
        self.root.minsize(1100,688)
        self.root.maxsize(1100,688)

#back ground image For Jpg Use ImageTk
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
#root.attributes('-alpha',0.5)  #to use whole screen transparant
#---------------------------------------------------------------
#---------------------------------------------------------------
# Create A Label in grid

#for palceholder
        self.usercheck=False
        self.passcheck=False

#------------------------------------------No Need To Use Label 
#--------------------------------------------------------------
#username=Label(root,text="User_Name:")
#username.place(x=300, y=150)

#password=Label(root,text="User_Password")
#password.place(x=500, y=150)

#create a entry width
        
        self.user=StringVar()
        self.user1=Entry(self.root,textvariable=self.user,bg="black",fg="white")
        self.user1.place(x=450, y=250)
# for place holder
        self.user1.insert(0, "UserName")
        self.user1.configure(state=DISABLED)
        self.user1.bind("<Button>",self.userr)
#-------------------------------------------------------------------------------
        self.pas=StringVar()
        self.pas1=Entry(self.root,textvariable=self.pas,background="black",fg="white")
        self.pas1.place(x=450, y=300)
# for place holder-2
        self.pas1.insert(0, "PassWord")
        self.pas1.configure(state=DISABLED)
        self.pas1.bind("<Button>",self.passw)

# For Submit Button
# For submit image
        
        self.sub=PhotoImage(file="login-button-png-18035.png")

#b1=Button(root,image=sub,bg="black",activebackground="black",command=admin)
        self.b1=Button(self.root,text="LOGIN",bg="black",activebackground="black",command=self.admin)
        self.b1.place(x=483,y=350)
# defs
    def qui(self):
        #not distroy whole window
        #self.root.destroy()
        self.user1.destroy()
        self.pas1.destroy()
        self.b1.destroy()
        self.d1.destroy()
        win1.window1(self.root)
       #window1.win1(root)
    
    def userr(self,event):
        
        self.user1.configure(state=NORMAL)
        self.user1.delete(0,END)
        self.usercheck=True

    def passw(self,event):
        
        self.pas1.configure(state=NORMAL,show='*')#for passwod entry field
        self.pas1.delete(0, END)
        self.passcheck=True

    def admin(self):
        
       u=self.user.get()
       p=self.pas.get()
       f=open('Admin_Data.txt','r')
       b=0
       for line in f.readlines():
           
           a=line.split(' ')
           for i in range(1):
               
               if a[0]==u and a[1].strip("\n")==p:
                   
                   #tkmb.showinfo(title='Message Box', message='Varified User', icon='info')
                   mixer.init()
                   mixer.music.load('welcome_back.mp3')
                   mixer.music.play()
                   self.qui()
                   b=b+1
       if b==0:
           tkmb.showinfo(title='Message Box', message='INCORRECT DETAILS', icon='warning')

    
#class window1:
#    def __init__(self,root):
#        self.root=root
#        self.but_img=PhotoImage(file="textfx.png")
#        self.bw1=Button(self.root,text="Gun Allotment",bg="black",activebackground="black",command=self.add_gun)
#        self.bw1.place(x=300,y=250)
#        
#        self.bw2=Button(self.root,text="Gun List",bg="black",activebackground="black",command=self.GA)
#        self.bw2.place(x=450,y=250)
#        
#        self.bw3=Button(self.root,text="Add Gun",bg="black",activebackground="black",command=self.GA)
#        self.bw3.place(x=600,y=250)
#        
#    def add_gun():
#        pass
#    def GA():
#        pass
        
        
        
        
           
    
    


#create instance
root=Tk()
#title text
a=mainwin(root)
root.mainloop()