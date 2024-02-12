from tkinter import *
import customtkinter as ctk
from PIL import ImageTk,Image
from tkinter import messagebox

class admin_code:
    def __init__(self,admin_window) :
        self.admin_window=admin_window
        self.admin_window.geometry('1600x900')
        self.admin_window.title('Admin Code')
        self.admin_img=Image.open('Travel-Management-System/User_Authentication/images/admin_code_bg.jpg')
        self.admin_resize=self.admin_img.resize((1600,900))
        self.admin_con=ImageTk.PhotoImage(self.admin_resize)
        self.admin_label=Label(self.admin_window,image=self.admin_con).place(x=0,y=0)


        self.frame=ctk.CTkFrame(self.admin_window,fg_color='#5B5858',width=400,height=300,bg_color='transparent')
        self.frame.place(x=550,y=200)

        self.code_label=ctk.CTkLabel(self.admin_window,text='Enter your Admin code',font=('Aerial',30),fg_color='#5B5858').place(x=610,y=230)
        self.code_entry=ctk.CTkEntry(self.admin_window,fg_color='white',bg_color='#5B5858',text_color='black',width=200,height=40)
        self.code_entry.place(x=650,y=290)

        self.next_btn=ctk.CTkButton(self.admin_window,text='Next',fg_color='white',text_color='black',bg_color='#5B5858').place(x=680,y=390)

        self.arrow_btn=ctk.CTkButton(self.admin_window,text='←',width=20,fg_color='#5B5858',bg_color='#5B5858').place(x=560,y=210)

        def hide():
           self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/closeye.png')
           self.code_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/openeye.png')
            self.code_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='Travel-Management-System/User_Authentication/images/openeye.png')
        self.open_btn=Button(self.admin_window,image=self.open_eye,bg='white',bd=0,width=30,height=35,cursor='hand',command=hide)
        self.open_btn.place(x=820,y=290)
       

        


if __name__ == "__main__":    
    root = Tk()
    obj = admin_code(root)
    root.mainloop()