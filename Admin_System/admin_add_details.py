from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import customtkinter as ctk
from datetime import datetime
class Add_details():
    def add_details(self,parent_frame):
        # Add details button Frame
        self.add_button_frame = Frame(parent_frame, bg="lightblue")
        self.add_button_frame.place(x=0, y=0, width=1253, height=551)

        #Add_details_label
        add_details_label = Label(self.add_button_frame, text="Add Details", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        add_details_label.place(x=0, y=0, width=1253, height=50)

        #System_logo
        top_left_logo = Image.open("Travel-Management-System/System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(add_details_label, image=self.top_left_logo)
        label_top_left_logo.place(x=5, y=0, width=40, height=40)

        #Details_enter_frame
        add_details_frame = LabelFrame(self.add_button_frame, text= "All Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue", bd=5, relief=RIDGE)
        add_details_frame.place(x=5, y=55, width=1243, height=250)
        

        # Variables
        self.bus_no_var = StringVar()
        self.from_var = StringVar()
        self.to_var = StringVar()
        self.departure_date_var = StringVar()
        self.departure_time_var = StringVar()
        self.bus_agency_name = StringVar()
        self.station_var = StringVar()
        self.bus_type_var = StringVar()
        self.fare_var = StringVar()
        self.reporting_time_var = StringVar()
        self.added_date_var = StringVar()
        self.available_seats_var = StringVar()
        self.seats_sold_var = StringVar()
        self.seats_booked_var = StringVar()
        self.total_seats_var = StringVar()

        #Labels_and_entries
        bus_no_label = Label(add_details_frame, text="Bus No:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_no_label.place(x=5, y=10)
        self.bus_no_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.bus_no_var)
        self.bus_no_entry.place(x=150, y=10, width=200, height=30)

        from_label = Label(add_details_frame, text="From:", font=("Arial", 12, "bold"), bg="lightblue")
        from_label.place(x=5, y=50)
        self.combo_box_from = ttk.Combobox(add_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.from_var)
        self.combo_box_from["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet", "Dhangadi", "Biratnagar", "Dailekh"]
        self.combo_box_from.current(0)
        self.combo_box_from.place(x=150, y=50, width=200, height=30)

        to_label = Label(add_details_frame, text="To:", font=("Arial", 12, "bold"), bg="lightblue")
        to_label.place(x=5, y=90)
        self.combo_box_to = ttk.Combobox(add_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.to_var)
        self.combo_box_to["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet", "Dhangadi", "Biratnagar", "Dailekh"]
        self.combo_box_to.current(0)
        self.combo_box_to.place(x=150, y=90, width=200, height=30)

        departure_date_label = Label(add_details_frame, text="Departure Date:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_date_label.place(x=5, y=130)
        self.departure_date_entry = DateEntry(add_details_frame, selectmode="day", cursor="hand2", state="readonly", font=("Arial", 12, "bold"), textvariable=self.departure_date_var, date_pattern="yyyy-mm-dd")
        self.departure_date_entry.place(x=150, y=130, width=200, height=30)
        
        departure_time_label = Label(add_details_frame, text="Departure Time:", bg="lightblue", font=("Arial", 12, "bold"))
        departure_time_label.place(x=5, y=170)
        self.departure_time_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.departure_time_var)
        self.departure_time_entry.place(x=150, y=170, width=200, height=30)

        bus_agency_name_label = Label(add_details_frame, text="Bus Agency:", bg="lightblue", font=("Arial", 12, "bold"))
        bus_agency_name_label.place(x=375, y=10)
        self.bus_agency_name_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.bus_agency_name)
        self.bus_agency_name_entry.place(x=520, y=10, width=200, height=30)

        station_label = Label(add_details_frame, text="Station:", bg="lightblue", font=("Arial", 12, "bold"))
        station_label.place(x=375, y=50)
        self.station_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.station_var)
        self.station_entry.place(x=520, y=50, width=200, height=30)

        type_label = Label(add_details_frame, text="Type:", bg="lightblue", font=("Arial", 12, "bold"))
        type_label.place(x=375, y=90)
        self.type_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.bus_type_var)
        self.type_entry.place(x=520, y=90, width=200, height=30)

        fare_label = Label(add_details_frame, text="Fare (Rs):", bg="lightblue", font=("Arial", 12, "bold"))
        fare_label.place(x=375, y=130)
        self.fare_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.fare_var)
        self.fare_entry.place(x=520, y=130, width=200, height=30)
        
        
        reporting_time_label = Label(add_details_frame, text="Reporting Time:", bg="lightblue", font=("Arial", 12, "bold"))
        reporting_time_label.place(x=375, y=170)
        self.reporting_time_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.reporting_time_var)
        self.reporting_time_entry.place(x=520, y=170, width=200, height=30)

        added_date_label = Label(add_details_frame, text="Date:", bg="lightblue", font=("Arial", 12, "bold"))
        added_date_label.place(x=745, y=10)
        self.added_date_entry = DateEntry(add_details_frame, selectmode="day", cursor="hand2", state="readonly", font=("Arial", 12, "bold"), textvariable=self.added_date_var, date_pattern="yyyy-mm-dd")
        self.added_date_entry.place(x=890, y=10, width=200, height=30)

        available_seats_label = Label(add_details_frame, text="Available Seats:", bg="lightblue", font=("Arial", 12, "bold"))
        available_seats_label.place(x=745, y=50)
        self.available_seats_var.set("37")
        self.available_seats_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.available_seats_var)
        self.available_seats_entry.place(x=890, y=50, width=200, height=30)
        
        seats_sold_label = Label(add_details_frame, text="Seats Sold:", bg="lightblue", font=("Arial", 12, "bold"))
        seats_sold_label.place(x=745, y=90)
        self.seats_sold_var.set("0")
        self.seats_sold_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.seats_sold_var)
        self.seats_sold_entry.place(x=890, y=90, width=200, height=30)
        
        seats_booked_label = Label(add_details_frame, text="Seats Booked:", bg="lightblue", font=("Arial", 12, "bold"))
        seats_booked_label.place(x=745, y=130)
        self.seats_booked_var.set("0")
        self.seats_booked_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.seats_booked_var)
        self.seats_booked_entry.place(x=890, y=130, width=200, height=30)
        
        total_seats_label = Label(add_details_frame, text="Total Seats:", bg="lightblue", font=("Arial", 12, "bold"))
        total_seats_label.place(x=745, y=170)
        self.total_seats_var.set("37")
        self.total_seats_entry = ttk.Entry(add_details_frame, font=("Arial", 12, "bold"), textvariable=self.total_seats_var)
        self.total_seats_entry.place(x=890, y=170, width=200,height=30)


        # Details Table
        details_table_frame = Frame(self.add_button_frame, bg="lightblue", bd = 5, relief=RIDGE)
        details_table_frame.place(x=5, y=378, width=1243, height=171)

        # Scroll bar
        scroll_bar_x = ttk.Scrollbar(details_table_frame, orient=HORIZONTAL, cursor="hand2")
        scroll_bar_y = ttk.Scrollbar(details_table_frame, orient=VERTICAL, cursor="hand2")
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
 
        self.details_table = ttk.Treeview(details_table_frame, column= ("bus_no", "from", "to", "departure_date", "departure_time", "bus_agency", "station", "type", "fare", "reporting_time", "no_seat_available", "seats_sold", "seats_booked", "total_seats", "date"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.config(command=self.details_table.xview)
        scroll_bar_y.config(command=self.details_table.yview)

        self.details_table.heading("bus_no", text="Bus No")
        self.details_table.heading("bus_agency", text="Bus Agency")
        self.details_table.heading("station", text="Station")
        self.details_table.heading("no_seat_available", text="Available Seats")
        self.details_table.heading("departure_date", text="Departure Date")
        self.details_table.heading("departure_time", text="Departure Time")
        self.details_table.heading("from", text="From")
        self.details_table.heading("to", text="To")
        self.details_table.heading("fare", text="Fare (Rs)")
        self.details_table.heading("type", text="Type")
        self.details_table.heading("reporting_time", text="Reporting Time")
        self.details_table.heading("seats_sold", text="Seats Sold")
        self.details_table.heading("seats_booked", text="Seats Booked")
        self.details_table.heading("total_seats", text="Total Seats")
        self.details_table.heading("date", text="Date")
        
        self.details_table["show"] = "headings"

        self.details_table.column("bus_no", width=125)
        self.details_table.column("bus_agency", width=125)
        self.details_table.column("station", width=125)
        self.details_table.column("no_seat_available", width=125)
        self.details_table.column("departure_date", width=125)
        self.details_table.column("departure_time", width=125)
        self.details_table.column("from", width=125)
        self.details_table.column("to", width=125)
        self.details_table.column("fare", width=125)
        self.details_table.column("type", width=125)
        self.details_table.column("reporting_time", width=125)
        self.details_table.column("seats_sold", width=125)
        self.details_table.column("seats_booked", width=125)
        self.details_table.column("total_seats", width=125)
        self.details_table.column("date", width=125)

        self.details_table.pack(fill=BOTH, expand=True)

        self.details_table.bind("<Enter>", self.details_table.config(cursor="hand2"))


        # CRUD Buttons
        button_frame = Frame(self.add_button_frame, bg="lightblue", bd = 5, relief=RIDGE)
        button_frame.place(x=5, y=305, width=1243, height=72)

        add_data_button = Button(button_frame, text="Add", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold")
        add_data_button.place(x=0, y=0, width=200, height=61)
        
        update_data_button = Button(button_frame, text="Update", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold")
        update_data_button.place(x=201, y=0, width=200, height=61)
        
        delete_data_button = Button(button_frame, text="Delete", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold")
        delete_data_button.place(x=402, y=0, width=200, height=61)
        
        clear_data_button = Button(button_frame, text="Clear", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold")
        clear_data_button.place(x=603, y=0, width=200, height=61)

        restore_data_button = Button(button_frame, text="Restore", font=("Arial", 15, "bold"),bg="blue", fg="white", cursor="hand2", highlightthickness=5, activebackground="darkblue", activeforeground="gold")
        restore_data_button.place(x=804, y=0, width=200, height=61)
        
        reset_data_button = Button(button_frame, text="Reset", font=("Arial", 15, "bold"),bg="red", fg="white", cursor="hand2", bd=10, highlightthickness=5, activebackground="orange", activeforeground="gray12")
        reset_data_button.place(x=1032, y=0, width=200, height=61)

     


