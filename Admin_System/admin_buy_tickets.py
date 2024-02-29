from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import customtkinter as ctk
from datetime import datetime
from admin_ticket_info import Ticket_Info

import json
from mysql.connector import Error
from admin_ticket_info import Ticket_Info

class Ticket:
    def __init__(self):
        ## Variables 
        self.buy_ticket_section_passenger_name_var = StringVar()
        self.buy_ticket_section_passenger_contact_var = StringVar()        

        self.buy_ticket_section_bus_no_var = StringVar()
        self.buy_ticket_section_total_passenger_var = StringVar()
        self.buy_ticket_section_bus_agency_var = StringVar()
        self.buy_ticket_section_departure_date_var = StringVar()
        self.buy_ticket_section_departure_time_var = StringVar()
        self.buy_ticket_section_from_var = StringVar()
        self.buy_ticket_section_to_var = StringVar()
        self.buy_ticket_section_fare_var = StringVar()
        self.buy_ticket_section_reporting_time_var = StringVar()
        self.bus_type = StringVar()

        # Authetication variable - initializing buy_ticket
        self.buy_ticket_section_username_var = StringVar()
        self.buy_ticket_section_email_var = StringVar()
        self.buy_ticket_section_password_var = StringVar()


    ## Ticket Details
    def buy_ticket(self, parent_frame):
        # Ticket button frame #
        self.ticket_button_frame = Frame(parent_frame, bg="lightblue")
        self.ticket_button_frame.place(x=0, y=0, width=1253, height=551)

        # Title Label #
        buy_ticket_label = Label(self.ticket_button_frame, text="Buy Ticket", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        buy_ticket_label.place(x=0, y=0, width=1253, height=50)
        
        ## Logo
        top_left_logo = Image.open("System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(buy_ticket_label, image=self.top_left_logo)
        label_top_left_logo.place(x=5, y=0, width=40, height=40)

        ticket_details_frame = LabelFrame(self.ticket_button_frame, text= "Ticket Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
        ticket_details_frame.place(x=5, y=55, width=375, height=490)


        # search For cancel Button
        self.search_for_cancel_btn = ctk.CTkButton(ticket_details_frame, text="", fg_color="#35c857",  cursor="hand2", width=18, height=18, hover_color="#368e4b", font=("times new roman", 17, "bold"), corner_radius=150, command=self.search_for_cancel_btn_func)
        self.search_for_cancel_btn.place(x=352, y=57)


        passenger_name_label = Label(ticket_details_frame, text="Passenger Name:", bg="lightblue", font=("Arial", 12, "bold"))
        passenger_name_label.place(x=5, y=10)
        self.passenger_name_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_passenger_name_var)
        self.passenger_name_entry.place(x=150, y=10, width=200, height=30)
        
        contact_label = Label(ticket_details_frame, text="Mobile Number:", bg="lightblue", font=("Arial", 12, "bold"))
        contact_label.place(x=5, y=50)
        self.contact_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_passenger_contact_var)
        self.contact_entry.place(x=150, y=50, width=200, height=30)
        
        bus_no_label = Label(ticket_details_frame, text="Bus No:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_no_label.place(x=5, y=90)
        bus_no_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_bus_no_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        bus_no_entry_label.place(x=150, y=90, width=200, height=30)

        bus_agency_label = Label(ticket_details_frame, text="Bus Agency:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_agency_label.place(x=5, y=130)
        bus_agency_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_bus_agency_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        bus_agency_entry_label.place(x=150, y=130, width=200, height=30)

        departure_date_label = Label(ticket_details_frame, text="Departure Date:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_date_label.place(x=5, y=170)
        departure_date_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_departure_date_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        departure_date_entry_label.place(x=150, y=170, width=200, height=30)
        
        departure_time_label = Label(ticket_details_frame, text="Departure Time:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_time_label.place(x=5, y=210)
        departure_time_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_departure_time_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        departure_time_entry_label.place(x=150, y=210, width=200, height=30)

        from_label = Label(ticket_details_frame, text="From:", font=("Arial", 12, "bold"), bg="lightblue")
        from_label.place(x=5, y=250)
        combo_box_frome_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_from_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        combo_box_frome_entry_label.place(x=150, y=250, width=200, height=30)
       
        combo_box_frome_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_from_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        combo_box_frome_entry_label.place(x=150, y=250, width=200, height=30)
        
        to_label = Label(ticket_details_frame, text="To:", font=("Arial", 12, "bold"), bg="lightblue")
        to_label.place(x=5, y=290)
        combo_box_to_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_to_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        combo_box_to_entry_label.place(x=150, y=290, width=200, height=30)
        
        fare_label = Label(ticket_details_frame, text="Fare (NPR):", bg="lightblue", font=("Arial", 12, "bold"))
        fare_label.place(x=5, y=330)

        if self.buy_ticket_section_fare_var.get() == "":
            self.buy_ticket_section_fare_var.set("0.0")

        fare_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_fare_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        fare_entry_label.place(x=150, y=330, width=200, height=30)
        
        total_passenger_label = Label(ticket_details_frame, text="Total Passengers:", bg="lightblue", font=("Arial", 12, "bold"))
        total_passenger_label.place(x=5, y=370)
        self.buy_ticket_section_total_passenger_var.set("0")

        total_passenger_entry_label = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_total_passenger_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        total_passenger_entry_label.place(x=150, y=370, width=200, height=30)

        reporting_time_label = Label(ticket_details_frame, text="Reporting Time:", bg="lightblue", font=("Arial", 12, "bold"))
        reporting_time_label.place(x=5, y=410)
        reporting_time_entry = Label(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_reporting_time_var, anchor=W, bg="white", borderwidth=1, relief=RIDGE)
        reporting_time_entry.place(x=150, y=410, width=200, height=30)

        ## -------------------Bus Seats Booking----------------------
        bus_info_frame = Frame(self.ticket_button_frame, bg="#182356", bd=3, relief=RIDGE)
        bus_info_frame.place(x=390, y=70, width=350, height=75)


        bus_agency_label = Label(bus_info_frame, textvariable=self.buy_ticket_section_bus_agency_var, bg="#182356", fg="white", font=("Arial", 17, "bold"))
        bus_agency_label.place(x=5, y=5)
        bus_type_label = Label(bus_info_frame, textvariable=self.bus_type, bg="#182356", fg="white", font=("Arial", 11, "bold"))
        bus_type_label.place(x=7, y=40)
        
        seat_index_frame = Frame(self.ticket_button_frame, bg="#182356", bd=3, relief=RIDGE)
        seat_index_frame.place(x=850, y=70, width=389, height=75)
        seat_index_label = Label(seat_index_frame, text="Seat Index", bg="#182356", fg="white", font=("Arial", 17, "bold"))
        seat_index_label.place(x=15, y=5)
        
        available_index_button = ctk.CTkButton(seat_index_frame, text="", fg_color="#323645", width=20, height=20, hover=False,)
        available_index_button.place(x=28, y=40)
        available_label = Label(seat_index_frame, text="Available", bg="#182356", fg="white", font=("Arial", 10, "bold"))
        available_label.place(x=50, y=40)

        selected_index_button = ctk.CTkButton(seat_index_frame, text="", fg_color="#1db640", width=20, height=20, hover=False,)
        selected_index_button.place(x=138, y=40)
        selected_label = Label(seat_index_frame, text="Selected", bg="#182356", fg="white", font=("Arial", 10, "bold"))
        selected_label.place(x=160, y=40)

        booked_index_button = ctk.CTkButton(seat_index_frame, text="", fg_color="#bc0202", width=20, height=20, hover=False,)
        booked_index_button.place(x=248, y=40)
        booked_label = Label(seat_index_frame, text="Booked", bg="#182356", fg="white", font=("Arial", 10, "bold"))
        booked_label.place(x=270, y=40)
        
        self.bus_seats_frame = Frame(self.ticket_button_frame, bg="#081548", bd=3, relief=RIDGE)
        self.bus_seats_frame.place(x=390, y=152, width=850, height=305)

        # After booking, insert data into the database
        self.bus_no = self.buy_ticket_section_bus_no_var.get()        
        self.booked_seats_ls = self.fetch_booked_seats()         # fetch list from database
        self.booking_date = datetime.now().strftime("%Y-%m-%d")  # Current date and time

        if self.bus_no == "":
            self.seats_reference = [[0]*9 if i != 2 else [0] for i in range(5)]
        else:
            self.seats_reference = self.fetch_seat_reference_data()
        

        self.seats_buttons = []
        

        # Row 1
        for i in range(5):
            row_buttons = []
            for j in range(9):
                if i == 0 and j == 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{2}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)

                elif i == 0 and j < 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{17-2*j}", fg_color="#323645",cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))    
                    
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)
            

            # Row 2
                elif i == 1 and j == 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{1}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)

                elif i == 1 and j < 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{18-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)            


            # Row 3    
                elif i == 2 and j == 0:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{19}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)


            # Row 4
                elif i == 3 and j < 9:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"B{17-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)


            # Row 5
                elif i == 4 and j < 9:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"B{18-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, command= lambda i=i, j=j: self.book_seat(i, j), hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)
            
            self.seats_buttons.append(row_buttons)


        # Update the GUI of Booled Seats
        self.update_booked_seats_gui()
        # self.update_display_no_of_seats()

        # Steering Logo
        # steering_logo = Image.open("System_Images/steering.png")
        # steering_logo = steering_logo.resize((50, 40), Image.LANCZOS) 
        # steering_logo = ImageTk.PhotoImage(steering_logo)
        # steering_logo = Label(self.bus_seats_frame, image=steering_logo)
        # steering_logo.place(x=830, y=380, width=40, height=40)

        ## Footer Frame
        self.footer_frame = Frame(self.ticket_button_frame, bg="gray12", bd=3, relief=RIDGE)
        self.footer_frame.place(x=390, y=465, width=850, height=75)

        selected_seats_title_label = Label(self.footer_frame, text="Selected Seat(s)", fg="white", bg="gray12", font=("Arial", 15, "bold"))
        selected_seats_title_label.place(x=15, y=5)

        self.selected_ones = "Not selected"
        self.selected_seats_label = Label(self.footer_frame, text=self.selected_ones, fg="white", bg="gray12", font=("Arial", 12, "bold"))
        self.selected_seats_label.place(x=15, y=30)

        total_price_title_label = Label(self.footer_frame, text="Total Price", fg="white", bg="gray12", font=("Arial", 15, "bold"))
        total_price_title_label.place(x=400, y=5)

        self.total = f"{0:.2f}"
        self.total_price = Label(self.footer_frame, text=f"NPR. {self.total}", fg="white", bg="gray12", font=("Arial", 12, "bold"))
        self.total_price.place(x=405, y=30)
        
        # book button
        book_now_button = ctk.CTkButton(self.footer_frame, text="BOOK NOW", fg_color="#35c857",  cursor="hand2", width=125, height=50, hover_color="#368e4b", font=("times new roman", 15, "bold"), command=self.create_booking_confirmation_window)
        book_now_button.place(x=700, y=10)

        # cancel button
        self.cancel_button = None

        # Ticket Info initiallization
        self.ticket_info_obj = Ticket_Info()


    ## Buy Tickets Functions
    def book_seat(self, row, col):
        # selected_count = sum(sum(row) for row in self.seats_reference)
        selected_count = int(self.buy_ticket_section_total_passenger_var.get())
        if self.seats_reference[row][col] == 0:         # 0 -> Available Seats
            if selected_count < 10:                     # Mark seat as selected 
                self.seats_reference[row][col] = 1      # 1 -> Selected Seats
                self.og_color = self.seats_buttons[row][col].cget("fg_color")
                self.seats_buttons[row][col].configure(fg_color="#1db640", hover=False)

            else:
                messagebox.showerror("Error", "Maximum limit of 10 seats reached.", parent=self.ticket_button_frame)
                return

        elif self.seats_reference[row][col] == 1:       # 1 -> Selected Seats
            self.seats_reference[row][col] = 0          # 0 -> Available Seats
            self.seats_buttons[row][col].configure(fg_color=self.og_color, hover=True)


        elif self.seats_reference[row][col] == 2:       # 2 -> Booked Seats
            messagebox.showerror("Error", "Already Booked", parent=self.ticket_button_frame)
            return

        self.get_selected_seats()   
        self.get_total_price(float(self.buy_ticket_section_fare_var.get()))  



    def get_selected_seats(self):
        self.selected_seats_ls = []
        selected_count = 0
        for i in range(len(self.seats_reference)):
            for j in range(len(self.seats_reference[i])):
                if self.seats_reference[i][j] == 1:
                    self.selected_seats_ls.append(self.seats_buttons[i][j].cget("text"))
                    selected_count += 1
                    if selected_count == 10:
                        break
            self.buy_ticket_section_total_passenger_var.set(str(selected_count)) 
            if selected_count == 10:
                break

        if self.selected_seats_ls:           # If contains any element
            self.selected_ones = ", ".join(self.selected_seats_ls) 


        else:
            self.selected_ones = "Not selected"

        self.selected_seats_label.config(text=self.selected_ones)
        return self.selected_seats_ls



    def get_total_price(self, seat_price):
        self.total = 0  # Reset Total Price
        seat_fare_ls = []
        for i in range(len(self.seats_reference)):
            for j in range(len(self.seats_reference[i])):
                if self.seats_reference[i][j] == 1:
                    # Appending seat_price to the list
                    seat_fare_ls.append(seat_price)

        if seat_fare_ls:        # If contains any element
            self.total = sum(seat_fare_ls)
        else:                   # Else
            self.total = 0.0

        self.total_price.config(text=f"NPR. {self.total:.2f}")



    def create_booking_confirmation_window(self):
        if self.buy_ticket_section_passenger_name_var.get() != "" and self.buy_ticket_section_passenger_contact_var.get() != "":
            if self.selected_ones != "Not selected":
            
                # Confirm Transaction Window
                self.confirm_transaction_window = Toplevel(self.ticket_button_frame, bg="lightblue")
                self.confirm_transaction_window.title("Confirm Authentication")
                self.confirm_transaction_window.geometry("450x300+550+150")
                self.confirm_transaction_window.maxsize(450, 300)
                self.confirm_transaction_window.minsize(450, 300)
                self.confirm_transaction_window.resizable(0, 0)

                confirm_transaction_label = Label(self.confirm_transaction_window, text="Confirm Transaction", font=("Arial", 20, "bold"), fg="green", bg="lightblue")
                confirm_transaction_label.place(x=0, y=10, relwidth=1)
                
                username_label = Label(self.confirm_transaction_window, text="Username:", fg="black", bg = "lightblue", font=("Arial", 14, "bold"))
                username_label.place(x=40, y=75)
                self.booking_transaction_username_entry = ttk.Entry(self.confirm_transaction_window, font=("Arial", 14, "bold"))
                self.booking_transaction_username_entry.place(x=160, y=75, width=235, height=35)

                password_label = Label(self.confirm_transaction_window, text="Password:", fg="black", bg = "lightblue", font=("Arial", 14, "bold"))
                password_label.place(x=40, y=135)
                self.booking_transaction_password_entry = ttk.Entry(self.confirm_transaction_window, font=("Arial", 14, "bold"), show="*")
                self.booking_transaction_password_entry.place(x=160, y=135, width=235, height=35)

                def password_show_password():
                    if password_checkbox_var.get() == 1:            # If checkbox is checked
                        self.booking_transaction_password_entry.configure(show='')      # Show the password
                    else:
                        self.booking_transaction_password_entry.configure(show='*')     # Hide the password

                password_checkbox_var = IntVar()
                password_check_button = ctk.CTkCheckBox(self.confirm_transaction_window,text="show password",variable=password_checkbox_var,command=password_show_password,checkmark_color="black",bg_color="lightblue",fg_color="white",text_color="black",hover = FALSE, font=("Arial",13,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20,cursor="hand2")
                password_check_button.place(x=160, y=175)


                # Buttons
                confirm_button = Button(self.confirm_transaction_window, text="CONFIRM", font=("Arial", 15, "bold"),bg="black", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=self.book_now_button_func)
                confirm_button.place(x=50, y=240, width=150, height=40)

                # Set grab on the popup window
                self.confirm_transaction_window.grab_set()
            
                # cancel button
                def cancel_func():
                    self.ticket_button_frame.grab_release()
                    self.confirm_transaction_window.destroy()

                cancel_button = Button(self.confirm_transaction_window, text="CANCEL", font=("Arial", 15, "bold"),bg="black", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=cancel_func)
                cancel_button.place(x=232, y=240, width=165, height=40)

            else:
                messagebox.showerror("Error", "seats selection required!", parent=self.ticket_button_frame)

        else:
            messagebox.showerror("Error", "Fields required!", parent=self.ticket_button_frame)

        

    def create_cancel_booking_confirmation_window(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()

            # For ckecking if the data is equivalent to [[0]*9 if i != 2 else [0] for i in range(5)]
            query = "SELECT seat_reference_wrt_id FROM booking_id_table WHERE bus_no = %s ORDER BY booking_id DESC LIMIT 1"
            values = (self.bus_no,)
            cursor.execute(query, values)
            row = cursor.fetchone()
            if row is not None:
                if json.loads(row[0]) == [[0]*9 if i != 2 else [0] for i in range(5)]:
                    messagebox.showerror("Error", "Not Cancel", parent=self.confirm_cancel_window)

                else:
                    # Change password Window
                    self.confirm_cancel_window = Toplevel(self.ticket_button_frame, bg="lightblue")
                    self.confirm_cancel_window.title("Confirm Authentication")
                    self.confirm_cancel_window.geometry("450x300+550+150")
                    self.confirm_cancel_window.maxsize(450, 300)
                    self.confirm_cancel_window.minsize(450, 300)
                    self.confirm_cancel_window.resizable(0, 0)

                    confirm_cancel_label = Label(self.confirm_cancel_window, text="Confirm Cancel", font=("Arial", 20, "bold"), fg="green", bg="lightblue")
                    confirm_cancel_label.place(x=0, y=10, relwidth=1)
                    
                    # Security Answers
                    username_label = Label(self.confirm_cancel_window, text="Username:", fg="black", bg = "lightblue", font=("Arial", 14, "bold"))
                    username_label.place(x=40, y=75)
                    self.booking_cancellation_username_entry = ttk.Entry(self.confirm_cancel_window, font=("Arial", 14, "bold"))
                    self.booking_cancellation_username_entry.place(x=160, y=75, width=235, height=35)

                    # Security Answers
                    password_label = Label(self.confirm_cancel_window, text="Password:", fg="black", bg = "lightblue", font=("Arial", 14, "bold"))
                    password_label.place(x=40, y=135)
                    self.booking_cancellation_password_entry = ttk.Entry(self.confirm_cancel_window, font=("Arial", 14, "bold"), show="*")
                    self.booking_cancellation_password_entry.place(x=160, y=135, width=235, height=35)

                    def password_show_password():
                        if password_checkbox_var.get() == 1:            # If checkbox is checked
                            self.booking_cancellation_password_entry.configure(show='')      # Show the password
                        else:
                            self.booking_cancellation_password_entry.configure(show='*')     # Hide the password

                    password_checkbox_var = IntVar()
                    password_check_button = ctk.CTkCheckBox(self.confirm_cancel_window,text="show password",variable=password_checkbox_var,command=password_show_password,checkmark_color="black",bg_color="lightblue",fg_color="white",text_color="black",hover = FALSE, font=("Arial",13,"bold"),onvalue=1,offvalue=0,checkbox_width=20,checkbox_height=20,cursor="hand2")
                    password_check_button.place(x=160, y=175)


                    # Buttons
                    confirm_button = Button(self.confirm_cancel_window, text="CONFIRM", font=("Arial", 15, "bold"),bg="black", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=self.cancel_booking)
                    confirm_button.place(x=50, y=240, width=150, height=40)

                    # Set grab on the popup window
                    self.confirm_cancel_window.grab_set()
                
                    def cancel_leave_func():
                        self.ticket_button_frame.grab_release()
                        self.confirm_cancel_window.destroy()

                    leave_button = Button(self.confirm_cancel_window, text="LEAVE", font=("Arial", 15, "bold"),bg="black", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold", command=cancel_leave_func)
                    leave_button.place(x=232, y=240, width=165, height=40)

                connection.commit()

        except Error as e:
                messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.confirm_cancel_window)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def book_now_button_func(self):
        if self.booking_transaction_username_entry.get() != "" and self.booking_transaction_password_entry.get() != "":

            if self.booking_transaction_username_entry.get() == (self.buy_ticket_section_username_var.get() or self.buy_ticket_section_email_var) and self.booking_transaction_password_entry.get() == self.buy_ticket_section_password_var.get():
                # selecting seats
                seats_ls = self.get_selected_seats()   
                self.get_total_price(float(self.buy_ticket_section_fare_var.get()))  

                for i in seats_ls:
                    self.booked_seats_ls.append(i)

                messagebox.showinfo("Sucessfully Booked", "Thank you and Please, visit us again.", parent=self.confirm_transaction_window)
                self.update_booking_data()      ## It contains GUI and DATABASE updation
                self.insert_booking_id_data(seats_ls)
                self.update_display_no_of_seats()

                # Ticket Generation Data and Window
                self.insert_ticket_info_data(seats_ls)
                new_window = Toplevel(self.ticket_button_frame)
                self.ticket_info_obj.ticket_info_class(new_window)

                self.create_cancel_button()
                global confirm_transaction
                confirm_transaction = self.confirm_transaction_window
                    
                # Reseting the selected seats and total price
                self.get_selected_seats() 
                self.get_total_price(float(self.buy_ticket_section_fare_var.get()))
            
            else:
                messagebox.showerror("Invalid", "Username or Password", parent=self.confirm_transaction_window)

        else:
            messagebox.showerror("Error", "Fields required!", parent=self.confirm_transaction_window)



    def create_cancel_button(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            # Retrieve booked seats for the given bus number and contact      
            query = "SELECT * FROM ticket_info_table where bus_no = %s AND mobile_no = %s ORDER BY ticket_id DESC LIMIT 1"
            values = (self.bus_no, self.contact_entry.get())
            cursor.execute(query, values)
            row = cursor.fetchone()         

            if row is not None:
                # book button
                self.cancel_button = ctk.CTkButton(self.footer_frame, text="CANCEL", fg_color="#35c857",  cursor="hand2", width=125, height=50, hover_color="#368e4b", font=("times new roman", 17, "bold"), command=self.create_cancel_booking_confirmation_window)
                self.cancel_button.place(x=550, y=10)
        
            connection.commit()

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def cancel_booking(self):
        if self.booking_cancellation_username_entry.get() != "" and self.booking_cancellation_password_entry.get() != "":

            if self.booking_cancellation_username_entry.get() == (self.buy_ticket_section_username_var.get() or self.buy_ticket_section_email_var.get()) and self.booking_cancellation_password_entry.get() == self.buy_ticket_section_password_var.get():

                qn = messagebox.askyesno("Cancel?", "Are you sure you want to cancel the bookings?", parent=self.confirm_cancel_window)
                if qn == 1:
                    try:
                        connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                        cursor = connection.cursor()

                        # For ckecking if the data is equivalent to [[0]*9 if i != 2 else [0] for i in range(5)]
                        query = "SELECT seat_reference_wrt_id FROM booking_id_table WHERE bus_no = %s ORDER BY booking_id DESC LIMIT 1"
                        values = (self.bus_no,)
                        cursor.execute(query, values)
                        row = cursor.fetchone()
                        if row is not None:
                            if json.loads(row[0]) == [[0]*9 if i != 2 else [0] for i in range(5)]:
                                messagebox.showerror("Error", "Not Cancel", parent=self.confirm_cancel_window)

                            else:
                                # Fetching second last seat_reference_wrt_id from booking_id_table updating the seat_reference_wrt in reference table
                                query1 = "SELECT seat_reference_wrt_id FROM booking_id_table WHERE bus_no = %s AND booking_id < (SELECT MAX(booking_id) FROM booking_id_table WHERE bus_no = %s) ORDER BY booking_id DESC LIMIT 1"
                                values1 = (self.bus_no, self.bus_no)
                                cursor.execute(query1, values1)
                                row1 = cursor.fetchone()
                                if row1 is not None:
                                    self.seat_reference_wrt_id_json = row1[0]              

                                # Fetching last booked_seats_wrt_id booking_id_table For updating the booked_seats in reference table
                                query2 = "SELECT booked_seats_wrt_id FROM booking_id_table WHERE bus_no = %s ORDER BY booking_id DESC LIMIT 1"
                                values2 = (self.bus_no,)
                                cursor.execute(query2, values2)
                                row2 = cursor.fetchone()
                                if row2 is not None:
                                    booked_seats_wrt_id_json = row2[0]
                                    # Reassiging self.booked_seats_ls for bus reference Table
                                    for i in json.loads(booked_seats_wrt_id_json):      # -> returns str
                                        if i in self.booked_seats_ls:
                                            self.booked_seats_ls.remove(i)
                                connection.commit()

                                # Updating Seat Reference table
                                query3 = "UPDATE bus_seat_bookings SET seat_reference=%s, booked_seats=%s  WHERE bus_no = %s"
                                values3 = (self.seat_reference_wrt_id_json, json.dumps(self.booked_seats_ls), self.bus_no)
                                cursor.execute(query3, values3)                

                                
                                # Deletion of data in booking_id_table from latest insertation
                                query5 = "DELETE FROM booking_id_table WHERE bus_no = %s ORDER BY booking_id DESC LIMIT 1"
                                values5 = (self.bus_no,)
                                cursor.execute(query5, values5)
                                
                                # Deletion of data in ticket_info_table from latest insertation
                                query6 = "DELETE FROM ticket_info_table WHERE bus_no = %s AND mobile_no = %s ORDER BY ticket_id DESC LIMIT 1"
                                values6 = (self.bus_no, self.contact_entry.get())
                                cursor.execute(query6, values6)
                            
                                messagebox.showinfo("Sucess", "Cancelled", parent=self.confirm_cancel_window)
                                self.confirm_cancel_window.destroy()

                    
                        connection.commit()
                        self.cancel_button.destroy()

                        # First fetch data    
                        self.seats_reference = self.fetch_seat_reference_data()
                        # Update the GUI after the cancel
                        self.update_booked_seats_gui()
                        
                        # Reset Seats Availablity
                        self.update_display_no_of_seats()       

                    except Error as e:
                        messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.confirm_cancel_window)

                    finally:
                        if connection.is_connected():
                            cursor.close()
                            connection.close()

            else:
                messagebox.showerror("Invalid", "Username or Password", parent=self.confirm_cancel_window)

        else:
            messagebox.showerror("Error", "Fields required!", parent=self.confirm_cancel_window)



    def fetch_seat_reference_data(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            # Retrieve booked seats for the given bus number
            query = "SELECT seat_reference FROM bus_seat_bookings where bus_no = %s"
            values = (self.bus_no,)
            cursor.execute(query, values)
            row = cursor.fetchone()                                    # -> returns tuple
            if row is not None:
                seats_reference_json = row[0]                          # -> returns str   
                seats_reference = json.loads(seats_reference_json)     # -> returns list
                return seats_reference
            else:
                return []

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def update_booking_data(self):
        # Updating the gui along with updating/booking data in database
        self.update_booked_seats_gui()
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            query = "UPDATE bus_seat_bookings SET booked_seats= %s, seat_reference=%s WHERE bus_no = %s"
            values = (json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), self.bus_no)
            cursor.execute(query, values)
            connection.commit()

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    ## Fetching booked seats / reference data from database
    def fetch_booked_seats(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            # Retrieve booked seats for the given bus number
            query = "SELECT booked_seats FROM bus_seat_bookings where bus_no = %s"
            values = (self.bus_no,)
            cursor.execute(query, values)
            row = cursor.fetchone()                                    # -> returns tuple
            if row is not None:
                booked_seats_ls_json = row[0]                          # -> returns str   
                booked_seats_ls = json.loads(booked_seats_ls_json)     # -> returns list
                return booked_seats_ls
            else:
                return []

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def update_booked_seats_gui(self):
        for i in range(len(self.seats_reference)):
            for j in range(len(self.seats_reference[i])):
                if self.seats_reference[i][j] == 1:             # 1 -> Selected Seats
                    self.seats_buttons[i][j].configure(fg_color="#bc0202", hover=False)
                    self.seats_reference[i][j] = 2              # 2 -> Booked Seats
                
                elif self.seats_reference[i][j] == 2:           # 2 -> Booked Seats
                    self.seats_buttons[i][j].configure(fg_color="#bc0202", hover=False)

                elif self.seats_reference[i][j] == 0:           # 0 -> Available Seats
                    self.seats_buttons[i][j].configure(fg_color="#323645", hover=False)



    # Insrt Data with respect to booking_ID
    def insert_booking_id_data(self, seat_ls):
        booked_seats_wrt_id = seat_ls   # Get selected Seats
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            # Insert inside Booking Id (Cancel) table
            query = "INSERT INTO booking_id_table (bus_no, booked_seats_wrt_id, seat_reference_wrt_id, booking_date) VALUES (%s, %s, %s, %s)"
            values = (self.bus_no, json.dumps(booked_seats_wrt_id), json.dumps(self.seats_reference), self.booking_date)
            cursor.execute(query, values)
            connection.commit()


        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()



    def update_display_no_of_seats(self):
        lengths = [len(row) for row in self.seats_reference]    # Output = [9, 9, 1, 9, 9]
        self.no_total_seats = sum(lengths)                      # Output = 37
        self.no_available_seats = 0
        self.no_booked_seats = 0

        for i in range(len(self.seats_reference)):
            for j in range(len(self.seats_reference[i])):
                if self.seats_reference[i][j] == 0:            # 0 -> Availabale Seats
                    self.no_available_seats += 1
                
                elif self.seats_reference[i][j] == 2:          # 2 -> Booked Seats
                    self.no_booked_seats += 1
        
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            query = "update details_table set available_seats = %s, seats_sold = %s, seats_booked = %s, total_seats = %s where bus_no = %s"
            values = (str(self.no_available_seats), str(self.no_booked_seats), str(self.no_booked_seats), str(self.no_total_seats), self.bus_no)
            cursor.execute(query, values)
            connection.commit()

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    


    def insert_ticket_info_data(self, seats_ls):
        selected_ones = ", ".join(seats_ls)
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            
            query = "insert into ticket_info_table (passenger_name, mobile_no, booked_date, bus_no, bus_agency, bus_type, from_place, to_place, departure_date, departure_time, seat_no, total_passenger, fare, total_price, rept_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            values = (self.buy_ticket_section_passenger_name_var.get(), self.buy_ticket_section_passenger_contact_var.get(), datetime.now().strftime("%Y-%m-%d"), self.bus_no, self.buy_ticket_section_bus_agency_var.get(),  self.bus_type.get(), self.buy_ticket_section_from_var.get(), self.buy_ticket_section_to_var.get(), self.buy_ticket_section_departure_date_var.get(), self.buy_ticket_section_departure_time_var.get(), json.dumps(seats_ls), self.buy_ticket_section_total_passenger_var.get(), self.buy_ticket_section_fare_var.get(), f"{self.total:.2f}", self.buy_ticket_section_reporting_time_var.get())
            
            cursor.execute(query, values)
            connection.commit()      

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        # Set the data for ticket generation        
        self.ticket_info_obj.info_ticket_section_passenger_name_var.set(self.buy_ticket_section_passenger_name_var.get())
        self.ticket_info_obj.info_ticket_section_passenger_contact_var.set(self.buy_ticket_section_passenger_contact_var.get())
        self.ticket_info_obj.info_ticket_section_bus_no_var.set(self.bus_no)
  
        
    
    def search_for_cancel_btn_func(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            
            query1 = "SELECT * FROM admin_details where username = %s and email = %s and password = %s"
            values1 = ( self.buy_ticket_section_username_var.get(), self.buy_ticket_section_emial_var.get(), self.buy_ticket_section_password_var.get())
            cursor.execute(query1, values1)
            row = cursor.fetchone()  
            if row is not None:

                query2 = "SELECT * FROM ticket_info_table where bus_no = %s AND mobile_no = %s ORDER BY ticket_id DESC LIMIT 1"
                values2 = (self.bus_no, self.contact_entry.get())
                cursor.execute(query2, values2)
                row = cursor.fetchone()         
                if row is not None:
                    # book button
                    self.cancel_button = ctk.CTkButton(self.footer_frame, text="CANCEL", fg_color="#35c857",  cursor="hand2", width=125, height=50, hover_color="#368e4b", font=("times new roman", 17, "bold"), command=self.create_cancel_booking_confirmation_window)
                    self.cancel_button.place(x=550, y=10)

                else:
                    messagebox.showerror("Error", "Booking is not done for cancelling", parent=self.ticket_button_frame)
            
            else:
                messagebox.showerror("Error", "Account is not created!!", parent=self.ticket_button_frame)

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.ticket_button_frame)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    @staticmethod
    def destroy_confirm_window():
        confirm_transaction.destroy()