

#pip install google_trans_new
from tkinter import * #import tat ca nhung thu can thiet cua tkint er
from PIL import Image, ImageTk #PIL giup minh chen anh vao
from googletrans import Translator #import Translator de dich

#tao man hinh Tkinter Window  
root = Tk()
root.title('Google Galaxy') #Tieu de
root.geometry("500x630") #kich thuoc
root.iconbitmap('img+font/logo.ico') #chen logo

load = Image.open('img+font/background.png') #chen background
render = ImageTk.PhotoImage(load) #xuat hinh anh background
img = Label(root, image=render) #giup hien thi hinh anh va van ban
img.place(x=0,y=0) #dat len man hinh (x=0,y=0 la goc toa do)

name = Label(root, text="Translator", fg="#FFFFFF", bd = 0, bg = "#03152D") #text= chu hien thi, fg xet mau, bd la vien, bg la xet mau backgroun d
name.config(font=("Transformer Movie", 30))#Xet font cua chu
name.pack(pady=10)#hien thi len man hinh 

box = Text(root, width=28,height=8,font=("ROBOTO", 16)) #Tao text box de dien
box.pack(pady=20)
button_frame= Frame(root).pack(side=BOTTOM) #tao khung

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT = box.get(1.0,END)
    print(INPUT)
    #t=Translator()
    a=Translator().translate(INPUT, src="vi",dest="en")
    b=a.text
    box1.insert(END,b)
clear_button = Button(button_frame, text="Clear text", font=(("Arial"),10, 'bold'),bg='#303030', fg='#FFFFFF',command=clear)
clear_button.place(x=150,y=310)
trans_button = Button(button_frame, text="Translate", font=(("Arial"),10, 'bold'),bg='#303030', fg='#FFFFFF',command=translate)
trans_button.place(x=  290,y=310)
box1 = Text(root, width=28,height=8,font=("ROBOTO", 16)) #Tao text box1 de dien
box1.pack(pady=50)


root.mainloop() #tao vong lap de hien thi cua so
