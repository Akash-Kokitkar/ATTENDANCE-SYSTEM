from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student_details import Student
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
from tkinter import messagebox
import os
import _sqlite3
import cv2
import numpy as np


class Face_recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognize")

        f_recognition = Label(self.root, bg="Red", text="Face Recognize", font=("times new roman", 35, "bold"))
        f_recognition.place(x=0, y=0, width=1530, height=45)

        img3 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\facialrecognition.png")
        img3 = img3.resize((950, 700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=55, width=950, height=700)

        img4 = Image.open(
            r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img4 = img4.resize((950, 700), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=650, y=55, width=950, height=700)

        # button

        b1 = Button(bg_img, text="Face Recognition", command=self.face_recognition, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="dark green", fg="white")
        b1.place(x=380, y=620, width=200, height=40)

        # +++++++++++++++++++Attendanc++++++++++++++++++++++++++++
    def mark_attendance(self,i,r,d,n):
        with open("attendances.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (d not in name_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m%Y")
                dtString=now.strftime("%H:%M:{%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")













    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = _sqlite3.connect("app.db")
                cur = conn.cursor()
                cur.execute(
                    "select Name From student where student_id="+str(id))

                n=cur.fetchone()
                n="+".join(n)

                cur.execute(
                    "select dep From student where student_id="+str(id))

                d=cur.fetchone()
                d="+".join(d)

                cur.execute(
                    "select student_id From student where student_id="+ str(id))

                i = cur.fetchone()
                i = "+".join(i)

                cur.execute(
                    "select roll From student where student_id=" + str(id))

                r = cur.fetchone()
                r = "+".join(r)

                if confidence>77:
                    cv2.putText(img, f"Student_id:{i}", (x, y-105), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"RollNO:{r}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img,f"Departnment:{d}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255),3)
                    self.mark_attendance(i,r,d,n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face", (x, y- 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)


                coord=[x,y,w,h]

            return coord

        def recognize(img,clg,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detection",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()
