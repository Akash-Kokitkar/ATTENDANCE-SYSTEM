
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_details import Student
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np


class Train:


    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train_Data")

        f_title_lbl = Label(self.root, bg="Black",fg="RED",text="Train_Data_System ", font=("times new roman", 35, "bold"))
        f_title_lbl.place(x=0, y=0, width=1530, height=45)


        img1=Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\facialrecognition.png")
        img1=img1.resize((1530,325),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=0,y=55,width=1530,height=325)

        img2 = Image.open(r"C:\Users\AKASH\tkinters\QR ATTENDANCE\clg_img\facialrecognition.png")
        img2 = img2.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=440, width=1530, height=325)

        b1 = Button(self.root, bg="Blue",command=self.train_classifier,text="Train DATA", cursor="hand2", font=("times new roman", 35, "bold"))
        b1.place(x=0, y=380, width=1530, height=60)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

     # @@@@@@@@@@@@@@@@@Train Classifier@@@@@@@@@@@@@@@@@@@@

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Done","Training Done")









if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

