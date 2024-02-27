from tkinter import*
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql


class admin_forgot:
    def __init__(self,forgot_window):
        self.forgot_window   =forgot_window
        self.forgot_window.title('Forgot Password') 
        self.forgot_window.geometry('1440x900+0+0')
        self.forgot_window.resizable(0,0)    

        self.bg_img=Image.open('User_Authentication/images/forget_password.jpg')
        self.bg_resize=self.bg_img.resize((1440,900))
        self.bg_con=ImageTk.PhotoImage(self.bg_resize)
        self.bg_label=Label(self.forgot_window,image=self.bg_con)
        self.bg_label.place(x=0,y=0)

        self.frame=ctk.CTkFrame(self.forgot_window,fg_color='#5B5858',width=400,height=560,bg_color='transparent')
        self.frame.place(x=510,y=150)
        
        # admin Label
        self.ad_label=ctk.CTkLabel(self.forgot_window,text='Admin',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',25))
        self.ad_label.place(x=680,y=160)
        self.label=ctk.CTkLabel(self.forgot_window,text='Forgot password?',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',20))
        self.label.place(x=640,y=200)

        # username/email
        self.username_label=ctk.CTkLabel(self.forgot_window,text='Username/Email',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15)).place(x=600,y=240)
        self.user_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.user_entry.place(x=600,y=270)

        # security Question
        self.sec_ques=ctk.CTkLabel(self.forgot_window,text='Security Question',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.sec_ques.place(x=600,y=320)
        self.security_qn_combo_box = ttk.Combobox(self.forgot_window, font=("Aerial", 15), state="readonly",width=18,background='#5B5858')
        self.security_qn_combo_box["values"] = ("Select", "Favorite movie")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=600, y=350)


        # security Answer
        self.sec_ans=ctk.CTkLabel(self.forgot_window,text='Security Answer',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.sec_ans.place(x=600,y=400)
        self.ans_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.ans_entry.place(x=600,y=430)

        # reset password
        self.reset_label=ctk.CTkLabel(self.forgot_window,text='Reset Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.reset_label.place(x=600,y=480)
        self.reset_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.reset_entry.place(x=600,y=510)

        def hide():
           self.open_eye.configure(file='User_Authentication/images/closeye.png')
           self.reset_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='User_Authentication/images/openeye.png')
            self.reset_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='User_Authentication/images/openeye.png')
        self.open_btn=Button(self.forgot_window,image=self.open_eye,bg='white',bd=0,height=24,cursor='hand',command=hide)
        self.open_btn.place(x=783,y=511)

    # confirm password
        self.confirm=ctk.CTkLabel(self.forgot_window,text='Comfirm Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.confirm.place(x=600,y=560)
        self.con_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.con_entry.place(x=600,y=590)


        def hide1():
           self.open_eye1.configure(file='User_Authentication/images/closeye.png')
           self.con_entry.configure(show='*')
           self.open_btn1.configure(command=show1)
        def show1():
            self.open_eye1.configure(file='User_Authentication/images/openeye.png')
            self.con_entry.configure(show='')
            self.open_btn1.configure(command=hide1)
            
        self.open_eye1=PhotoImage(file='User_Authentication/images/openeye.png')
        self.open_btn1=Button(self.forgot_window,image=self.open_eye1,bg='white',bd=0,height=24,cursor='hand',command=hide1)
        self.open_btn1.place(x=783,y=591)
        


    # reset Button
        self.reset_btn=ctk.CTkButton(self.forgot_window,text='Reset',fg_color='white',text_color='black',font=('aerial',20),width=70,command=self.reset)
        self.reset_btn.place(x=670,y=650)

    def reset(self):
        username = self.user_entry.get()
        answer = self.ans_entry.get()
        reset_pass = self.reset_entry.get()
        con_pass = self.con_entry.get()

        if username == '' or answer == '' or reset_pass == '' or con_pass == '':
            messagebox.showerror("Error", 'Enter all details')
            return

        if reset_pass != con_pass:
            messagebox.showerror('Error', 'Both passwords do not match')
            return

        try:
            connection = mysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='user_authentication'
            )
            cursor = connection.cursor()
            query = 'SELECT * FROM register WHERE username = %s OR email = %s'
            cursor.execute(query, (username, username))
            row = cursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid username/email')
            else:
                if row[7] != answer:
                    messagebox.showerror('Error', 'Incorrect security answer')
                else:
                    query = 'UPDATE register SET password = %s WHERE sec_ans = %s'
                    cursor.execute(query, (reset_pass, answer))
                    connection.commit()
                    messagebox.showinfo("Success", "Password reset successfully")

        except Exception as e:
                    messagebox.showerror("Error",f"an error occured: {str(e)}")

        finally:
                    if connection.is_connected():
                        connection.close() 

    # def return_login_page(self):
    #     connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")

    #     my_cursor = connection.cursor()
    #     query2 = "select * from register where email = %s or username = %s"
    #     values2 = (self.email.get(), self.username.get())
    #     my_cursor.execute(query2, values2)
    #     row = my_cursor.fetchone()
    #     if row == None:
    #         messagebox.showerror("Error", "Needs registration before login", parent=self.root)
    #     else: 
    #         self.root.destroy()





if __name__ == "__main__":    
    root = Tk()
    obj = admin_forgot(root)
    root.mainloop()