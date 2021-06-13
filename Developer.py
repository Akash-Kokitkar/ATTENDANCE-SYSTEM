
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_details import Student
import os
from train import Train
from attendance import Attendance
from face_recognition import Face_recognition


class Developer:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        title_lbl = Label(self.root, text="Attendance Record", font=("times new roman", 35, "bold"),
                          bg="orange", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # first img
        img = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\dev.jpg")
        img = img.resize((1530, 720), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        #frame

        main_frame = Frame(f_lbl, bd=2)
        main_frame.place(x=700, y=55, width=1000, height=600)

        img_left = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\images.jpg")
        img_left = img_left.resize((200, 200), Image.ANTIALIAS)
        self.photo_left_img = ImageTk.PhotoImage(img_left)

        # f_lbl2 = Label(main_frame, image=self.photo_left_img)
        # f_lbl2.place(x=150, y=450, width=200, height=200)
        #

        # Label

        title_lbl = Label(main_frame, text="Welcome to developer site", font=("times new roman", 20, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0)

        title_lbl = Label(main_frame, text="I am python developer", font=("times new roman", 15, "bold"),
                           fg="black")
        title_lbl.place(x=0, y=50)

        title_lbl = Label(main_frame, text="This system is  developed using Python OpenCV With Tkinter GUI & Sqlite Database ", font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=90)

        title_lbl = Label(main_frame, text="System help is attendance managemnt and detection ",
                          font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=130)

        title_lbl = Label(main_frame, text="If you have any suggestion or querry ",
                          font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=170)

        title_lbl = Label(main_frame, text="You can contact me  ",
                          font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=210)

        title_lbl = Label(main_frame, text="@ kokitkarakash6@gmail.com ",
                          font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=250)

        title_lbl = Label(main_frame, text="Thank You",
                          font=("times new roman", 15, "bold"),
                          fg="black")
        title_lbl.place(x=0, y=290)


        # img = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\di.jpg")
        # img = img.resize((300,310), Image.ANTIALIAS)
        # self.photoimg = ImageTk.PhotoImage(img)
        #
        # f_lbl = Label(main_frame, image=self.photoimg)
        # f_lbl.place(x=0, y=75, width=300, height=310)
        #

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()


