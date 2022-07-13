from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox as tkmb
import back_window_1 as back_win1
import back_window_2 as back_win2
import back_window_3 as back_win3
class window1:
    def __init__(self,root):
        self.root=root
        self.root.title("MAIN WINDOW")
        self.photo=Image.open("192866.jpg")
        self.bg=ImageTk.PhotoImage(self.photo)

#create a lable size of a window
#we use lable as a back ground image
        
        self.d1=Label(self.root,image=self.bg)
        self.d1.pack()
        self.but_img=PhotoImage(file="BUT-1.png")
        self.bw1=Button(self.root,bg="white",activebackground="white",command=self.add_gun)
        self.bw1.config(image=self.but_img)
        self.bw1.place(x=200,y=250)
        
        self.but_img2=PhotoImage(file="BUT-2.png")
        self.bw2=Button(self.root,bg="white",activebackground="white",command=self.GL)
        self.bw2.config(image=self.but_img2)
        self.bw2.place(x=450,y=250)
        
        self.but_img3=PhotoImage(file="BUT-3.png")
        self.bw3=Button(self.root,bg="white",activebackground="white",command=self.GA)
        self.bw3.config(image=self.but_img3)
        self.bw3.place(x=700,y=250)
        
    def add_gun(self):
        self.rakh()
        back_win1.bw_1(self.root)
    def GA(self):
        self.rakh()
        back_win3.bw_3(self.root)
    def GL(self):
        self.rakh()
        back_win2.bw_2(self.root)
    def rakh(self):
        self.bw1.destroy()
        self.bw2.destroy()
        self.bw3.destroy()
        self.d1.destroy()
    
      
    