from tkinter import*
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

import ctypes
myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class register_type:
    def __init__(self,window):
        self.window_register_type = window
        self.window_register_type.geometry('1440x900')
        self.window_register_type.title('Admin resgister')
        self.window_register_type.minsize(1465, 740)
        self.window_register_type.iconbitmap("System_Images/title_logo.ico")
        
        #bg_image
        bg2 = Image.open("User_Authentication/images/bg.jpg")
        resize_bg2 = bg2.resize((1465,750))
        self.bg2_image = ImageTk.PhotoImage(resize_bg2)
        Label(self.window_register_type,image=self.bg2_image).place(x=0,y=0) 

        #register_frame
        self.register_frame = Frame(self.window_register_type,bd=5,bg="white")
        self.register_frame.place(x=180,y=100,width=1200,height=600)
  
        #regiter_bg
        left_img = Image.open("User_Authentication/images/left_bg_img1.jpg")
        resize_left_img = left_img.resize((410,600))
        self.left_img_image = ImageTk.PhotoImage(resize_left_img)
        Label(self.register_frame,image=self.left_img_image).place(x=-5,y=-5,width=410,height=600)

        #heading
        ctk.CTkLabel(self.register_frame,text="Admin Register",bg_color="white",fg_color='white',text_color='black',font=("amiri",30,"bold")).place(x=450,y=10)

        #f_name
        ctk.CTkLabel(self.register_frame,text="First name",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=450,y=60)
        self.f_name_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),fg_color='white',text_color='black')
        self.f_name_entry.place(x=450,y=90)

        #l_name
        ctk.CTkLabel(self.register_frame,text="Last name",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=850,y=60)
        self.l_name_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.l_name_entry.place(x=850,y=90)

        #set_username
        ctk.CTkLabel(self.register_frame,text="Set username",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=450,y=130)
        self.u_name_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.u_name_entry.place(x=450,y=160)

        #E-mail
        ctk.CTkLabel(self.register_frame,text="E-mail",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=850,y=130)
        self.E_mail_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.E_mail_entry.place(x=850,y=160)

        #contact
        ctk.CTkLabel(self.register_frame,text="Contact",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=450,y=200)
        self.contact_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.contact_entry.place(x=450,y=230)

        #adress
        ctk.CTkLabel(self.register_frame,text="Address",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=850,y=200)
        self.address_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.address_entry.place(x=850,y=230)

        #s_question
        ctk.CTkLabel(self.register_frame,text="Security Question",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=450,y=270)
        self.security_qn_combo_box = ttk.Combobox(self.register_frame, font=("Amiri", 12), state="readonly",width=18)
        self.security_qn_combo_box["values"] = ("Select", "Birth Place", "Father's Name", "Citizenship No", "Favorite movie")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=450, y=300)

        # s_answer
        ctk.CTkLabel(self.register_frame,text="Security Answer",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=850,y=270)
        self.s_answer_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black')
        self.s_answer_entry.place(x=850,y=300)

        # s_password
        ctk.CTkLabel(self.register_frame,text="Set password",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=450,y=340)
        self.pass_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black', show="*")
        self.pass_entry.place(x=450,y=370)
   
       

        # c_password
        ctk.CTkLabel(self.register_frame,text="Confirm password",font=("amiri",20),bg_color="white",fg_color='white',text_color='black').place(x=850,y=340)
        self.cpass_entry = ctk.CTkEntry(self.register_frame,textvariable=StringVar(),width=200,font=("arisl",12),bg_color="white",fg_color='white',text_color='black', show="*")
        self.cpass_entry.place(x=850,y=370)

        #check_button
        self.terms_conditions = IntVar()
        self.che_button =Checkbutton(self.register_frame,variable=self.terms_conditions,text="I agree with the terms and conditions",fg='black',bg='white', cursor="hand2", activebackground="white")
        self.che_button.place(x=480,y=430)

        #register_button
        register_button_img = Image.open("User_Authentication/images/register_button_img.png")
        resize_register_img = register_button_img.resize((125,50))
        self.register_button_img = ImageTk.PhotoImage(resize_register_img)
        re_button = Button(self.register_frame,image=self.register_button_img, bg="white", bd=0, activebackground="white",command=self.db_connect, cursor="hand2")
        re_button.place(x=500,y=480,width=125,height=50)

        #login_button
        login_button_img = Image.open("User_Authentication/images/login_button_img.png")
        resize_login_button = login_button_img.resize((125,50))
        self.login_button_img = ImageTk.PhotoImage(resize_login_button)
        lo_button = Button(self.register_frame,image=self.login_button_img, bg="white",bd=0, activebackground="white",command=self.return_login_page, cursor="hand2")
        lo_button.place(x=800,y=480)

 # eye image
        def hide():
           self.open_eye.configure(file='User_Authentication/images/closeye.png')
           self.pass_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='User_Authentication/images/openeye.png')
            self.pass_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='User_Authentication/images/closeye.png')
        self.open_btn=Button(self.register_frame,image=self.open_eye,bg='white',bd=0,height=22,cursor='hand2',command=show)
        self.open_btn.place(x=620,y=371)
    
        def hide1():
           self.open_eye1.configure(file='User_Authentication/images/closeye.png')
           self.cpass_entry.configure(show='*')
           self.open_btn1.configure(command=show1)
        def show1():
            self.open_eye1.configure(file='User_Authentication/images/openeye.png')
            self.cpass_entry.configure(show='')
            self.open_btn1.configure(command=hide1)
            
        self.open_eye1=PhotoImage(file='User_Authentication/images/closeye.png')
        self.open_btn1=Button(self.register_frame,image=self.open_eye1,bg='white',bd=0,height=22,cursor='hand2',command=show1)
        self.open_btn1.place(x=1020,y=371)

      
    def db_connect(self):
            fname = self.f_name_entry.get()
            lname = self.l_name_entry.get()
            email = self.E_mail_entry.get()
            contact = self.contact_entry.get()
            address = self.address_entry.get()
            security_qn = self.security_qn_combo_box.get()
            security_ans = self.s_answer_entry.get()
            username = self.u_name_entry.get()
            setpass = self.pass_entry.get()
            cpass = self.cpass_entry.get()

            if fname == "" or lname == "" or email == "" or contact == "" or address == "" or security_qn=='' or security_ans == "" or username == "" or setpass == "" or cpass == "" :
                messagebox.showerror("Error","Fill all the details", parent=self.window_register_type)
            elif security_qn=='Select':
                 messagebox.showerror("Error","Select your security question", parent=self.window_register_type)
            elif setpass != cpass:
                messagebox.showerror("Error","Both password not match", parent=self.window_register_type)
            elif self.terms_conditions.get() == 0:
                messagebox.showerror("Error","Accept terms and conditions", parent=self.window_register_type)
            else:
                try:
                    connection = mysql.connector.connect(
                        host = "localhost",
                        username = "root",
                        password="Root@123",
                        database = "travel_ms_db"
                    )
                    my_cursor = connection.cursor()
        
                    quary1 = "select * from admin_details where email = %s and username = %s"
                    values1 = (email, username)
                    my_cursor.execute(quary1,values1)
                    row = my_cursor.fetchone()
                    if row is not None and row[4]==email:
                        messagebox.showerror("Error","email already taken ", parent=self.window_register_type)
                    else:
                        quary2 = "insert into admin_details (fname, lname, username, email, contact, address, security_qn, security_ans, new_password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        values2 = (fname, lname, username, email, contact, address, security_qn, security_ans,setpass)
                        
                        my_cursor.execute(quary2,values2) 
                        connection.commit()
                        messagebox.showinfo("Success","Id created successfully", parent=self.window_register_type)

                except Exception as e:
                    messagebox.showerror("Error",f"an error occured: {str(e)}", parent=self.window_register_type)

                finally:
                    if connection.is_connected():
                        my_cursor.close()
                        connection.close()   


    def return_login_page(self):
        connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                
        my_cursor = connection.cursor()
        query2 = "select * from admin_details where email = %s or username = %s"
        values2 = (self.E_mail_entry.get(), self.u_name_entry.get())
        my_cursor.execute(query2, values2)
        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror("Error", "Needs registration before login", parent=self.window_register_type)
        else: 
            from admin_code import admin_code
            admin_code.main_window_destroy()
            # from admin_login import Admin_login
            # new_window = Toplevel()
            # obj = Admin_login(new_window)
            # self.window_register_type.destroy()

            
            
if __name__ == "__main__":    
    root = Tk()
    obj = register_type(root)
    root.mainloop()
 

