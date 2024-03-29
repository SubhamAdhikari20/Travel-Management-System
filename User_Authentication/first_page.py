from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class FirstPage:
    def __init__(self, first_window):
        self.first_window = first_window
        self.first_window.geometry('1465x740+0+0')
        self.first_window.title('YATRU TRAVELS')
        self.first_window.minsize(1465, 740)
        self.first_window.iconbitmap("System_Images/title_logo.ico")

        global win
        win = self.first_window

        # backgroung Image
        self.bg_img = Image.open('User_Authentication/images/1 copy.png')  # Update the path
        self.bg_img_resize = self.bg_img.resize((1465, 750))
        self.bg_con = ImageTk.PhotoImage(self.bg_img_resize)
        self.bg_label = Label(self.first_window, image=self.bg_con)
        self.bg_label.place(x=0, y=0)

        # login and sign up Button
        self.login_btn = ctk.CTkButton(self.first_window, text='Login', fg_color='#373737', font=('Arial', 15),corner_radius=20, width=110, height=50, command=self.login)
        self.login_btn.place(x=1150, y=20)

        self.signup_btn = ctk.CTkButton(self.first_window, text='Sign up', fg_color='#373737', font=('Arial', 15), corner_radius=20, width=110, height=50, command=self.sign)
        self.signup_btn.place(x=1300, y=20)

    def login(self):
        self.login_btn.destroy()
        self.signup_btn.destroy()
        if hasattr(self, "sign_frame") and self.sign_frame.winfo_exists():
            self.sign_frame.destroy()

        # Frame
        self.login_frame = ctk.CTkFrame(self.first_window, fg_color='#5B5858', width=500, height=400, bg_color='transparent', corner_radius=1)
        self.login_frame.place(x=500, y=200)

        # labels
        self.login_label = ctk.CTkLabel(self.login_frame, text='Login', bg_color='#5B5858', fg_color='#5B5858',text_color='white', font=('Arial', 35))
        self.login_label.place(x=210, y=10)
        ctk.CTkLabel(self.login_frame, text='Which type of account do you', bg_color='#5B5858', fg_color='#5B5858',text_color='white', height=2).place(x=170, y=70)
        ctk.CTkLabel(self.login_frame, text='want to login to?', bg_color='#5B5858', fg_color='#5B5858', height=10,text_color='white').place(x=195, y=95)


        # admin and passenger Button
        self.login_passenger_btn = ctk.CTkButton(self.login_frame, text='Passenger', fg_color='#319BA9', bg_color='#5B5858', text_color='white', font=('Arial', 18),corner_radius=40, height=70, width=250,command=self.passenger_login_func)
        self.login_passenger_btn.place(x=125, y=130)

        self.login_admin_btn = ctk.CTkButton(self.login_frame, text='Admin', fg_color='#319BA9', bg_color='#5B5858',text_color='white', corner_radius=40, font=('Arial', 18), width=250,height=70, command=self.admin_login)
        self.login_admin_btn.place(x=125, y=210)
 
        # create and arrowButton
        ctk.CTkLabel(self.login_frame, text='Do not have an account?', bg_color='#5B5858', fg_color='#5B5858', text_color='white').place(x=180, y=310)
        ctk.CTkButton(self.login_frame, text='Create Account', bg_color='#5B5858', fg_color='white',text_color='black',command=self.sign).place(x=180, y=350)

        ctk.CTkButton(self.login_frame, text='←', width=20, fg_color='#5B5858', bg_color='#5B5858',command=self.go_back_from_login_frame).place(x=10, y=10)

    def sign(self):
        self.signup_btn.destroy()
        self.login_btn.destroy()
        if hasattr(self, "login_frame") and self.login_frame.winfo_exists():
            self.login_frame.destroy()

        # Frame
        self.sign_frame = ctk.CTkFrame(self.first_window, fg_color='#5B5858', width=500, height=400, bg_color='transparent', corner_radius=1)
        self.sign_frame.place(x=500, y=200)

        # Label
        self.sign_label = ctk.CTkLabel(self.sign_frame, text='Sign up', bg_color='#5B5858', fg_color='#5B5858',text_color='white', font=('Arial', 35))
        self.sign_label.place(x=190, y=10)
        ctk.CTkLabel(self.sign_frame, text='Which type of account do you', bg_color='#5B5858', fg_color='#5B5858',text_color='white', height=2).place(x=170, y=70)
        ctk.CTkLabel(self.sign_frame, text='want to sign in to?', bg_color='#5B5858', fg_color='#5B5858', height=10,text_color='white').place(x=210, y=95)
        
        # passenger and admin button
        self.sign_passenger = ctk.CTkButton(self.sign_frame, text='Passenger', fg_color='#319BA9', bg_color='#5B5858', text_color='white', font=('Arial', 18),corner_radius=40, height=70, width=250,command=self.passenger_register_func)
        self.sign_passenger.place(x=125, y=130)
        self.sign_admin_btn= ctk.CTkButton(self.sign_frame, text='Admin', fg_color='#319BA9', bg_color='#5B5858',text_color='white', corner_radius=40, font=('Arial', 18), width=250,height=70,command=self.code_admin)
        self.sign_admin_btn.place(x=125, y=210)

        ctk.CTkLabel(self.sign_frame, text='Already have an account?', bg_color='#5B5858', fg_color='#5B5858',text_color='white').place(x=175, y=310)
        ctk.CTkButton(self.sign_frame, text='Login', bg_color='#5B5858', fg_color='white',text_color='black', command=self.login).place(x=180, y=350)
        ctk.CTkButton(self.sign_frame, text='←', width=20, fg_color='#5B5858', bg_color='#5B5858',command=self.go_back_from_signin_frame).place(x=10, y=10)


    def go_back_from_login_frame(self):
        self.login_frame.destroy()
        self.login_btn = ctk.CTkButton(self.first_window, text='Login', fg_color='#373737', font=('Arial', 15),corner_radius=20, width=110, height=50, command=self.login)
        self.login_btn.place(x=1150, y=20)

        self.signup_btn = ctk.CTkButton(self.first_window, text='Sign up', fg_color='#373737', font=('Arial', 15), corner_radius=20, width=110, height=50, command=self.sign)
        self.signup_btn.place(x=1300, y=20)


    def go_back_from_signin_frame(self):
        self.sign_frame.destroy()
        self.login_btn = ctk.CTkButton(self.first_window, text='Login', fg_color='#373737', font=('Arial', 15),corner_radius=20, width=110, height=50, command=self.login)
        self.login_btn.place(x=1150, y=20)

        self.signup_btn = ctk.CTkButton(self.first_window, text='Sign up', fg_color='#373737', font=('Arial', 15), corner_radius=20, width=110, height=50, command=self.sign)
        self.signup_btn.place(x=1300, y=20)


    def admin_login(self):
        new=Toplevel(self.first_window)
        from admin_login import Admin_login
        obj=Admin_login(new)

    def code_admin(self):
        new=Toplevel(self.first_window)
        from admin_code import admin_code
        obj=admin_code(new)

    
    def passenger_login_func(self):
        new_window = Toplevel(self.first_window)
        from passenger_login import Passenger_Login 
        obj = Passenger_Login(new_window)

        
    def passenger_register_func(self):
        new_window = Toplevel(self.first_window)
        from passenger_register import register_type
        obj = register_type(new_window)


        
if __name__ == "__main__":
    root = Tk()
    first_window_obj = FirstPage(root)
    root.mainloop()
