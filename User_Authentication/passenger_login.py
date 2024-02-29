from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import sys

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Passenger_Login():
    def __init__(self,window):
        self.window_login_type = window
        self.window_login_type.geometry("1465x740+0+0")
        self.window_login_type.title("Logintype")
        self.window_login_type.minsize(1465, 750)
        self.window_login_type.iconbitmap("System_Images/title_logo.ico")

        #background_img
        bg = Image.open("User_Authentication/images/login_bg.jpg")
        resize_bg = bg.resize((1536,785))
        self.bg_image = ImageTk.PhotoImage(resize_bg)
        bg_label = Label(self.window_login_type,image=self.bg_image)
        bg_label.place(x=0,y=0,width=1536,height=785)

        #self.login_frame
        self.login_frame = Frame(self.window_login_type,bd=5,bg="gray38")
        self.login_frame.place(x=600,y=140,width=400,height=500)

        # login_logo_top
        logo = Image.open("User_Authentication/images/login_logo.png")
        resize_logo = logo.resize((100,100))
        self.logo_image = ImageTk.PhotoImage(resize_logo)
        Label(self.login_frame,image=self.logo_image,bg="gray38").place(x=140,y=10,width=100,height=100)
        
        #labels
        Label(self.login_frame,text="Login",bg="gray38",fg="white",font=("Arial",20,"bold")).place(x=150,y=110)

        # username
        self.passenger_username = StringVar()
        Label(self.login_frame,text="Username",bg="gray38",fg="white",font=("Arial",16,"bold")).place(x=110,y=160)
        user_logo = Image.open("User_Authentication/images/username_logo.png")
        resize_user_logo = user_logo.resize((30,30))
        self.user_logo_image = ImageTk.PhotoImage(resize_user_logo)
        Label(self.login_frame,image=self.user_logo_image,bg="gray38").place(x=70,y=155)
        self.username_entry = ctk.CTkEntry(self.login_frame,textvariable=self.passenger_username,width=250,font=("Arial",20,"bold"),corner_radius=20, height=35)
        self.username_entry.place(x=70,y=195)

        #password
        self.passenger_password = StringVar()
        Label(self.login_frame,text="Password",bg="gray38",fg="white",font=("Arial",16,"bold")).place(x=110,y=250)
        p_logo = Image.open("User_Authentication/images/password_logo.png")
        resize_p_logo = p_logo.resize((30,30))
        self.p_logo_image = ImageTk.PhotoImage(resize_p_logo)
        Label(self.login_frame,image=self.p_logo_image,bg="gray38").place(x=70,y=245)
        self.password_entry = ctk.CTkEntry(self.login_frame, textvariable=self.passenger_password, show = "*",width=250,font=("Arial",20,"bold"),corner_radius=20, height=35)
        self.password_entry.place(x=70,y=280)
        def show_password():
            if checkbox_var.get() == 1:  # If checkbox is checked
                self.password_entry.configure(show='')  # Show the password
            else:
                self.password_entry.configure(show='*')  # Hide the password

        checkbox_var = IntVar()
        check_button = ctk.CTkCheckBox(self.login_frame,text="show password",variable=checkbox_var,command=show_password,checkmark_color="black",bg_color="gray38",fg_color="white",text_color="white",hover = FALSE,font=("Arial",14,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20,cursor="hand2")
        check_button.place(x=80,y=320)

        # login_button
        login_button = ctk.CTkButton(self.login_frame,text="Login",bg_color="gray38",width=100,fg_color="white",text_color="black",font=("Arial",12,"bold"),corner_radius=20,cursor="hand2", command=self.authentication)
        login_button.place(x=150,y=355)

        create_button = Button(self.login_frame,text="Create new account?",fg="white",bg="gray38",bd=0,font=("times new roman",10,"bold"), cursor="hand2", command=self.passenger_create_account_func)
        create_button.place(x=70,y=395)
        forget_button = Button(self.login_frame,text="Forget password?",fg="white",bg="gray38",bd=0,font=("times new roman",10,"bold"), cursor="hand2", command=self.forget_condition)
        forget_button.place(x=70,y=420)
    

    def authentication(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" and password == "":
            messagebox.showerror("Error","Fill all the details", parent=self.window_login_type)
        else:
            try:
                Connection = mysql.connector.connect(
                    host = "localhost",
                    username = "root",
                    password = "Root@123",
                    database = "travel_ms_db"               
                  )
                my_cursor = Connection.cursor()
                quary1 = "select * from passenger_details where (username = %s or email = %s) and new_password = %s"
                values1 = (username ,username, password)
                my_cursor.execute(quary1,values1)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error","Invalid Username or Password", parent=self.window_login_type)
                else:
                    
                    self.new_window2 = Toplevel(self.window_login_type)
                    sys.path.append(r"C:\Users\subha\.vscode\Travel_MS_Project\Passenger_System")
                    from passenger_dashboard import Travel 
                    self.passenger_dash_obj = Travel(self.new_window2)

                    # Set the account data for account_section
                    self.passenger_dash_obj.dashboard_section_fname_var.set(row[1])
                    self.passenger_dash_obj.dashboard_section_lname_var.set(row[2])
                    self.passenger_dash_obj.dashboard_section_username_var.set(row[3])
                    self.passenger_dash_obj.dashboard_section_contact_var.set(row[5])
                    self.passenger_dash_obj.dashboard_section_email_var.set(row[6])
                    self.passenger_dash_obj.dashboard_section_password_var.set(row[9])
                    self.passenger_dash_obj.dashboard_section_confirm_password_var.set(row[9])

                    self.passenger_username.set("")
                    self.passenger_password.set("")

                    
                    Connection.commit()
            except Exception as e:
                messagebox.showerror("Error",f"An error occurd: {str(e)}", parent=self.window_login_type)
            finally:
                if Connection.is_connected():
                    Connection.close()
                    my_cursor.close()


    def forget_condition(self):
        username = self.username_entry.get()

        if username == "":
            messagebox.showerror("Error","Enter username", parent=self.window_login_type)
        else:
            try:
                Connection = mysql.connector.connect(
                    host = "localhost",
                    username = "root",
                    password = "Root@123",
                    database = "travel_ms_db"               
                  )
                my_cursor = Connection.cursor()
                quary1 = "select * from passenger_details where username = %s or email = %s"
                values1 = (username, username)
                my_cursor.execute(quary1,values1)
                row = my_cursor.fetchone()
                
                if row is None:
                    messagebox.showerror("Error","Invalid Username", parent=self.window_login_type)
                else:
                    from Passenger_forget_password import forget_password
                    new_window = Toplevel(self.window_login_type)
                    obj = forget_password(new_window)

                Connection.commit()
            except Exception as e:
                messagebox.showerror("Error",f"An error occured: {str(e)}", parent=self.window_login_type)
            
            finally:
                if Connection.is_connected():
                    Connection.close()
                    my_cursor.close()



    def passenger_create_account_func(self):
        new_window = Toplevel()
        from passenger_register import register_type
        obj = register_type(new_window)

    

if __name__ == "__main__":
    root = Tk()
    obj = Passenger_Login(root)
    root.mainloop()