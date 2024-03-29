from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class register_type:
    def __init__(self,window):
        self.window_register_type = window
        self.window_register_type.geometry("1465x740+0+0") 
        self.window_register_type.title("Passenge Register")
        self.window_register_type.iconbitmap("System_Images/title_logo.ico")


        #bg_image
        bg2 = Image.open("User_Authentication/images/register_bg.jpg")
        resize_bg2 = bg2.resize((1536,785))
        self.bg2_image = ImageTk.PhotoImage(resize_bg2)
        Label(self.window_register_type,image=self.bg2_image).place(x=0,y=0,width=1536,height=785) 

        #register_frame
        register_frame = Frame(self.window_register_type,bd=5,bg="white")
        register_frame.place(x=180,y=100,width=1200,height=600)

        #regiter_bg
        left_img = Image.open("User_Authentication/images/left_bg_img1.jpg")
        resize_left_img = left_img.resize((410,600))
        self.left_img_image = ImageTk.PhotoImage(resize_left_img)
        Label(register_frame,image=self.left_img_image).place(x=-5,y=-5,width=410,height=600)

        #heading
        register_label = Label(register_frame,text="Register",bg="white",font=("amiri",16,"bold"))
        register_label.place(x=450,y=10)
        #f_name
        f_name_label = Label(register_frame,text="First name",font=("amiri",12),bg="white")
        f_name_label.place(x=450,y=60)
        self.f_name_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.f_name_entry.place(x=450,y=90)

        #l_name
        l_name_label = Label(register_frame,text="Last name",font=("amiri",12),bg="white")
        l_name_label.place(x=850,y=60)
        self.l_name_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.l_name_entry.place(x=850,y=90)

        #set_username
        username_label = Label(register_frame,text="Set username",font=("amiri",12),bg="white")
        username_label.place(x=450,y=130)
        self.u_name_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.u_name_entry.place(x=450,y=160)

        #E-mail
        email_label = Label(register_frame,text="E-mail",font=("amiri",12),bg="white")
        email_label.place(x=850,y=130)
        self.E_mail_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.E_mail_entry.place(x=850,y=160)

        #contact
        contact_label = Label(register_frame,text="Contact",font=("amiri",12),bg="white")
        contact_label.place(x=450,y=200)
        self.contact_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12))
        self.contact_entry.place(x=450,y=230)

        #adress
        address_label = Label(register_frame,text="Adress",font=("amiri",12),bg="white")
        address_label.place(x=850,y=200)
        self.address_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.address_entry.place(x=850,y=230)

        #s_question
        s_qn_label = Label(register_frame,text="Security Question",font=("amiri",12),bg="white")
        s_qn_label.place(x=450,y=270)
        self.security_qn_combo_box = ttk.Combobox(register_frame, font=("Amiri", 12), state="readonly",width=18,cursor="hand2")
        self.security_qn_combo_box["values"] = ("Select", "Select", "Birth Place", "Father's Name", "Citizenship No", "Favorite movie")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=450, y=300)


        # s_answer
        s_ans_label = Label(register_frame,text="Security Answer",font=("amiri",12),bg="white")
        s_ans_label.place(x=850,y=270)
        self.s_answer_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),)
        self.s_answer_entry.place(x=850,y=300)

        # s_password
        s_password_label = Label(register_frame,text="Set password",font=("amiri",12),bg="white")
        s_password_label.place(x=450,y=340)
        self.pass_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),show="*")
        self.pass_entry.place(x=450,y=370)

        def hide1():
           self.close_eye1.configure(file='User_Authentication/images/closeye.png')
           self.pass_entry.configure(show='*')
           self.close_btn1.configure(command=show1)
        def show1():
            self.close_eye1.configure(file='User_Authentication/images/openeye.png')
            self.pass_entry.configure(show='')
            self.close_btn1.configure(command=hide1)

        self.close_eye1=PhotoImage(file='User_Authentication/images/closeye.png')
        self.close_btn1=Button(register_frame,image=self.close_eye1,bg='white',bd=0,height=20,command=show1,cursor="hand2")
        self.close_btn1.place(x=605,y=370)

        # c_password
        c_password_label = Label(register_frame,text="Confirm password",font=("amiri",12),bg="white")
        c_password_label.place(x=850,y=340)
        self.cpass_entry = ttk.Entry(register_frame,textvariable=StringVar(),width=20,font=("arisl",12),show="*")
        self.cpass_entry.place(x=850,y=370)

        def hide():
           self.close_eye.configure(file='User_Authentication/images/closeye.png')
           self.cpass_entry.configure(show='*')
           self.close_btn.configure(command=show)
        def show():
            self.close_eye.configure(file='User_Authentication/images/openeye.png')
            self.cpass_entry.configure(show='')
            self.close_btn.configure(command=hide)

        self.close_eye=PhotoImage(file='User_Authentication/images/closeye.png')
        self.close_btn=Button(register_frame,image=self.close_eye,bg='white',bd=0,height=20,command=show,cursor="hand2")
        self.close_btn.place(x=1005,y=370)

        #check_button
        self.terms_conditions = IntVar()
        self.che_button = Checkbutton(register_frame,variable=self.terms_conditions,bg="white",fg="black",text="I agree with the terms and conditions",onvalue=1,offvalue=0,cursor="hand2",activebackground="white")
        self.che_button.place(x=480,y=430)

        #register_button
        register_button_img = Image.open("User_Authentication/images/register_button_img.png")
        resize_register_img = register_button_img.resize((125,50))
        self.register_button_img = ImageTk.PhotoImage(resize_register_img)
        re_button = Button(register_frame,image=self.register_button_img,bd=0,bg="white",activebackground="white",cursor="hand2", command=self.db_connect)
        re_button.place(x=500,y=480,width=125,height=50)

        #login_button
        login_button_img = Image.open("User_Authentication/images/login_button_img.png")
        resize_login_button = login_button_img.resize((125,50))
        self.login_button_img = ImageTk.PhotoImage(resize_login_button)
        lo_button = Button(register_frame,image=self.login_button_img,bd=0,bg="white",activebackground="white",cursor="hand2", command=self.return_login_page)
        lo_button.place(x=800,y=480)

        self.fname = self.f_name_entry
        self.lname = self.l_name_entry
        self.email = self.E_mail_entry
        self.contact = self.contact_entry
        self.address = self.address_entry
        self.security_qn = self.security_qn_combo_box
        self.security_ans = self.s_answer_entry
        self.username = self.u_name_entry
        self.setpass = self.pass_entry
        self.cpass = self.cpass_entry


    def db_connect(self):
        if self.fname.get() == "" or self.lname.get() == "" or self.email.get() == "" or self.contact.get() == "" or self.address == "" or self.security_ans.get() == "" or self.username.get() == "" or self.setpass.get() == "" or self.cpass.get() == "" :
            messagebox.showerror("Error","Fill all the details",parent = self.window_register_type)
        elif self.setpass.get() != self.cpass.get():
            messagebox.showerror("Error","Both password should match",parent = self.window_register_type)
        elif self.terms_conditions.get() == 0:
            messagebox.showerror("Error","Accept terms and conditions",parent = self.window_register_type)
        else:
            try:
                connection = mysql.connector.connect(
                    host = "localhost",
                    username = "root",
                    password = "Root@123",
                    database = "travel_ms_db"
                )
                my_cursor = connection.cursor()
                quary1 = "select * from passenger_details where email = %s or username = %s"
                values1 = (self.email.get(), self.username.get())
                my_cursor.execute(quary1,values1,)
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error","You already have account",parent = self.window_register_type)
                else:
                    quary2 = "insert into passenger_details (fname, lname, username, contact, email, address, security_qn, security_ans, new_password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    values2 = (self.fname.get(),self.lname.get(),self.username.get(),self.contact.get(),self.email.get(),self.address.get(),self.security_qn.get(),self.security_ans.get(),self.setpass.get())
                    my_cursor.execute(quary2,values2)
                        
                    connection.commit()
                    messagebox.showinfo("Success","Id created successfully",parent = self.window_register_type)

            except Exception as e:
                messagebox.showerror("Error",f"an error occured: {str(e)}",parent = self.window_register_type)

            finally:
                if connection.is_connected():
                    connection.close()


    def return_login_page(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")

        my_cursor = connection.cursor()
        query2 = "select * from passenger_details where email = %s or username = %s"
        values2 = (self.email.get(), self.username.get())
        my_cursor.execute(query2, values2)
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Needs registration before login", parent=self.window_register_type)
        else: 
            # new_window = Toplevel()
            # from passenger_login import Passenger_Login
            # obj = Passenger_Login(new_window)
            self.window_register_type.destroy()


if __name__ == "__main__":       
    root = Tk()
    obj = register_type(root)
    root.mainloop()