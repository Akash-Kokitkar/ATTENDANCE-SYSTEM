

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import _sqlite3
import cv2

class Student :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")
        self.root.title("Face_Recognition_System")

        self.var_dep=StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_adress = StringVar()
        self.var_gender = StringVar()






        # first img
        img = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img = img.resize((600, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=600, height=130)
        # second img

        img1 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img1 = img1.resize((600, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=610, y=0, width=500, height=130)

        # third img
        img2 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img2 = img2.resize((530, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=990, y=0, width=550, height=130)


        # bg img

        img3 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\dev.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT", font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

# main frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)


# left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman", 12, "bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\girl.jpeg")
        img_left = img_left.resize((740, 130), Image.ANTIALIAS)
        self.photo_left_img = ImageTk.PhotoImage(img_left)

        # left frame photo

        f_lbl2 = Label(left_frame, image=self.photo_left_img)
        f_lbl2.place(x=5, y=0, width=740, height=130)

        # course frame insider
        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Coursr Information",
                                font=("times new roman", 12, "bold"))
        course_frame.place(x=10, y=135, width=730, height=150)

        # departnment frame
        dep_label=Label(course_frame,bg="white",text="Department",font=("times new roman", 12, "bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),width=17,state="read only ")
        dept_combo['values']=("Select Departnment","Computer","It","Extc","Mechanical")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        course_label = Label(course_frame, bg="white", text="Course", font=("times new roman", 13, "bold"))
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="read only ")
        course_combo['values'] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10)

        # Year
        year_label = Label(course_frame, bg="white", text="Year", font=("times new roman", 13, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)


        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="read only ")
        year_combo['values'] = ("Select Year", "2018-19", "2019-20", "2020-21", "2021-22")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10)

        # semester
        semester_label = Label(course_frame, bg="white", text="Sem", font=("times new roman", 13, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state="read only ")
        semester_combo['values'] = ("Select Sem", "I", "II", "III", "IV","V","VI","VII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10)


        # student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Coursr Information",
                                  font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=250, width=730, height=300)

        # student id
        student_id_label = Label(class_student_frame, bg="white", text="Student_ID", font=("times new roman", 13, "bold"))
        student_id_label.grid(row=0, column=0, padx=10, sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0,column=1)

        # student name

        student_id_name = Label(class_student_frame, bg="white", text="Student Name",
                                 font=("times new roman", 13, "bold"))
        student_id_name.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3,padx=10,pady=5,)

        # class Div
        student_id_div = Label(class_student_frame, bg="white", text="Class Divison",
                                font=("times new roman", 13, "bold"))
        student_id_div.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        # student_id_ediv = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20, font=("times new roman", 12, "bold"))
        # student_id_ediv.grid(row=1, column=1,padx=10,pady=5)
        gender_combo = ttk.Combobox(class_student_frame, text="Div", textvariable=self.var_div,
                                    font=("times new roman", 12, "bold"), width=16,
                                    state="read only ")
        gender_combo['values'] = ("A", "B")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=2, pady=10)

        # roll no
        student_id_roll = Label(class_student_frame, bg="white", text="Roll NO",
                               font=("times new roman", 13, "bold"))
        student_id_roll.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        student_id_eroll = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        student_id_eroll.grid(row=1, column=3, padx=10, pady=5)

        # gender

        # student_id_div = Label(class_student_frame, bg="white", text="Gender",
        #                        font=("times new roman", 13, "bold"))
        # student_id_div.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        # student_id_ediv = ttk.Entry(class_student_frame,textvariable=self.var_gender ,width=20, font=("times new roman", 12, "bold"))
        # student_id_ediv.grid(row=2, column=1, padx=10, pady=5)

        gender_label = Label(class_student_frame, bg="white", text="Gender", font=("times new roman", 13, "bold"))
        gender_label.grid(row=2, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame,text="Gender",textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=16,
                                    state="read only ")
        gender_combo['values'] = ( "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=2, pady=10)

        # email no
        student_id_div = Label(class_student_frame, bg="white", text="email",
                               font=("times new roman", 13, "bold"))
        student_id_div.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        student_id_ediv = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        student_id_ediv.grid(row=2, column=3, padx=10, pady=5)

        # phone no
        student_id_div = Label(class_student_frame, bg="white", text="Phone No",
                               font=("times new roman", 13, "bold"))
        student_id_div.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        student_id_ediv = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        student_id_ediv.grid(row=3, column=1, padx=10, pady=5)

        # Adress
        student_id_div = Label(class_student_frame, bg="white", text="Adress",
                               font=("times new roman", 13, "bold"))
        student_id_div.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        student_id_ediv = ttk.Entry(class_student_frame,textvariable=self.var_adress, width=20, font=("times new roman", 12, "bold"))
        student_id_ediv.grid(row=3, column=3, padx=10, pady=5)


        # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take A Photo",value="Yes")
        radiobtn1.grid(row=6,column=0)


        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="No Photo", value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame
        bttn_frame=Frame(class_student_frame,bg="white",bd=2,relief=RIDGE)
        bttn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(bttn_frame,command=self.add_data,bg="black",width=18,fg="white",text="Save",font=("times new roman", 12, "bold"))
        save_btn.grid(row=0,column=0)

         # update button
        save_btn = Button(bttn_frame,command=self.update, bg="black", width=18, fg="white", text="Update",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=1)

        # delete btn
        save_btn = Button(bttn_frame,bg="black",command=self.delete, width=18, fg="white", text="Delete",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=2)

        # reset btn
        save_btn = Button(bttn_frame,command=self.reset, bg="black", width=18, fg="white", text="Reset",
                          font=("times new roman", 12, "bold"))
        save_btn.grid(row=0, column=3)

        bttn_frame1 = Frame(class_student_frame, bg="white", bd=2, relief=RIDGE)
        bttn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn = Button(bttn_frame1,command=self.generate_dataset, bg="black", width=35, fg="white", text="Take Photo",
                          font=("times new roman", 12, "bold"))
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(bttn_frame1, bg="black", width=35, fg="white", text="Update Photo",
                                font=("times new roman", 12, "bold"))
        update_photo_btn.grid(row=0, column=1)

        # right frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=780,y=10, width=660, height=580)

        img_right = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\student.jpg")
        img_right = img_right.resize((740, 130), Image.ANTIALIAS)
        self.photo_right_img = ImageTk.PhotoImage(img_right)

        f_lbl2 = Label(right_frame, image=self.photo_right_img)
        f_lbl2.place(x=5, y=0, width=720, height=130)

        # >>>>>Search System frame

        class_search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        class_search_frame.place(x=5, y=135, width=700, height=70)



        search = Label(class_search_frame, bg="white", text="Search By",
                           font=("times new roman", 15, "bold"))
        search.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(class_search_frame, font=("times new roman", 12, "bold"), width=17, state="read only ")
        search_combo['values'] = ("Search By","Roll no","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10)

        # btn

        entry = ttk.Entry(class_search_frame, width=15, font=("times new roman", 12, "bold"))
        entry.grid(row=0, column=2, padx=10, pady=5)

        search_btn = Button(class_search_frame, bg="black", width=10, fg="white", text="Search",
                          font=("times new roman", 12, "bold"))
        search_btn.grid(row=0, column=3,padx=2)

        show_All = Button(class_search_frame, bg="black", width=10, fg="white", text="Show All",
                          font=("times new roman", 12, "bold"))
        show_All.grid(row=0, column=4,padx=2)

# +++++++++++++++++table frame

        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                )
        table_frame.place(x=5, y=210, width=660, height=350)

# +++++++++++++++++scroll bar
        scrollbary=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbarx=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.students_table=ttk.Treeview(table_frame,column=("Dep","name","course","year","sem","id","div","roll no","phone","gender","email","adress","photo"),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary)
        scrollbarx.pack(side=RIGHT,fill=X)
        scrollbary.pack(side=BOTTOM,fill=Y)

        scrollbarx.config(command=self.students_table.yview)
        scrollbary.config(command=self.students_table.xview)

        self.students_table.heading("Dep",text="Departnment")
        self.students_table.heading("name", text="Name")
        self.students_table.heading("course", text="Course")
        self.students_table.heading("year", text="Year")
        self.students_table.heading("sem", text="Semester")
        self.students_table.heading("id", text="Student_Id")
        self.students_table.heading("div", text="Divison")
        self.students_table.heading("roll no", text="Roll no")
        self.students_table.heading("phone", text="Phone")
        self.students_table.heading("email", text="Email")
        self.students_table.heading("gender", text="Gender")
        self.students_table.heading("adress", text="Adress")
        self.students_table.heading("photo", text="Photo")


        self.students_table["show"]="headings"

        self.students_table.column("Dep",width=100)
        self.students_table.column("name", width=100)
        self.students_table.column("course", width=100)
        self.students_table.column("sem", width=100)
        self.students_table.column("year", width=100)
        self.students_table.column("id", width=100)
        self.students_table.column("div", width=100)
        self.students_table.column("roll no", width=100)
        self.students_table.column("email", width=100)
        self.students_table.column("gender", width=100)
        self.students_table.column("adress", width=100)
        self.students_table.column("photo", width=100)



        self.students_table.pack(fill=BOTH,expand=1)
        self.students_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


        conn = _sqlite3.connect("app.db")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE  IF NOT EXISTS student (dep TEXT,Name TEXT,course TEXT,year TEXT,semester TEXT,student_id TEXT PRIMARY KEY,div INTEGER,roll TEXT,phone INTEGER,gender TEXT,email TEXT,adress TEXT,photo TEXT)")
        conn.commit()
        conn.close()





    # ++++++++++function declaration
    def add_data(self):


        if self.var_dep.get()=="Select departnment" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","Complete Every Information",parent=self.root)
        else:
           try:
                conn = _sqlite3.connect("app.db")
                curr = conn.cursor()
                curr.execute("insert into student Values(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                                                                     (self.var_dep.get(),
                                                                                      self.var_std_name.get(),
                                                                                      self.var_course.get(),
                                                                                      self.var_year.get(),
                                                                                      self.var_semester.get(),
                                                                                      self.var_std_id.get(),

                                                                                      self.var_div.get(),
                                                                                      self.var_roll.get(),

                                                                                      self.var_phone.get(),
                                                                                      self.var_gender.get(),
                                                                                      self.var_email.get(),

                                                                                      self.var_adress.get(),
                                                                                      self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Done","Saved",parent=self.root)

           except Exception as es:
               messagebox.showinfo("Error",f"{str(es)}",parent=self.root)

    # @@@@@@@@@@@fetch
    def fetch_data(self):
        conn = _sqlite3.connect("app.db")
        curr = conn.cursor()
        curr.execute("SELECT * FROM student")
        data = curr.fetchall()

        if len(data) != 0:
            self.students_table.delete(* self.students_table.get_children())
            for i in data:
                self.students_table.insert("",END,values=i)
            conn.commit()
        conn.close()


      # @@@@@@@@@@@@@@@@get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.students_table.focus()
        content=self.students_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_std_name.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_std_id.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_phone.set(data[8])
        self.var_gender.set(data[9])
        self.var_email.set(data[10])
        self.var_radio1.set(data[11])



    def update(self):
        if self.var_dep.get() == "Select departnment" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Complete Every Information", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to make changes",parent=self.root)
                if update>0:
                    conn = _sqlite3.connect("app.db")
                    curr = conn.cursor()
                    curr.execute("Update student set dep=?,Name=?,course=?,year=?,semester=?,div=?,roll=?,phone=?,gender=?,email=?,adress=?,photo=? where student_id=?",
                                 (self.var_dep.get(),
                                  self.var_std_name.get(),
                                  self.var_course.get(),
                                  self.var_year.get(),
                                  self.var_semester.get(),


                                  self.var_div.get(),
                                  self.var_roll.get(),

                                  self.var_phone.get(),
                                  self.var_gender.get(),
                                  self.var_email.get(),

                                  self.var_adress.get(),
                                  self.var_radio1.get(),
                                  self.var_std_id.get()
                                 ))

                    conn.commit()
                    conn.close()
                    self.fetch_data()



                else:
                    if not update:
                        return

                messagebox.showinfo("Sucess", "sucessfully updated", parent=self .root)

            except Exception as es:
                messagebox.showinfo("Error", f"{str(es)}", parent=self.root)


 # @@@@@@@@@@@@@@@@@delete
    def delete(self):
        if self.var_std_id.get()==" ":
            messagebox.showerror("Error","Student Id required")
        else:
            try:
                delete=messagebox.askyesno("Delete info","Do you want to delete this data")
                if delete>0:
                     conn = _sqlite3.connect("app.db")
                     curr = conn.cursor()
                     curr.execute("DELETE FROM student WHERE student_id=?",(self.var_std_id.get(),))

                     conn.commit()
                     conn.close()
                     messagebox.showinfo("Deleted","Removed the data")
                     self.fetch_data()

            except Exception as es:
                messagebox.showinfo("Error", f"{str(es)}", parent=self.root)


      # reset function
    def reset(self):
         self.var_dep.set("Select Departnment")
         self.var_std_name.set("")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select semester")
         self.var_std_id.set("")
         self.var_div.set("Select Div")
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_adress.set("")
         self.var_radio1.set("")


# @@@@@@@@@@@@@@@@@@ Generate data set @@@@@@@@@@@@@@@

    def generate_dataset(self):
        if self.var_dep.get() == "Select departnment" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Complete Every Information", parent=self.root)
        else:
            try:
                conn = _sqlite3.connect("app.db")
                curr = conn.cursor()
                curr.execute("Select * from student")
                myresult=curr.fetchall()
                id=0
                for x in myresult:
                    id+=1

                curr.execute(
                    "Update student set dep=?,Name=?,course=?,year=?,semester=?,div=?,roll=?,phone=?,gender=?,email=?,adress=?,photo=? where student_id=?",
                    (self.var_dep.get(),
                     self.var_std_name.get(),
                     self.var_course.get(),
                     self.var_year.get(),
                     self.var_semester.get(),

                     self.var_div.get(),
                     self.var_roll.get(),

                     self.var_phone.get(),
                     self.var_gender.get(),
                     self.var_email.get(),

                     self.var_adress.get(),
                     self.var_radio1.get(),
                     self.var_std_id.get()==id+1
                     ))

                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()


                # **************************Load predefined data on face frontal algo grom open cv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #sclaing factor=1.3
                    #Minimum Neighbor=5


                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
                        cv2.imshow("croppedFace",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Set Completed")



            except Exception as es:
                messagebox.showinfo("Error", f"{str(es)}", parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
