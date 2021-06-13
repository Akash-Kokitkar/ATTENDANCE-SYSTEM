
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from student_details import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from attendance import Attendance
from face_recognition import Face_recognition
from Developer import Developer
from help import help


class Face_recongnition:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")


        # first img
        img=Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\university.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# second img

        img1=Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\BestFacialRecognition.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=500,height=130)

# third img
        img2=Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\university.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=550,height=130)
# bg img

        img3 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\dev.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE_REGONITION_ATTENDANCE_SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # @@@@@@@@@@@time@@@@@@@@@@@@@@
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("times new roman",18,"bold"),bg="white",fg="black")
        lbl.place(x=1350,y=1,width=150,height=50)
        time()

        # std button
        img4 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img4 = img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1 = Button(bg_img, text="Student Detail", command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=200, y=300, width=220, height=40)
# face detect
        img5 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\face_detector1.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img,command=self.face_data, image=self.photoimg5, cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        b2 = Button(bg_img,command=self.face_data, text="Face recognize", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=500, y=300, width=220, height=40)

# attendance
        img6 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\smart-attendance.jpg")
        img6= img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img,command=self.attendance, image=self.photoimg6, cursor="hand2")
        b2.place(x=800, y=100, width=220, height=220)

        b2 = Button(bg_img, text="Attendance",command=self.attendance, cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=800, y=300, width=220, height=40)
# help
        img7 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\help.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_img,command=self.help,image=self.photoimg7, cursor="hand2")
        b2.place(x=1100, y=100, width=220, height=220)

        b2 = Button(bg_img,command=self.help, text="Help", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=1100, y=300, width=220, height=40)

# Train Face button

        img8 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2 = Button(bg_img,command=self.Train, image=self.photoimg8, cursor="hand2")
        b2.place(x=200, y=380, width=220, height=220)

        b2 = Button(bg_img,command=self.Train, text="Train", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=200, y=580, width=220, height=40)

# photo face button
        img9 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\girl.jpeg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(bg_img, image=self.photoimg9,command=self.open_img, cursor="hand2")
        b2.place(x=500, y=380, width=220, height=220)

        b2 = Button(bg_img, text="photo", cursor="hand2", command=self.open_img,font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=500, y=580, width=220, height=40)

# Developer
        img10 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\dev.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b2 = Button(bg_img,command=self.developer, image=self.photoimg10, cursor="hand2")
        b2.place(x=800, y=380, width=220, height=220)

        b2 = Button(bg_img,command=self.developer, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=800, y=580, width=220, height=40)

# Exi11
        img11 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2 = Button(bg_img,command=self.exitting, image=self.photoimg11, cursor="hand2")
        b2.place(x=1100, y=380, width=220, height=220)

        b2 = Button(bg_img,command=self.exitting, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="blue",
                    fg="white")
        b2.place(x=1100, y=580, width=220, height=40)


    def open_img(self):
        os.startfile("data")

    # @@@@@ function button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)


    # @@@@@@@@@@@Train daata
    def Train(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)


     # @@@@@@@@@@@face recognition@@@@@@@@@@@@

    def face_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Face_recognition(self.new_window)

    def attendance(self):
         self.new_window = Toplevel(self.root)
         self.app = Attendance(self.new_window)


    def developer(self):
         self.new_window = Toplevel(self.root)
         self.app = Developer(self.new_window)

    def help(self):
         self.new_window = Toplevel(self.root)
         self.app = help(self.new_window)

    def exitting(self):
        self.exit=messagebox.askyesno("Face Recognition","Do you want to exit this system",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return




if __name__=="__main__":
    root=Tk()
    obj=Face_recongnition(root)
    root.mainloop()

