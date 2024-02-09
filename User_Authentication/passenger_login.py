from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import customtkinter as ctk

class Passenger_Login():
    def __init__(self,window):
        self.window_login_type = window
        self.window_login_type.geometry("1536x785+0+0")
        self.window_login_type.title("Logintype")

        #background_img
        bg = Image.open("Travel-Management-System/User_Authentication/images/login_bg.jpg")
        resize_bg = bg.resize((1536,785))
        self.bg_image = ImageTk.PhotoImage(resize_bg)
        bg_label = Label(self.window_login_type,image=self.bg_image)
        bg_label.place(x=0,y=0,width=1536,height=785)

        #self.login_frame
        self.login_frame = Frame(self.window_login_type,bd=5,bg="gray38")
        self.login_frame.place(x=600,y=140,width=400,height=500)

        # login_logo_top
        logo = Image.open("Travel-Management-System/User_Authentication/images/login_logo.png")
        resize_logo = logo.resize((100,100))
        self.logo_image = ImageTk.PhotoImage(resize_logo)
        Label(self.login_frame,image=self.logo_image,bg="gray38").place(x=150,y=20,width=100,height=100)
        
        #labels
        Label(self.login_frame,text="Login",bg="gray38",fg="white",font=("arial",12,"bold")).place(x=175,y=125)

        # username
        Label(self.login_frame,text="Username",bg="gray38",fg="white",font=("arial",16,"bold")).place(x=110,y=160)
        user_logo = Image.open("Travel-Management-System/User_Authentication/images/username_logo.png")
        resize_user_logo = user_logo.resize((30,30))
        self.user_logo_image = ImageTk.PhotoImage(resize_user_logo)
        Label(self.login_frame,image=self.user_logo_image,bg="gray38").place(x=70,y=155)
        self.username_entry = ctk.CTkEntry(self.login_frame,textvariable=StringVar(),width=250,font=("arial",24,"bold"),corner_radius=20)
        self.username_entry.place(x=70,y=195)

        #password
        Label(self.login_frame,text="Password",bg="gray38",fg="white",font=("arial",16,"bold")).place(x=110,y=250)
        p_logo = Image.open("Travel-Management-System/User_Authentication/images/password_logo.png")
        resize_p_logo = p_logo.resize((30,30))
        self.p_logo_image = ImageTk.PhotoImage(resize_p_logo)
        Label(self.login_frame,image=self.p_logo_image,bg="gray38").place(x=70,y=245)
        self.password_entry = ctk.CTkEntry(self.login_frame,textvariable=StringVar(),show = "*",width=250,font=("arial",24,"bold"),corner_radius=20)
        self.password_entry.place(x=70,y=280)
        def show_password():
            if checkbox_var.get() == 1:  # If checkbox is checked
                self.password_entry.configure(show='')  # Show the password
            else:
                self.password_entry.configure(show='*')  # Hide the password

        checkbox_var = IntVar()
        check_button = ctk.CTkCheckBox(self.login_frame,text="show password",variable=checkbox_var,command=show_password,checkmark_color="black",bg_color="gray38",fg_color="white",text_color="white",hover = FALSE,font=("Arial",14,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20)
        check_button.place(x=80,y=320)

        # login_button
        login_button = ctk.CTkButton(self.login_frame,text="Login",bg_color="gray38",width=100,fg_color="white",text_color="black",font=("arial",12,"bold"),corner_radius=20)
        login_button.place(x=150,y=355)

        create_button = Button(self.login_frame,text="Create new account?",fg="white",bg="gray38",bd=0,font=("times new roman",10,"bold"))
        create_button.place(x=70,y=395)
        forget_button = Button(self.login_frame,text="Forget password?",fg="white",bg="gray38",bd=0,font=("times new roman",10,"bold"))
        forget_button.place(x=70,y=420)
    
if __name__ == "__main__":
    root = Tk()
    obj = Passenger_Login(root)
    root.mainloop()