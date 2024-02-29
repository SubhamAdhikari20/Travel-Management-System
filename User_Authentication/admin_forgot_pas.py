from tkinter import*
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class admin_forgot:
    def __init__(self,forgot_window):
        self.forgot_window   =forgot_window
        self.forgot_window.geometry('1465x740+0+0')
        self.forgot_window.title('Forgot Password') 
        self.forgot_window.iconbitmap("System_Images/title_logo.ico")
   

        self.bg_img=Image.open('User_Authentication/images/forget_password.jpg')
        self.bg_resize=self.bg_img.resize((1465,750))
        self.bg_con=ImageTk.PhotoImage(self.bg_resize)
        self.bg_label=Label(self.forgot_window,image=self.bg_con)
        self.bg_label.place(x=0,y=0)

        self.frame=ctk.CTkFrame(self.forgot_window,fg_color='#5B5858',width=400,height=560,bg_color='transparent')
        self.frame.place(x=510,y=150)
        
        # admin Label
        self.ad_label=ctk.CTkLabel(self.forgot_window,text='Admin',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',25, "bold"))
        self.ad_label.place(x=680,y=160)
        self.label=ctk.CTkLabel(self.forgot_window,text='Forgot password?',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',20, "bold"))
        self.label.place(x=640,y=200)

        # username/email
        self.username_label=ctk.CTkLabel(self.forgot_window,text='Username/Email',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',15, "bold")).place(x=600,y=240)
        self.user_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Arial',15, "bold"))
        self.user_entry.place(x=600,y=270, width=222, height=30)

        # security Question
        self.sec_ques=ctk.CTkLabel(self.forgot_window,text='Security Question',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',15, "bold"))
        self.sec_ques.place(x=600,y=320)
        self.security_qn_combo_box = ttk.Combobox(self.forgot_window, font=("Arial", 15, "bold"), state="readonly",width=18,background='#5B5858')
        self.security_qn_combo_box["values"] = ("Select", "Favorite movie")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=600, y=350, width=222, height=30)


        # security Answer
        self.sec_ans=ctk.CTkLabel(self.forgot_window,text='Security Answer',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',1, "bold"))
        self.sec_ans.place(x=600,y=400)
        self.ans_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Arial',15, "bold"))
        self.ans_entry.place(x=600,y=430, width=222, height=30)

        # reset password
        self.reset_label=ctk.CTkLabel(self.forgot_window,text='Reset Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',15, "bold"))
        self.reset_label.place(x=600,y=480)
        self.reset_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Arial',14, "bold"), show="*")
        self.reset_entry.place(x=600,y=510, width=222, height=30)

        def hide():
           self.open_eye.configure(file='User_Authentication/images/closeye.png')
           self.reset_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='User_Authentication/images/openeye.png')
            self.reset_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='User_Authentication/images/closeye.png')
        self.open_btn=Button(self.forgot_window,image=self.open_eye,bg='white',bd=0,height=24,cursor='hand2',command=show)
        self.open_btn.place(x=790,y=511)

    # confirm password
        self.confirm=ctk.CTkLabel(self.forgot_window,text='Comfirm Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Arial',15, "bold"))
        self.confirm.place(x=600,y=560)
        self.con_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Arial',14, "bold"), show="*")
        self.con_entry.place(x=600,y=590, width=222, height=30)


        def hide1():
           self.open_eye1.configure(file='User_Authentication/images/closeye.png')
           self.con_entry.configure(show='*')
           self.open_btn1.configure(command=show1)
        def show1():
            self.open_eye1.configure(file='User_Authentication/images/openeye.png')
            self.con_entry.configure(show='')
            self.open_btn1.configure(command=hide1)
            
        self.open_eye1=PhotoImage(file='User_Authentication/images/closeye.png')
        self.open_btn1=Button(self.forgot_window,image=self.open_eye1,bg='white',bd=0,height=24,cursor='hand2',command=show1)
        self.open_btn1.place(x=790,y=591)
        


    # reset Button
        self.reset_btn=ctk.CTkButton(self.forgot_window,text='Reset',fg_color='white',text_color='black',font=('Arial',20, "bold"),width=70,command=self.reset)
        self.reset_btn.place(x=670,y=650)

    def reset(self):
        username = self.user_entry.get()
        answer = self.ans_entry.get()
        reset_pass = self.reset_entry.get()
        con_pass = self.con_entry.get()

        if username == '' or answer == '' or reset_pass == '' or con_pass == '':
            messagebox.showerror("Error", 'Enter all details', parent=self.forgot_window)
        if self.security_qn_combo_box.get() == "Select":
            messagebox.showerror("Error", "Please, select a query")
        elif reset_pass != con_pass:
            messagebox.showerror('Error', "Passwords don't match", parent=self.forgot_window)
        
        else:
            try:
                connection = mysql.connect(
                    host='localhost',
                    user='root',
                    password="Root@123",
                    database='travel_ms_db'
                )
                cursor = connection.cursor()
                query = "select * from admin_details where (email = %s or username = %s) and security_qn = %s and security_ans = %s"
                values = (username, username, self.security_qn_combo_box.get(), answer)
                cursor.execute(query, values)
                row = cursor.fetchone()
                if row is None:
                    messagebox.showerror('Error', "Please enter the correct answer", parent=self.forgot_window)
                else:
                    query = "UPDATE admin_details SET new_password = %s WHERE email = %s or username = %s"
                    values = (reset_pass, username, username)
                    cursor.execute(query, values)
                    connection.commit()
                    messagebox.showinfo("Success", "Your password has been reset. Please login with new password", parent=self.forgot_window)

            except Exception as e:
                messagebox.showerror("Error",f"an error occured: {str(e)}", parent=self.forgot_window)

            finally:
                if connection.is_connected():
                    connection.close() 
                    cursor.close()


    def return_login_page(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")

        my_cursor = connection.cursor()
        query2 = "select * from admin_register where email = %s or username = %s"
        values2 = (self.user_entry.get(), self.user_entry.get())
        my_cursor.execute(query2, values2)
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Needs registration before login", parent=self.root)
        else: 
            self.root.destroy()





if __name__ == "__main__":    
    root = Tk()
    obj = admin_forgot(root)
    root.mainloop()