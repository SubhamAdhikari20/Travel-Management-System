from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector as mysql
import admin_forgot_pas
import sys

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Admin_login():
    def __init__(self,window):
        self.window_login_type = window
        self.window_login_type.geometry('1465x740+0+0')
        self.window_login_type.title("Admin Login")
        self.window_login_type.minsize(1465,740)
        self.window_login_type.iconbitmap("System_Images/title_logo.ico")
        
        bg = Image.open("User_Authentication/images/login_bg.jpg")
        resize_bg = bg.resize((1465,750))
        self.bg_image = ImageTk.PhotoImage(resize_bg)
        bg_label = Label(self.window_login_type,image=self.bg_image)
        bg_label.place(x=0,y=0)

        login_frame = Frame(self.window_login_type,bd=5,bg="gray38")
        login_frame.place(x=520, y=150, width=400, height=500)

        logo = Image.open("User_Authentication/images/login_logo.png")
        resize_logo = logo.resize((100,100))
        self.logo_image = ImageTk.PhotoImage(resize_logo)
        Label(login_frame,image=self.logo_image,bg="gray38").place(x=150,y=10,width=100,height=100)
        

        Label(login_frame,text="Admin Login",bg="gray38",fg="white",font=("Arial",20,"bold")).place(x=105,y=120)
        Label(login_frame,text="Username",bg="gray38",fg="white",font=("Arial",15,"bold")).place(x=95,y=185)
        
        user_logo = Image.open("User_Authentication/images/username_logo.png")
        resize_user_logo = user_logo.resize((20,20))
        self.user_logo_image = ImageTk.PhotoImage(resize_user_logo)
        Label(login_frame,image=self.user_logo_image,bg="gray38").place(x=70,y=190)
        
        self.admin_username = StringVar()
        self.username_entry = Entry(login_frame,textvariable=self.admin_username,width=25,font=("Arial",14,"bold"),fg='black',bg='white')
        self.username_entry.place(x=70,y=220, width=250, height=30)

        Label(login_frame,text="Password",bg="gray38",fg="white",font=("Arial",15,"bold")).place(x=95,y=260)
    
        p_logo = Image.open("User_Authentication/images/password_logo.png")
        resize_p_logo = p_logo.resize((20,20))
        self.p_logo_image = ImageTk.PhotoImage(resize_p_logo)
        Label(login_frame,image=self.p_logo_image,bg="gray38").place(x=70,y=263)

        self.admin_password = StringVar()
        self.password_entry = Entry(login_frame,textvariable=self.admin_password,width=25,bg='white',fg='black',font=("Arial",14,"bold"), show="*")
        self.password_entry.place(x=70,y=290, width=250, height=30)

        def hide():
           self.open_eye.configure(file='User_Authentication/images/closeye.png')
           self.password_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='User_Authentication/images/openeye.png')
            self.password_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='User_Authentication/images/closeye.png')
        self.open_btn=Button(login_frame,image=self.open_eye,bg='white',bd=0,height=22,cursor='hand2',command=show)
        self.open_btn.place(x=287,y=292)

        # login Button
        login_button = ctk.CTkButton(login_frame,text="Login",text_color='black',fg_color="white", font=("Arial",12,"bold"), command=self.login_btn_func)
  
        # creating and forgot Button
        self.new_acc_btn=ctk.CTkButton(login_frame,text="Create new account?",text_color="white",fg_color="gray38",font=("times new roman",15,"bold"),command=self.code).place(x=40,y=410)

        self.forgot_pass_btn=ctk.CTkButton(login_frame,text="Forgot password?",text_color="white",fg_color="gray38",font=("times new roman",15,"bold"),command=self.forgot).place(x=40,y=440)

    def code(self):  
        signin=Toplevel()
        from admin_code import admin_code
        obj=admin_code(signin)

    def forgot(self):
        forgot=Toplevel(self.window_login_type)
        obj=admin_forgot_pas.admin_forgot(forgot)

    def login_btn_func(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username==''or password=='':
            messagebox.showerror('ERROR','Enter all details', parent = self.window_login_type)
          
        else:
            try:
                connection=mysql.connect(
                    host='localhost',
                    username='root',
                    password="Root@123",
                    database='travel_ms_db'
                )
                cursor=connection.cursor()
                query="select * from admin_details where (email = %s or username = %s) and new_password = %s"
                values=(username, username, password)
                cursor.execute(query,values)
                row=cursor.fetchone()
                if row is None:
                    messagebox.showerror('ERROR','Invalid username or password!!', parent = self.window_login_type)
                else:
                    open_main = messagebox.askyesno("Yes NO", "Access only by admin?", parent=self.window_login_type)
                    if open_main == 1:
                        self.new_window2 = Toplevel()
                        sys.path.append(r"C:\Users\subha\.vscode\Travel_MS_Project\Admin_System")
                        from admin_dashboard import Travel 
                        self.admin_dash_obj = Travel(self.new_window2)

                        # Set the account data for account_section  
                        self.admin_dash_obj.dashboard_section_fname_var.set(row[1])
                        self.admin_dash_obj.dashboard_section_lname_var.set(row[2])
                        self.admin_dash_obj.dashboard_section_username_var.set(row[3])
                        self.admin_dash_obj.dashboard_section_contact_var.set(row[5])
                        self.admin_dash_obj.dashboard_section_email_var.set(row[6])
                        self.admin_dash_obj.dashboard_section_password_var.set(row[9])
                        self.admin_dash_obj.dashboard_section_confirm_password_var.set(row[9])

                        # self.window_login_type.destroy()
                        self.admin_username.set("")
                        self.admin_password.set("")

            except Exception as e:
                messagebox.showerror("Error",f"an error occured: {str(e)}", parent = self.window_login_type)

            finally:
                if connection.is_connected():
                    connection.close()  

    

if __name__ == "__main__":    
    root = Tk()
    obj = Admin_login(root)
    root.mainloop()