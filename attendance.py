
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import _sqlite3
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Record")


        # stringVar() variable
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_data=StringVar()
        self.var_atten_attendance=StringVar()






        # first img
        img = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\smart-attendance.jpg")
        img = img.resize((800,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)
        # second img

        img1 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img1 = img1.resize((800,200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=700, height=200)

        img3 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\dev.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)



        # bg img*******************

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Attendance Record", font=("times new roman", 35, "bold"),
                          bg="light blue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)


# main Frame******************
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=600)


          # *******Left frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=760, height=580)

         # image in left frame
        img_left = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\girl.jpeg")
        img_left = img_left.resize((740, 130), Image.ANTIALIAS)
        self.photo_left_img = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(left_frame, image=self.photo_left_img)
        f_lbl2.place(x=5, y=0, width=750, height=130)

        # frame in left side

        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="",
                                  font=("times new roman", 12, "bold"))
        course_frame.place(x=0, y=130, width=750, height=370)


        # label entry
        Attendance = Label(course_frame, bg="white", text="Attendace_ID", font=("times new roman", 13, "bold"))
        Attendance.grid(row=0, column=0, padx=10, sticky=W)

        Attendance=ttk.Entry(course_frame,textvariable=self.var_atten_id ,width=20,font=("times new roman", 12, "bold"))
        Attendance.grid(row=0,column=1,padx=10,pady=8,sticky=W)

        #Name
        Name = Label(course_frame, bg="white",text="Name", font=("times new roman", 13, "bold"))
        Name.grid(row=0, column=3, padx=10, sticky=W)

        Name = ttk.Entry(course_frame, width=20,textvariable=self.var_atten_name , font=("times new roman", 12, "bold"))
        Name.grid(row=0, column=4, padx=10, pady=8, sticky=W)

        #date
        date = Label(course_frame, bg="white", text="Date", font=("times new roman", 13, "bold"))
        date.grid(row=1, column=0, padx=10, sticky=W)

        date = ttk.Entry(course_frame, width=20,textvariable=self.var_atten_data , font=("times new roman", 12, "bold"))
        date.grid(row=1, column=1, padx=10, pady=8, sticky=W)


        # Deapartnment
        Departnment = Label(course_frame, bg="white", text="Departnment", font=("times new roman", 13, "bold"))
        Departnment.grid(row=1, column=3, padx=10, sticky=W)

        Departnment = ttk.Entry(course_frame, width=20,textvariable=self.var_atten_dep, font=("times new roman", 12, "bold"))
        Departnment.grid(row=1, column=4, padx=10, pady=8, sticky=W)

        # time

        Time = Label(course_frame, bg="white", text="Time", font=("times new roman", 13, "bold"))
        Time.grid(row=2, column=0, padx=10, sticky=W)

        Time = ttk.Entry(course_frame, width=20,textvariable=self.var_atten_time , font=("times new roman", 12, "bold"))
        Time.grid(row=2, column=1, padx=10, pady=8, sticky=W)

          # roll no ******************
        roll = Label(course_frame, bg="white", text="Roll No", font=("times new roman", 13, "bold"))
        roll.grid(row=2, column=3, padx=10, sticky=W)

        roll = ttk.Entry(course_frame, width=20,textvariable=self.var_atten_roll ,font=("times new roman", 12, "bold"))
        roll.grid(row=2, column=4, padx=10, pady=8, sticky=W)

        # attendance
        Attendance = Label(course_frame, bg="white", text="Attendace_Stastus", font=("times new roman", 13, "bold"))
        Attendance.grid(row=3, column=0, padx=10, sticky=W)

        Attendace = ttk.Combobox(course_frame,textvariable=self.var_atten_attendance ,font=("times new roman", 12, "bold"),
                                  width=17, state="read only ")
        Attendace['values'] = ("Present","Absent")
        Attendace.current(0)
        Attendace.grid(row=3, column=1, padx=2, pady=10)

        # button frame
        bttn_frame = Frame(course_frame, bg="white", bd=2, relief=RIDGE)
        bttn_frame.place(x=0, y=250, width=715, height=35)

        save_btn = Button(bttn_frame,  bg="black",command=self.import_csv, width=18, fg="yellow", text="Import_Csv",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=0)

        # update button
        save_btn = Button(bttn_frame, bg="black",command=self.update,width=18, fg="yellow", text="Update",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=1)

        # export btn
        save_btn = Button(bttn_frame, bg="black",command=self.export_csv,width=18, fg="yellow", text="Export",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=2)

        # reset btn
        save_btn = Button(bttn_frame, command=self.reset_data, bg="black", width=20, fg="yellow", text="Reset",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=3)

        # *****************right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=780,y=10, width=660, height=580)

        table_frame = Frame(right_frame, bg="white", bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=700, height=545)

        # @@@@@@@@@@ Scroll Bar

        scrollbary = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrollbarx = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendance_table = ttk.Treeview(table_frame,column=("id","roll no","name","Dep",  "time", "date","attendance"),xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary)


        scrollbarx.pack(side=RIGHT, fill=X)
        scrollbary.pack(side=BOTTOM, fill=Y)

        scrollbarx.config(command=self.attendance_table.yview)
        scrollbary.config(command=self.attendance_table.xview)


        self.attendance_table.heading("id",text="Attendance Id")
        self.attendance_table.heading("roll no", text="Roll")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("Dep", text="Departnment")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Atttendance")

        self.attendance_table["show"]="headings"
        self.attendance_table.column("id",width=100)
        self.attendance_table.column("roll no", width=100)
        self.attendance_table.column("name", width=100)
        self.attendance_table.column("Dep", width=100)
        self.attendance_table.column("time", width=100)
        self.attendance_table.column("date", width=100)
        self.attendance_table.column("attendance", width=100)

        self.attendance_table.pack(fill=BOTH, expand=1)

        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)



    def fetchdata(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)


# @@@@@@@@@@@@@@@@@@import csv@@@@@@@@@@@@@@@
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with  open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)

            self.fetchdata(mydata)


# @@@@@@@@@@@@@@@@@@@export csv@@@@@@@@@@@@@@@@@
    def export_csv(self):
        try :
            if len(mydata)<1:
                messagebox.showerror("Error","No data found",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)

            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported"+os.path.basename(fln)+"sucessfully")

        except Exception as es:
            messagebox.showinfo("Error", f"{str(es)}", parent=self.root)

    def get_cursor(self,event=""):
         cursor_row=self.attendance_table.focus()
         content=self.attendance_table.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])

         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_data.set(rows[5])

         self.var_atten_attendance.set(rows[6])

    def reset_data(self):

        self.var_atten_id.set("")
        self.var_atten_roll.set("")

        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_data.set("")

        self.var_atten_attendance.set("")

    def update(self):
        id = self.var_atten_id.get()
        roll = self.var_atten_roll.get()
        name = self.var_atten_name.get()
        dep = self.var_atten_dep.get()
        time = self.var_atten_time.get()
        date = self.var_atten_data.get()
        attendn = self.var_atten_attendance.get()

        # write to csv file
        try:
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)

            with open(fln, mode="a", newline="\n") as f:
                dict_writer = csv.DictWriter(f, fieldnames=( ["ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"]))

                dict_writer.writeheader()
                dict_writer.writerow({
                    "ID": id,
                    "Roll": roll,
                    "Name": name,
                    "Department": dep,
                    "Time": time,
                    "Date": date,
                    "Attendance": attendn
                })
            messagebox.showinfo("Data Exported", "Your data exported to " + os.path.basename(fln) + " Successfully",
                                parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()

