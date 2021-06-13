
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_details import Student
import os
from train import Train
from attendance import Attendance
from face_recognition import Face_recognition


class help:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        title_lbl = Label(self.root, text="Help Desk", font=("times new roman", 35, "bold"),
                          bg="orange", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # first img
        img = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img = img.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        title_lbl = Label(f_lbl, text="Email @ :kokitkarakash6@gmail.com", font=("times new roman", 20, "bold"),
                          bg="white", fg="green")
        title_lbl.place(x=540, y=200)


if __name__=="__main__":
    root=Tk()
    obj=help(root)
    root.mainloop()


