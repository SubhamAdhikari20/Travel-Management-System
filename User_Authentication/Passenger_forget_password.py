from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

class forget_password:
    def __init__(self,window):
        self.forget_pass = window
        self.forget_pass.geometry("1536x785+0+0")
        self.forget_pass.title("forget Password")

        #image
        bg1 = Image.open("User_Authentication/images/user_forget_password.jpg")
        resize_bg1 = bg1.resize((1536,786))
        self.bg1_img =ImageTk.PhotoImage(resize_bg1)
        bg_label = Label(self.forget_pass,image=self.bg1_img)
        bg_label.place(x=0,y=0)

        forget_frame = Frame(self.forget_pass,bg="gray38")
        forget_frame.place(x=600,y=140,width=350,height=450)

        # Label
        forget_label = Label(forget_frame,text="Forget Password?",font=("amiri",14,"bold"),bg="gray38",fg="white")
        forget_label.place(x=85,y=10)
        
        #back
        back_button = Button(forget_frame,text="X",font=("amiri",12,"bold"),bg="gray38",fg="white",bd=0)
        back_button.place(x=0,y=0)

        # email
        email_label = Label(forget_frame,text="Email",font=("amiri",12,"bold"),bg="gray38",fg="white")
        email_label.place(x=70,y=50)
        self.email_entry = ctk.CTkEntry(forget_frame,textvariable=StringVar(),width=190,font=("amiri",12,"bold"),corner_radius=20)
        self.email_entry.place(x=70,y=80)

        #security_question
        s_ques_label = Label(forget_frame,text="Security Question",font=("amiri",12,"bold"),bg="gray38",fg="white")
        s_ques_label.place(x=70,y=120)
        self.security_qn_combo_box = ttk.Combobox(forget_frame, font=("Amiri", 12,"bold"), state="readonly",width=18,)
        self.security_qn_combo_box["values"] = ("Select", "Favorite movie","Favorite food")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=70, y=150)

        #security answer
        s_ans_label = Label(forget_frame,text="Security answer",bg="gray38",font=("amiri",12,"bold"),fg="white")
        s_ans_label.place(x=70,y=190)
        self.security_ans_entry = ctk.CTkEntry(forget_frame,textvariable=StringVar(),width=190,font=("amiri",12,"bold"),corner_radius=20)
        self.security_ans_entry.place(x=70,y=220)

        #reset password

        re_label = Label(forget_frame,text="Reset password",font=("amiri",12,"bold"),bg="gray38",fg="white")
        re_label.place(x=70,y=260)
        self.re_password_entry = ctk.CTkEntry(forget_frame,show = "*",textvariable=StringVar(),width=190,font=("amiri",12,"bold"),corner_radius=20)
        self.re_password_entry.place(x=70,y=290)

        def hide():
           self.close_eye.configure(file='User_Authentication/images/closeye.png')
           self.re_password_entry.configure(show='*')
           self.close_btn.configure(command=show)
        def show():
            self.close_eye.configure(file='User_Authentication/images/openeye.png')
            self.re_password_entry.configure(show='')
            self.close_btn.configure(command=hide)

        self.close_eye=PhotoImage(file='User_Authentication/images/closeye.png')
        self.close_btn=Button(forget_frame,image=self.close_eye,bg='white',bd=0,height=20,command=show)
        self.close_btn.place(x=228,y=293)

        #conform_password
        con_label = Label(forget_frame,text="conform password",font=("amiri",12,"bold"),bg="gray38",fg="white")
        con_label.place(x=70,y=330)
        self.con_password_entry = ctk.CTkEntry(forget_frame,show = "*",textvariable=StringVar(),width=190,font=("amiri",12,"bold"),corner_radius=20)
        self.con_password_entry.place(x=70,y=360)

        def hide1():
           self.close_eye1.configure(file='User_Authentication/images/closeye.png')
           self.con_password_entry.configure(show='*')
           self.close_btn1.configure(command=show1)
        def show1():
            self.close_eye1.configure(file='User_Authentication/images/openeye.png')
            self.con_password_entry.configure(show='')
            self.close_btn1.configure(command=hide1)

        self.close_eye1=PhotoImage(file='User_Authentication/images/closeye.png')
        self.close_btn1=Button(forget_frame,image=self.close_eye1,bg='white',bd=0,height=20,command=show1)
        self.close_btn1.place(x=228,y=363)

        #button
        reset_button = ctk.CTkButton(forget_frame,text="Reset",font=("amiri",12,"bold"),corner_radius=20,bg_color="gray38",fg_color="white",text_color="black",width=80, command=self.check)
        reset_button.place(x=130,y=400)


    def check(self):
        reset_p = self.re_password_entry.get()
        conform_p = self.con_password_entry.get()

        if self.security_ans_entry.get() == "" or self.email_entry.get() == "" or self.re_password_entry.get() == "" or self.con_password_entry == "" or self.security_qn_combo_box.get() == "":
            messagebox.showerror("Error","Fill all the details",parent = self.forget_pass)

        elif self.security_qn_combo_box.get() == "Select":
            messagebox.showerror("Error", "Select a query!", parent = self.forget_pass)

        elif self.re_password_entry.get() != self.con_password_entry.get():
            messagebox.showerror("Error","Conform password does not match", parent = self.forget_pass)

        else:
            try:
                connection = mysql.connector.connect(
                    host = "localhost",
                    username = "root",
                    password = "#Nbchand07",
                    database = "travel_ms_db"
                )
                my_cursor = connection.cursor()
                quary1 = "select * from passenger_details where (email = %s or username = %s) and security_qn = %s and security_ans = %s"
                values1 = (self.email_entry.get(), self.email_entry.get(), self.security_qn_combo_box.get(), self.security_ans_entry.get())
                my_cursor.execute(quary1,values1)
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("error","Email or security Question is wrong", parent = self.forget_pass)
                
                else:
                    update_quary = "update passenger_details set new_password = %s where (email = %s or username = %s)"
                    update_values = (reset_p, self.email_entry.get(), self.email_entry.get())
                    my_cursor.execute(update_quary,update_values)

                connection.commit()
                messagebox.showinfo("success","Password changed successfully", parent = self.forget_pass)
                self.forget_pass.destroy()

            except Exception as e:
                messagebox.showerror("Error",f"an error occured: {str(e)}", parent = self.forget_pass)

            finally:
                if connection.is_connected():
                    connection.close()
                    my_cursor.close()



    
if __name__ == "__main__":
    root = Tk()
    obj = forget_password(root)
    root.mainloop()