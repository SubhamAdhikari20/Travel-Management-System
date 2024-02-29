from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
from mysql.connector import Error
import ctypes
import customtkinter as ctk
from datetime import datetime

class Account:
    def __init__(self):
        # Variables 
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.contact_var = StringVar()
        self.username_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.confirm_password_var = StringVar()

        # Update account data
        self.old_username_var = StringVar()
        self.old_email_var = StringVar()

        # Change Password
        self.old_password_var = StringVar()
        self.reset_password_var = StringVar()
        self.reset_confirm_password_var = StringVar()


    ## Ticket Details
    def account(self, parent_frame):
        # Ticket button frame
        self.account_button_frame = Frame(parent_frame, bg="lightblue")
        self.account_button_frame.place(x=0, y=0, width=1253, height=551)

        # Title Label
        account_label = Label(self.account_button_frame, text="Account", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        account_label.place(x=0, y=0, width=1253, height=50)
        
        # # Logo
        top_left_logo = Image.open("System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(account_label, image=self.top_left_logo)
        label_top_left_logo.place(x=5, y=0, width=40, height=40)

        ### account_details_frame - LabelFrame
        account_details_frame = LabelFrame(self.account_button_frame, text= "All Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue", bd=5, relief=RIDGE)
        account_details_frame.place(x=300, y=55, width=643, height=475)

        # Labels and Entries
        # First Name
        fname_label = Label(account_details_frame, text="First Name", fg="black", bg="lightblue", font=("Arial", 13, "bold"))
        fname_label.place(x=30, y=30)
        self.fname_entry = ttk.Entry(account_details_frame, textvariable=self.fname_var, font=("Arial", 15))
        self.fname_entry.place(x=30, y=60, width=250, height=35)
        
        # Last Name
        lname_label = Label(account_details_frame, text="Last Name", fg="black", bg="lightblue", font=("Arial", 13, "bold"))
        lname_label.place(x=350, y=30)
        self.lname_entry = ttk.Entry(account_details_frame, textvariable=self.lname_var, font=("Arial", 15))
        self.lname_entry.place(x=350, y=60, width=250, height=35)
        
        # Username
        username_label = Label(account_details_frame, text="Username", fg="black", bg="lightblue", font=("Arial", 13, "bold"))
        username_label.place(x=30, y=110)
        self.username_entry = ttk.Entry(account_details_frame, textvariable=self.username_var, font=("Arial", 15))
        self.username_entry.place(x=30, y=140, width=250, height=35)

        contact_label = Label(account_details_frame, text="Contact", fg="black", bg="lightblue", font=("Arial", 13, "bold"))
        contact_label.place(x=350, y=110)
        self.contact_entry = ttk.Entry(account_details_frame, textvariable=self.contact_var, font=("Arial", 15))
        self.contact_entry.place(x=350, y=140, width=250, height=35)

        # Email
        email_label = Label(account_details_frame, text="Email", fg="black", bg="lightblue", font=("Arial", 13, "bold"))
        email_label.place(x=30, y=190)
        self.email_entry = ttk.Entry(account_details_frame, textvariable=self.email_var,font=("Arial", 15))
        self.email_entry.place(x=30, y=215, width=570, height=35)
        # Contact
        

        # Change Password Button
        change_password_button = Button(account_details_frame, text="Change Password", font=("Arial", 14, "bold"), bd=3, fg="white", bg="green", activeforeground="white", activebackground="black", cursor="hand2", command=self.create_change_password)
        change_password_button.place(x=30, y=300, width=180, height=30)


        # CRUD Buttons
        update_button = Button(account_details_frame, text="Update", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=self.update_func)
        update_button.place(x=30, y=375, width=160, height=50)

        delete_button = Button(account_details_frame, text="Delete", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=self.delete_func)
        delete_button.place(x=235, y=375, width=160, height=50)

        logout_button = Button(account_details_frame, text="Logout", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=self.logout_func)
        logout_button.place(x=440, y=375, width=160, height=50)


        self.fetch_account_data()



    def create_change_password(self):
        # Change password Window
        self.change_password_window = Toplevel(self.account_button_frame, bg="white")
        self.change_password_window.title("Change Password")
        self.change_password_window.geometry("350x475+605+150")
        self.change_password_window.maxsize(350, 475)
        self.change_password_window.minsize(350, 475)
        self.change_password_window.resizable(0, 0)

        label_change_password = Label(self.change_password_window, text="Change Password", font=("Arial", 20, "bold"), fg="blue", bg="white")
        label_change_password.place(x=0, y=10, relwidth=1)
        
        # Security Answers
        old_password_label = Label(self.change_password_window, text="Old Password", fg="black", bg = "white", font=("Arial", 15, "bold"))
        old_password_label.place(x=50, y=60)
        self.old_password_entry = ttk.Entry(self.change_password_window, textvariable=self.old_password_var, font=("Arial", 15), show="*")
        self.old_password_entry.place(x=50, y=90, width=250, height=35)

        def old_password_show_password():
            if old_password_checkbox_var.get() == 1:            # If checkbox is checked
                self.old_password_entry.configure(show='')      # Show the password
            else:
                self.old_password_entry.configure(show='*')     # Hide the password

        old_password_checkbox_var = IntVar()
        old_password_check_button = ctk.CTkCheckBox(self.change_password_window,text="show password",variable=old_password_checkbox_var,command=old_password_show_password,checkmark_color="black",bg_color="white",fg_color="white",text_color="black",hover = FALSE, font=("Arial",13,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20,cursor="hand2")
        old_password_check_button.place(x=50, y=130)


        # Reset Password
        reset_password_label = Label(self.change_password_window, text="Reset Password", fg="black", bg = "white", font=("Arial", 15, "bold"))
        reset_password_label.place(x=50, y=170)
        self.reset_password_entry = ttk.Entry(self.change_password_window, textvariable=self.reset_password_var, font=("Arial", 15), show="*")
        self.reset_password_entry.place(x=50, y=200, width=250, height=35)

        def reset_password_show_password():
            if reset_password_checkbox_var.get() == 1:  # If checkbox is checked
                self.reset_password_entry.configure(show='')  # Show the password
            else:
                self.reset_password_entry.configure(show='*')  # Hide the password

        reset_password_checkbox_var = IntVar()
        reset_password_check_button = ctk.CTkCheckBox(self.change_password_window,text="show password",variable=reset_password_checkbox_var, command=reset_password_show_password,checkmark_color="black",bg_color="white",fg_color="white",text_color="black",hover = FALSE, font=("Arial",13,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20,cursor="hand2")
        reset_password_check_button.place(x=50,y=240)

        
        # Confirm Password
        confirm_password_label = Label(self.change_password_window, text="Confirm Password", fg="black", bg = "white", font=("Arial", 15, "bold"))
        confirm_password_label.place(x=50, y=280)
        self.confirm_password_entry = ttk.Entry(self.change_password_window, textvariable=self.reset_confirm_password_var, font=("Arial", 15), show="*")
        self.confirm_password_entry.place(x=50, y=310, width=250, height=35)
        
        def confirm_password_show_password():
            if confirm_password_checkbox_var.get() == 1:  # If checkbox is checked
                self.confirm_password_entry.configure(show='')  # Show the password
            else:
                self.confirm_password_entry.configure(show='*')  # Hide the password

        confirm_password_checkbox_var = IntVar()
        confirm_password_check_button = ctk.CTkCheckBox(self.change_password_window, text="show password",variable=confirm_password_checkbox_var, command=confirm_password_show_password, checkmark_color="black",bg_color="white",fg_color="white", text_color="black", hover = FALSE, font=("Arial",13,"bold"), onvalue=1, offvalue=0, checkbox_width=20, checkbox_height=20, cursor="hand2")
        confirm_password_check_button.place(x=50, y=350)



        # Reset Button
        reset_btn = Button(self.change_password_window, text="Reset", font=("Arial", 15, "bold"), fg="white", bg="blue", cursor="hand2", command=self.change_password_func)
        reset_btn.place(x=120, y=415, width=100, height=40)


        # Set grab on the popup window
        self.change_password_window.grab_set()





    ## Update 
    def update_func(self):
        if self.fname_var.get() == "" or self.lname_var.get() == "" or self.username_var.get() == "" or self.email_var.get() == "" or self.password_var.get() == "" or self.confirm_password_var.get() == "" or self.contact_var.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.account_button_frame)

        else:
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                my_cursor = connection.cursor()
                open_main = messagebox.askyesno("Are you sure?", "Account will be updated!!.", parent=self.account_button_frame)
                if open_main == 1:
                    query4 = "update passenger_details set fname = %s, lname = %s, contact = %s, email = %s, username = %s where (email = %s and username = %s)"
                    values4 = ( 
                            self.fname_entry.get(), 
                            self.lname_entry.get(), 
                            self.contact_entry.get(),
                            self.email_entry.get(),
                            self.username_entry.get(),
                            self.old_email_var.get(),
                            self.old_username_var.get()
                            )
                    my_cursor.execute(query4, values4)
                    messagebox.showinfo("Success", "Your account has been updated", parent=self.account_button_frame)
                    
                connection.commit()
                self.fetch_account_data()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.account_button_frame)

            finally:
                if connection.is_connected():
                    connection.close()
                    my_cursor.close()



    def change_password_func(self):
        if self.old_password_var.get() == "" or self.reset_password_var.get() == "" or self.reset_confirm_password_var.get() == "":
            messagebox.showerror("Error", "Fields are required!", parent=self.change_password_window)

        elif self.reset_password_var.get() != self.reset_confirm_password_var.get():
            messagebox.showerror("Invalid", "new password & confirm password must be same", parent=self.change_password_window)

        else:
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                my_cursor = connection.cursor()
                query3 = "select * from passenger_details where (email = %s and username = %s) and new_password = %s"
                values3 = (self.email_var.get(), self.username_var.get(), self.old_password_var.get())
                my_cursor.execute(query3, values3)
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Password is incorrect", parent=self.change_password_window)
                else:
                    query4 = "update passenger_details set new_password = %s where (email = %s and username = %s)"
                    values4 = ( 
                               self.reset_password_var.get(), 
                               self.email_var.get(),
                               self.username_var.get()
                               )
                    my_cursor.execute(query4, values4)
                    connection.commit()
                    messagebox.showinfo("Success", "Your password has been reset. Please login with new password", parent=self.change_password_window)

                    self.change_password_window.destroy()

                connection.commit()

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.change_password_window)

            finally:
                if connection.is_connected():
                    connection.close()
                    my_cursor.close()



    def delete_func(self):
        if self.fname_var.get() == "" or self.lname_var.get() == "" or self.username_var.get() == "" or self.email_var.get() == "" or self.password_var.get() == "" or self.confirm_password_var.get() == "" or self.contact_var.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.account_button_frame)

        else:
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                my_cursor = connection.cursor()
                
                open_main = messagebox.askyesno("Are you sure?", "The account will be deleted!!.", parent=self.account_button_frame)
                if open_main == 1:

                    query3 = "delete from passenger_details where (email = %s and username = %s)"
                    values3 = (self.email_entry.get(), self.username_entry.get())
                    my_cursor.execute(query3, values3)

                    connection.commit()
                    messagebox.showinfo("Successfully Deleted", "Record has been deleted!", parent=self.account_button_frame)
                    self.logout_func()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.account_button_frame)

            finally:
                if connection.is_connected():
                    connection.close()
                    my_cursor.close()


    def logout_func(self):
        from passenger_dashboard import Travel
        Travel.main_window_destroy()

        
    def fetch_account_data(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            my_cursor = connection.cursor()
            query3 = "select * from passenger_details where (email = %s and username = %s)"
            values3 = (self.email_entry.get(), self.username_entry.get())
            # values3 = (self.old_email_var.get(), self.old_username_var.get())
            my_cursor.execute(query3, values3)
            row = my_cursor.fetchone()
            if row != None:

                from passenger_dashboard import Travel
                Travel.set_dashboard_section_var(row[1], row[2], row[3], row[5], row[6], row[9])

            connection.commit()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.change_password_window)

        finally:
            if connection.is_connected():
                connection.close()
                my_cursor.close()


    def assign_var_account_section(self):
        # Copying data to account module 
        self.fname_var.set(self.dashboard_section_fname_var.get())
        self.lname_var.set(self.dashboard_section_lname_var.get())
        self.username_var.set(self.dashboard_section_username_var.get())
        self.contact_var.set(self.dashboard_section_contact_var.get())
        self.email_var.set(self.dashboard_section_email_var.get())
        self.password_var.set(self.dashboard_section_password_var.get())
        self.confirm_password_var.set(self.dashboard_section_confirm_password_var.get())

        # Old email and password
        self.old_email_var.set(self.dashboard_section_email_var.get())
        self.old_username_var.set(self.dashboard_section_username_var.get())