## Rijan Regmi
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import customtkinter as ctk
from datetime import datetime
from admin_ticket_info import Ticket_Info

class Ticket:
    def __init__(self):       
         # Variables #
        self.buy_ticket_section_bus_no_var = StringVar()
        self.buy_ticket_section_total_passenger_var = StringVar()
        self.buy_ticket_section_bus_agency_var = StringVar()
        self.buy_ticket_section_departure_date_var = StringVar()
        self.buy_ticket_section_departure_time_var = StringVar()
        self.buy_ticket_section_from_var = StringVar()
        self.buy_ticket_section_to_var = StringVar()
        self.buy_ticket_section_fare_var = StringVar()
        self.buy_ticket_section_reporting_time_var = StringVar()
        self.bus_agency_name = StringVar()
        self.bus_type = StringVar()

    # Ticket Details #
    def buy_ticket(self, parent_frame):
        # Ticket button frame #
        self.ticket_button_frame = Frame(parent_frame, bg="lightblue")
        self.ticket_button_frame.place(x=0, y=0, width=1253, height=551)

        # Title Label #
        buy_ticket_label = Label(self.ticket_button_frame, text="Buy Ticket", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        buy_ticket_label.place(x=0, y=0, width=1253, height=50)
        
        # Logo #
        top_left_logo = Image.open("Travel-Management-System/System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(buy_ticket_label, image=self.top_left_logo)
        label_top_left_logo.place(x=5, y=0, width=40, height=40)

        ticket_details_frame = LabelFrame(self.ticket_button_frame, text= "Ticket Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
        ticket_details_frame.place(x=5, y=55, width=375, height=490)


        self.buy_ticket_section_passenger_name_var = StringVar()
        self.buy_ticket_section_passenger_contact_var = StringVar()


        passenger_name_label = Label(ticket_details_frame, text="Passenger Name:", bg="lightblue", font=("Arial", 12, "bold"))
        passenger_name_label.place(x=5, y=10)
        self.passenger_name_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_passenger_name_var)
        self.passenger_name_entry.place(x=150, y=10, width=200, height=30)
###
        

        contact_label = Label(ticket_details_frame, text="Mobile Number:", bg="lightblue", font=("Arial", 12, "bold"))
        contact_label.place(x=5, y=50)
        self.contact_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_passenger_contact_var)
        self.contact_entry.place(x=150, y=50, width=200, height=30)
        
        bus_no_label = Label(ticket_details_frame, text="Bus No:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_no_label.place(x=5, y=90)
        bus_no_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_bus_no_var)
        bus_no_entry.place(x=150, y=90, width=200, height=30)

        bus_agency_label = Label(ticket_details_frame, text="Bus Agency:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_agency_label.place(x=5, y=130)
        bus_agency_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_bus_agency_var)
        bus_agency_entry.place(x=150, y=130, width=200, height=30)

        departure_date_label = Label(ticket_details_frame, text="Departure Date:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_date_label.place(x=5, y=170)
        departure_date_entry = DateEntry(ticket_details_frame, selectmode="day", cursor="hand2", state="readonly", font=("Arial", 12, "bold"), date_pattern="yyyy-mm-dd", textvariable=self.buy_ticket_section_departure_date_var)
        departure_date_entry.place(x=150, y=170, width=200, height=30)
        
        departure_time_label = Label(ticket_details_frame, text="Departure Time:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_time_label.place(x=5, y=210)
        departure_time_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_departure_time_var)
        departure_time_entry.place(x=150, y=210, width=200, height=30)

        from_label = Label(ticket_details_frame, text="From:", font=("Arial", 12, "bold"), bg="lightblue")
        from_label.place(x=5, y=250)
        combo_box_from = ttk.Combobox(ticket_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.buy_ticket_section_from_var)
        combo_box_from["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet"]
        combo_box_from.current(0)
        combo_box_from.place(x=150, y=250, width=200, height=30)
        

        to_label = Label(ticket_details_frame, text="To:", font=("Arial", 12, "bold"), bg="lightblue")
        to_label.place(x=5, y=290)
        combo_box_to = ttk.Combobox(ticket_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.buy_ticket_section_to_var)
        combo_box_to["values"] = ("Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet")
        combo_box_to.current(0)
        combo_box_to.place(x=150, y=290, width=200, height=30)
        
        fare_label = Label(ticket_details_frame, text="Fare (NPR./seat):", bg="lightblue", font=("Arial", 12, "bold"))
        fare_label.place(x=5, y=330)
        self.buy_ticket_section_fare_var.set("0.0")
        fare_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_fare_var)
        fare_entry.place(x=150, y=330, width=200, height=30)
        
        total_passenger_label = Label(ticket_details_frame, text="Total Passengers:", bg="lightblue", font=("Arial", 12, "bold"))
        total_passenger_label.place(x=5, y=370)
        self.buy_ticket_section_total_passenger_var.set("0")
        self.total_passenger_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_total_passenger_var)
        self.total_passenger_entry.place(x=150, y=370, width=200, height=30)

        reporting_time_label = Label(ticket_details_frame, text="Reporting Time:", bg="lightblue", font=("Arial", 12, "bold"))
        reporting_time_label.place(x=5, y=410)
        reporting_time_entry = ttk.Entry(ticket_details_frame, font=("Arial", 12, "bold"), textvariable=self.buy_ticket_section_reporting_time_var)
        reporting_time_entry.place(x=150, y=410, width=200, height=30)

        ## -------------------Bus Seats Booking----------------------
        bus_info_frame = Frame(self.ticket_button_frame, bg="#182356", bd=3, relief=RIDGE)
        bus_info_frame.place(x=390, y=70, width=350, height=75)


        self.bus_agency_name = StringVar()
        self.bus_type = StringVar()

        bus_agency_label = Label(bus_info_frame, textvariable=self.bus_agency_name, bg="#182356", fg="white", font=("Arial", 17, "bold"))
        bus_agency_label.place(x=5, y=5)
        bus_agency_label = Label(bus_info_frame, textvariable=self.bus_type, bg="#182356", fg="white", font=("Arial", 11, "bold"))
        bus_agency_label.place(x=7, y=40)
        
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

        self.seats = [[0] * 9 for _ in range(5)]
        self.seats_buttons = []

        # A
        # Row 1 #
        for i in range(5):
            row_buttons = []
            for j in range(9):
                if i == 0 and j == 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{2}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)

                elif i == 0 and j < 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{17-2*j}", fg_color="#323645",cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))    
                    
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)
            

            # Row 2
                elif i == 1 and j == 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{1}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)

                elif i == 1 and j < 8:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{18-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)            

            # Row 3    
                elif i == 2 and j == 0:
                    self.buttons = ctk.CTkButton(self.bus_seats_frame, text=f"A{19}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    self.buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(self.buttons)


            # Row 4
                elif i == 3 and j < 9:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"B{17-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)


            # Row 5
                elif i == 4 and j < 9:
                    buttons = ctk.CTkButton(self.bus_seats_frame, text=f"B{18-2*j}", fg_color="#323645",  cursor="hand2", width=70, height=40, hover_color="#6d7491", font=("Arial", 12, "bold"))
                    buttons.grid(row=i, column=j, padx=7, pady=10)
                    row_buttons.append(buttons)
            
            self.seats_buttons.append(row_buttons)


        ## Footer Frame
        self.footer_frame = Frame(self.ticket_button_frame, bg="gray12", bd=3, relief=RIDGE)
        self.footer_frame.place(x=390, y=465, width=850, height=75)

        selected_seats_title_label = Label(self.footer_frame, text="Selected Seat(s)", fg="white", bg="gray12", font=("Arial", 15, "bold"))
        selected_seats_title_label.place(x=15, y=5)

        self.selected_ones = "Not selected"
        self.selected_seats = Label(self.footer_frame, text=self.selected_ones, fg="white", bg="gray12", font=("Arial", 12, "bold"))
        self.selected_seats.place(x=15, y=30)

        total_price_title_label = Label(self.footer_frame, text="Total Price", fg="white", bg="gray12", font=("Arial", 15, "bold"))
        total_price_title_label.place(x=400, y=5)

        self.total = f"{0:.2f}"
        self.total_price = Label(self.footer_frame, text=f"NPR. {self.total}", fg="white", bg="gray12", font=("Arial", 12, "bold"))
        self.total_price.place(x=405, y=30)

        
        # initializating object
        self.obj = Ticket_Info()



        # book button
        book_now_button = ctk.CTkButton(self.footer_frame, text="BOOK NOW", fg_color="#35c857",  cursor="hand2", width=125, height=50, hover_color="#368e4b", font=("times new roman", 15, "bold"), command=self.ticket_info_func)
        book_now_button.place(x=700, y=10)



    def ticket_info_func(self):
        new_window = Toplevel(self.ticket_button_frame)
        self.obj.ticket_info_class(new_window)
        


        
