from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
from admin_code import admin_code


class Admin_login():
    def __init__(self,window):
        self.window_login_type = window
        self.window_login_type.geometry('1440x900+0+0')
        self.window_login_type.title("Admin Login")
        
        bg = Image.open("Travel-Management-System/User_Authentication/images/login_bg.jpg")
        resize_bg = bg.resize((1440,900))
        self.window_login_type.resizable(0,0)

        self.bg_image = ImageTk.PhotoImage(resize_bg)
        bg_label = Label(self.window_login_type,image=self.bg_image)
        bg_label.place(x=0,y=0)

        login_frame = Frame(self.window_login_type,bd=5,bg="gray38")
        login_frame.place(x=520, y=150, width=400, height=500)

        logo = Image.open("Travel-Management-System/User_Authentication/images/login_logo.png")
        resize_logo = logo.resize((100,100))
        self.logo_image = ImageTk.PhotoImage(resize_logo)
        Label(login_frame,image=self.logo_image,bg="gray38").place(x=150,y=10,width=100,height=100)
        
        Label(login_frame,text="Admin Login",bg="gray38",fg="white",font=("arial",25,"bold")).place(x=120,y=120)

        Label(login_frame,text="Username",bg="gray38",fg="white",font=("arial",20,"bold")).place(x=95,y=185)

        user_logo = Image.open("Travel-Management-System/User_Authentication/images/username_logo.png")
        resize_user_logo = user_logo.resize((20,20))
        self.user_logo_image = ImageTk.PhotoImage(resize_user_logo)
        Label(login_frame,image=self.user_logo_image,bg="gray38").place(x=70,y=190)

        self.username_entry = Entry(login_frame,textvariable=StringVar,width=25,font=("arial",16,"bold"),fg='black',bg='white')
        self.username_entry.place(x=70,y=220)

        Label(login_frame,text="Password",bg="gray38",fg="white",font=("arial",20,"bold")).place(x=95,y=260)
        
        p_logo = Image.open("Travel-Management-System/User_Authentication/images/password_logo.png")
        resize_p_logo = p_logo.resize((20,20))
        self.p_logo_image = ImageTk.PhotoImage(resize_p_logo)
        Label(login_frame,image=self.p_logo_image,bg="gray38").place(x=70,y=263)

        self.password_entry = Entry(login_frame,textvariable=StringVar,width=25,bg='white',fg='black',font=("arial",16,"bold"))
        self.password_entry.place(x=70,y=290)

        def hide():
           self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/closeye.png')
           self.password_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/openeye.png')
            self.password_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='Travel-Management-System/User_Authentication/images/openeye.png')
        self.open_btn=Button(login_frame,image=self.open_eye,bg='white',bd=0,height=22,cursor='hand',command=hide)
        self.open_btn.place(x=278,y=292)



        # login Button
        login_button = ctk.CTkButton(login_frame,text="Login",text_color='black',fg_color="white", font=("arial",12,"bold"))
        login_button.place(x=120,y=340)

        # creating and forgot Button
        self.new_acc_btn=ctk.CTkButton(login_frame,text="Create new account?",text_color="white",fg_color="gray38",font=("times new roman",15,"bold"),command=self.code).place(x=40,y=410)

        self.forgot_pass_btn=ctk.CTkButton(login_frame,text="Forgot password?",text_color="white",fg_color="gray38",font=("times new roman",15,"bold")).place(x=40,y=440)

    def code(self):  
        signin=Toplevel()
        obj=admin_code(signin)
        self.window_login_type.destroy()

    

if __name__ == "__main__":    
    root = Tk()
    obj = Admin_login(root)
    root.mainloop()