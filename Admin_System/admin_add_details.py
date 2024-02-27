from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime
import json

class AddDetails:
    ## Add Details
    def add_details(self, parent_frame): 
        # Add details button Frame
        self.add_button_frame = Frame(parent_frame, bg="lightblue")
        self.add_button_frame.place(x=0, y=0, width=1253, height=551)
        
        add_details_label = Label(self.add_button_frame, text="Add Details", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        add_details_label.place(x=0, y=0, width=1253, height=50)

        top_left_logo = Image.open("System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(add_details_label, image=self.top_left_logo)
        label_top_left_logo.place(x=5, y=0, width=40, height=40)

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
        self.available_seats_var = StringVar()
        self.seats_sold_var = StringVar()
        self.seats_booked_var = StringVar()
        self.total_seats_var = StringVar()
        self.added_date_var = StringVar()


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
        self.total_seats_entry.place(x=890, y=170, width=200, height=30)

        # Details Table
        details_table_frame = Frame(self.add_button_frame, bg="lightblue", bd = 5, relief=RIDGE)
        details_table_frame.place(x=5, y=378, width=1243, height=171)

        # Scroll bar
        scroll_bar_x = ttk.Scrollbar(details_table_frame, orient=HORIZONTAL, cursor="hand2")
        scroll_bar_y = ttk.Scrollbar(details_table_frame, orient=VERTICAL, cursor="hand2")

        self.details_table = ttk.Treeview(details_table_frame, column= ("bus_no", "from", "to", "departure_date", "departure_time", "bus_agency", "station", "type", "fare", "reporting_time", "no_seat_available", "seats_sold", "seats_booked", "total_seats", "date"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.details_table.xview)
        scroll_bar_y.config(command=self.details_table.yview)

        self.details_table.heading("#0")
        self.details_table.heading("bus_no", text="Bus No")
        self.details_table.heading("from", text="From")
        self.details_table.heading("to", text="To")
        self.details_table.heading("bus_agency", text="Bus Agency")
        self.details_table.heading("station", text="Station")
        self.details_table.heading("no_seat_available", text="Available Seats")
        self.details_table.heading("departure_date", text="Departure Date")
        self.details_table.heading("departure_time", text="Departure Time")
        self.details_table.heading("fare", text="Fare (Rs)")
        self.details_table.heading("type", text="Type")
        self.details_table.heading("reporting_time", text="Reporting Time")
        self.details_table.heading("seats_sold", text="Seats Sold")
        self.details_table.heading("seats_booked", text="Seats Booked")
        self.details_table.heading("total_seats", text="Total Seats")
        self.details_table.heading("date", text="Date")

        self.details_table["show"] = "headings"

        self.details_table.column("#0", width=0, stretch=NO)
        self.details_table.column("bus_no", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("from", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("to", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("departure_date", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("departure_time", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("bus_agency", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("station", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("fare", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("type", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("reporting_time", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("no_seat_available", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("seats_sold", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("seats_booked", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("total_seats", width=150, anchor=CENTER, minwidth=150)
        self.details_table.column("date", width=150, anchor=CENTER, minwidth=150)

        self.details_table.pack(fill=BOTH, expand=True)
        self.details_table.bind("<Enter>", self.details_table.config(cursor="hand2"))


        self.fetch_data()
        self.style_func()


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



    ### Add Details Functions
    def add_details_db(self):        
        if self.bus_no_entry.get() == "":
        # if self.bus_no_entry.get() == "" or self.combo_box_from.get() or self.combo_box_to.get() == "" or self.departure_date_entry.get() == "" or self.departure_time_entry.get() == "" or self.bus_agency_name_entry.get() == "" or self.station_entry.get() == "" or self.type_entry.get() == "" or self.fare_entry.get() == "" or self.reporting_time_entry.get() == "" or self.added_date_entry.get() == "" or self.available_seats_entry.get() == "" or self.seats_sold_entry.get() == "" or self.seats_booked_entry.get() == "" or self.total_seats_entry.get() == "":
            messagebox.showerror("Error", "'Bus no' fields required", parent=self.add_button_frame)

        elif self.combo_box_from.get() == "Select" or self.combo_box_to.get() == "Select":
            messagebox.showerror("Error", "Invalid input 'Select'", parent=self.add_button_frame)

        else:
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db", port="3306")
                
                my_cursor = connection.cursor()
                query1 = "insert into details_table values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                
                values1 = (self.bus_no_entry.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.departure_date_entry.get(), self.departure_time_entry.get(), self.bus_agency_name_entry.get(), self.station_entry.get(), self.type_entry.get(), self.fare_entry.get(), self.reporting_time_entry.get(), self.available_seats_entry.get(), self.seats_sold_entry.get(), self.seats_booked_entry.get(), self.total_seats_entry.get(), self.added_date_entry.get())
                my_cursor.execute(query1, values1)

                # Insert into Seats_Referenence Table
                self.seats_reference = [[0]*9 if i != 2 else [0] for i in range(5)]
                self.booked_seats_ls = []
                query2 = "INSERT INTO bus_seat_bookings (bus_no, booked_seats, seat_reference, added_datE) VALUES (%s, %s, %s, %s)"
                values2 = (self.bus_no_entry.get(), json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), self.added_date_entry.get())
                my_cursor.execute(query2, values2)
                connection.commit()

                # Insert inside booking_id table (/Cancel Table)
                query3 = "INSERT INTO booking_id_table (bus_no, booked_seats_wrt_id, seat_reference_wrt_id, booking_date) VALUES (%s, %s, %s, %s)"
                values3 = (self.bus_no_entry.get(), json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), self.added_date_entry.get())
                my_cursor.execute(query3, values3)
                connection.commit()

                self.fetch_data()
                messagebox.showinfo("Success", "Record has been inserted!", parent=self.add_button_frame)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)

            finally:
                if connection.is_connected():
                    my_cursor.close()
                    connection.close()

            self.style_func()
    


    # Fetch data from database to the Hospital details table
    def fetch_data(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            my_cursor = connection.cursor()
            my_cursor.execute("select * from details_table")
            rows = my_cursor.fetchall()
            
            # Clear the tree view before inserting new data
            self.details_table.delete(*self.details_table.get_children())
            # Insert new data into the tree view
            if len(rows) != 0:
                for i in rows:
                    self.details_table.insert("", END, values=i)
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)    
        
        finally:
            connection.commit()
            if connection.is_connected():
                my_cursor.close()
                connection.close()



    # Click the row to copy data to the blanks
    def get_cursor(self, event=""):
        if self.details_table.selection():
            cursor_row = self.details_table.focus()
            content = self.details_table.item(cursor_row)
            self.details_table.config(cursor="hand2")
            row = content["values"]
    
            if len(row) >= 15:
                self.bus_no_var.set(row[0]),
                self.from_var.set(row[1]),
                self.to_var.set(row[2]), 
                self.departure_date_var.set(row[3]),
                self.departure_time_var.set(row[4]),
                self.bus_agency_name.set(row[5]),
                self.station_var.set(row[6]),
                self.bus_type_var.set(row[7]),
                self.fare_var.set(row[8]),
                self.reporting_time_var.set(row[9]),
                self.available_seats_var.set(row[10]),
                self.seats_sold_var.set(row[11]),
                self.seats_booked_var.set(row[12]),
                self.total_seats_var.set(row[13]),
                self.added_date_var.set(row[14])



    def update_data(self):
        if self.bus_no_var.get() == "":
            messagebox.showerror("Error", "'Bus No' field are recquired", parent=self.add_button_frame)
        
        else:
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                my_cursor = connection.cursor()
                my_cursor.execute("select * from details_table where bus_no = %s", (self.bus_no_var.get(),))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Add the data first to perform updation", parent=self.add_button_frame)

                else:
                    query = "update details_table set from_place = %s, to_place = %s, departure_date = %s, departure_time = %s, bus_agency = %s, station = %s, bus_type = %s, fare = %s, reporting_time = %s, available_seats = %s, seats_sold = %s, seats_booked = %s, total_seats = %s, added_date = %s where bus_no = %s"
                    
                    values = (self.combo_box_from.get(), self.combo_box_to.get(), self.departure_date_entry.get(), self.departure_time_entry.get(), self.bus_agency_name_entry.get(), self.station_entry.get(), self.type_entry.get(), self.fare_entry.get(), self.reporting_time_entry.get(), self.available_seats_entry.get(), self.seats_sold_entry.get(), self.seats_booked_entry.get(), self.total_seats_entry.get(), self.added_date_entry.get(), self.bus_no_entry.get())
                    
                    my_cursor.execute(query, values)
                    connection.commit()
                    self.fetch_data()
                    messagebox.showinfo("Successfully Updated", "Record has been updated!", parent=self.add_button_frame)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)

            finally:
                if connection.is_connected():
                        my_cursor.close()
                        connection.close()   
            self.style_func()



    def delete_data(self):
        if self.details_table.selection():      
            try:
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                my_cursor = connection.cursor()
                query = "delete from details_table where bus_no = %s"
                values = (self.bus_no_var.get(),)
                my_cursor.execute(query, values)

                connection.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Successfully Deleted", "Record has been deleted!", parent=self.add_button_frame)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)   
            finally:
                if connection.is_connected():
                    my_cursor.close()
                    connection.close()
        else:
            messagebox.showerror("Error", "Selection of the row is required", parent=self.add_button_frame)
        self.style_func()



    def clear_data(self):
        self.bus_no_var.set(""),
        self.from_var.set(""),
        self.to_var.set(""),
        self.departure_date_var.set(""),
        self.departure_time_var.set(""),
        self.bus_agency_name.set(""),
        self.station_var.set(""),
        self.bus_type_var.set(""),
        self.fare_var.set(""),
        self.reporting_time_var.set(""),
        self.added_date_var.set(""),
        self.available_seats_var.set(""),
        self.seats_sold_var.set(""),
        self.seats_booked_var.set(""),
        self.total_seats_var.set("")

        self.details_table.selection_remove(self.details_table.selection())
        self.style_func()



    # Restore the data of Bus in Database
    def restore_data(self):
        if self.details_table.selection():
            if self.bus_no_entry.get() == "":
                messagebox.showerror("Error", "'Bus No' field are recquired", parent=self.add_button_frame)

            else: 
                try:
                    connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
                    my_cursor = connection.cursor()
                    
                    # Check if the bus_no is present or not in bus_seat_bookings
                    query = "select * from bus_seat_bookings where bus_no = %s"
                    values = (self.bus_no_var.get(),)
                    my_cursor.execute(query, values)
                    row = my_cursor.fetchone()

                    if row is not None:
                        # Update Seats in Details Table
                        query1 = "update details_table set available_seats = %s, seats_sold = %s, seats_booked = %s, total_seats = %s, added_date = %s where bus_no = %s"
                        values1 = ("37", "0", "0", "37", datetime.now().strftime("%Y-%m-%d"), self.bus_no_var.get())
                        my_cursor.execute(query1, values1)

                        # Update Seats References as well
                        self.seats_reference = [[0]*9 if i != 2 else [0] for i in range(5)]
                        self.booked_seats_ls = []
                        query2 = "update bus_seat_bookings set booked_seats = %s, seat_reference = %s, added_date = %s where bus_no = %s"
                        values2 = (json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), datetime.now().strftime("%Y-%m-%d"), self.bus_no_entry.get())
                        my_cursor.execute(query2, values2)

                        # Deleting Booking Id (Cancel) table with respective bus no Seats References as well
                        query3 = "delete from booking_id_table where bus_no = %s"
                        values3 = (self.bus_no_var.get(),)
                        my_cursor.execute(query3, values3)


                        # Insert inside Booking Id (Cancel) table
                        query4 = "INSERT INTO booking_id_table (bus_no, booked_seats_wrt_id, seat_reference_wrt_id, booking_date) VALUES (%s, %s, %s, %s)"
                        values4 = (self.bus_no_entry.get(), json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), datetime.now().strftime("%Y-%m-%d"))
                        my_cursor.execute(query4, values4)

                        # Deleting ticket_info_table
                        query5 = "delete from ticket_info_table where bus_no = %s"
                        values5 = (self.bus_no_var.get(),)
                        my_cursor.execute(query5, values5)
            
                    else:
                        # Update Seats in Details Table    
                        query1 = "update details_table set available_seats = %s, seats_sold = %s, seats_booked = %s, total_seats = %s, added_date = %s where bus_no = %s"
                        values1 = ("37", "0", "0", "37", datetime.now().strftime("%Y-%m-%d"), self.bus_no_var.get())
                        my_cursor.execute(query1, values1)

                        # Update Seats References as well
                        self.seats_reference = [[0]*9 if i != 2 else [0] for i in range(5)]
                        self.booked_seats_ls = []
                        query2 = "INSERT INTO bus_seat_bookings (bus_no, booked_seats, seat_reference, added_date) VALUES (%s, %s, %s, %s)"
                        values2 = (self.bus_no_entry.get(), json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), datetime.now().strftime("%Y-%m-%d"))
                        my_cursor.execute(query2, values2)

                        # Insert inside Booking Id (Cancel) table
                        query3 = "INSERT INTO booking_id_table (bus_no, booked_seats_wrt_id, seat_reference_wrt_id, booking_date) VALUES (%s, %s, %s, %s)"
                        values3 = (self.bus_no_entry.get(), json.dumps(self.booked_seats_ls), json.dumps(self.seats_reference), datetime.now().strftime("%Y-%m-%d"))
                        my_cursor.execute(query3, values3)

                    connection.commit()
                    messagebox.showinfo("Successfully Restore", "All records have been restored regarding seats and references!", parent=self.add_button_frame)
                    
                    # Copy value from database to entries
                    query = "select available_seats, seats_sold, seats_booked, total_seats, added_date from details_table where bus_no = %s"
                    values = (self.bus_no_var.get(),)
                    my_cursor.execute(query, values)
                    row = my_cursor.fetchone()
                    if row is not None:
                        self.available_seats_var.set(row[0])
                        self.seats_booked_var.set(row[1])
                        self.seats_sold_var.set(row[2])
                        self.total_seats_var.set(row[3])
                        self.added_date_var.set(row[4])

                    connection.commit()
                    self.fetch_data()

                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)   
                finally:
                    if connection.is_connected():
                        my_cursor.close()
                        connection.close()
        else:
            messagebox.showerror("Error", "Selection of the row is required", parent=self.add_button_frame)
        self.style_func()



    # Reseting all data
    def reset_all_data(self):
        try:
            
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            my_cursor = connection.cursor()

            open_main = messagebox.askyesno("Are you sure?", "All the data will be erased.", parent=self.add_button_frame)

            if open_main == 1:
                query = "delete from details_table"
                my_cursor.execute(query)

                connection.commit()
                self.fetch_data()
                self.clear_data()
                messagebox.showinfo("Successfully Reset", "All records have been deleted!", parent=self.add_button_frame)
   

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.add_button_frame)   
        finally:
            if connection.is_connected():
                my_cursor.close()
                connection.close()
        self.style_func()



    # Style
    def style_func(self):
        # Add Style
        self.style = ttk.Style()

        # Configure the treeview colors 
        self.style.configure("Treeview.Heading", font=('Arial', 10, 'bold'), foreground="black")
        self.style.configure("Treeview", font=('Arial', 9), rowheight=25)

        # Change the selected color
        self.style.map("Treeview", background=[("selected", "#347083")])

        # Create Striped rows
        self.details_table.tag_configure("oddrow", background="white")
        self.details_table.tag_configure("evenrow", background="#c5e3ec")

        # Apply tags to alternate rows
        for i, row in enumerate(self.details_table.get_children()):
            if i % 2 == 0:
                self.details_table.item(row, tags=("evenrow",))
            else:
                self.details_table.item(row, tags=("oddrow",))

