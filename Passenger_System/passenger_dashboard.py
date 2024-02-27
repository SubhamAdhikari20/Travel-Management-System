from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import ctypes
import customtkinter as ctk
from datetime import datetime

from passenger_buy_tickets import Ticket

myappid = 'mycompany.myproduct.subproduct.version'       # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Travel:
    def __init__(self, root):
        self.main_window = root
        self.main_window.title("Travel Managemet System")
        self.main_window.geometry("1465x740+0+0")
        self.main_window.iconbitmap("System_Images/title_logo.ico")
        self.main_window.minsize(1465, 740)


        global primary
        primary = self.main_window

        # Variabels for account
        self.dashboard_section_fname_var = StringVar()
        self.dashboard_section_lname_var = StringVar()
        self.dashboard_section_contact_var = StringVar()
        self.dashboard_section_username_var = StringVar()
        self.dashboard_section_email_var = StringVar()
        self.dashboard_section_password_var = StringVar()
        self.dashboard_section_confirm_password_var = StringVar()
        
        
        ### ------------------------------Title---------------------------------
        title_label = Label(self.main_window, text="Welcome to Yatru Travels" , font=("Arial", 30, "bold"), bd=5, relief=RIDGE, fg="gold",bg="gray12")
        title_label.place(x=0, y=140, width=1465, height=50)

        # Show time 
        def show_time():
            now = datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            day_letter = now.strftime("%A")
            date_format = f"    {year}/{month}/{day}, {day_letter}"
            time_str = now.strftime("%I:%M:%S %p")
            time_label.config(text=time_str + date_format)
            time_label.after(1000, show_time)

        time_label = Label(title_label, font=("Arial", 15, "bold"), bd=0, relief=RIDGE, fg="gold",bg="gray12")
        time_label.place(x=7, y=7)
        show_time()

        # Top image
        top_img = Image.open("System_Images/top_img2.jpg")
        top_img = top_img.resize((1465, 740), Image.LANCZOS) 
        self.top_img = ImageTk.PhotoImage(top_img)
        label_top_img = Label(self.main_window, image=self.top_img)
        label_top_img.place(x=0, y=0, width=1465, height=140)
        
        # Top left image/logo
        top_left_img = Image.open("System_Images/logo.png")
        top_left_img = top_left_img.resize((200, 140), Image.LANCZOS) 
        self.top_left_img = ImageTk.PhotoImage(top_left_img)
        label_top_left_img = Label(self.main_window, image=self.top_left_img, relief=RIDGE)
        label_top_left_img.place(x=0, y=0, width=200, height=140)

        ##-------------------------------Body Frame----------------------------

        self.body_frame = Frame(self.main_window, bg="lightgreen")
        self.body_frame.place(x=0, y=190, width=1465, height=561)   

        ##-------------------------------Main Frame----------------------------     
        self.main_frame = Frame(self.body_frame, bg="lightblue", bd = 5, relief=RIDGE)
        self.main_frame.place(x=200, y=0, width=1263, height=561)

        ## -------------------------------Menu----------------------------------
        # Menu Frame
        menu_frame = Frame(self.body_frame, bg="blue")
        menu_frame.place(x=0, y=0, width=200, height=183)

        # Menu Frame and Label      
        menu_top_frame = Frame(menu_frame, bg="lightblue", bd = 5, relief=RIDGE)
        menu_top_frame.place(x=0, y=0,  width=200, height=70)

        menu_top_label = Label(menu_top_frame, text="MENU", font=("Arial", 25, "bold"), bg="gray17", fg="gold", padx=20)
        menu_top_label.place(x=0, y=0,  width=190, height=59)

        #Button Frame
        menu_button_frame = Frame(menu_frame, bg="white", bd = 5, relief=RIDGE, highlightbackground="gray17")
        menu_button_frame.place(x=0, y=70, width=200, height=113)

        ## Intializing Obj
        self.ticket_obj = Ticket()
        # self.account_obj = Account()
        # self.assign_var_account_section()

        # Menu Buttons
        dashboard_button = Button(menu_button_frame, text="Dashboard", font=("Arial", 15, "bold"),bg="gray17", fg="gold", cursor="hand2", highlightthickness=5, activebackground="gray12", activeforeground="red", command=self.dashboard_combined_func)
        dashboard_button.place(x=0, y=1, width=190, height=50)

        account_button = Button(menu_button_frame, text="Account", font=("Arial", 15, "bold"),bg="gray17", fg="gold", cursor="hand2", highlightthickness=5, activebackground="gray12", activeforeground="red")
        account_button.place(x=0, y=52, width=190, height=50)

        self.dashboard()
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_destroy_window)
        



    ################################## Dashboard Section ###################################

    def dashboard(self):
        ## Bus Details
        # Title Label
        ### ------------------------------Main Frame--------------------------------------
        self.dashboard_frame = Frame(self.main_frame, bg="lightblue")      
        self.dashboard_frame.place(x=0, y=0, width=1253, height=551)                        

        bus_details_label = Label(self.dashboard_frame, text="Bus Details", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        bus_details_label.place(x=0, y=0, width=1253, height=50)
        
        # Logo
        top_left_logo = Image.open("System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(self.dashboard_frame, image=self.top_left_logo)
        label_top_left_logo.place(x=10, y=5, width=40, height=40)


        # Data Frame, Labels and Entries
        self.bus_details_frame = LabelFrame(self.dashboard_frame, text= "Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
        self.bus_details_frame.place(x=5, y=55, width=375, height=490)

        from_label = Label(self.bus_details_frame, text="From", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        from_label.place(x=10, y=20)
        self.combo_box_from_var = StringVar()
        self.combo_box_from = ttk.Combobox(self.bus_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.combo_box_from_var)
        self.combo_box_from["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet", "Dhangadi", "Biratnagar", "Dailekh"]
        self.combo_box_from.current(0)
        self.combo_box_from.place(x=10, y=50, height=35)

        to_label = Label(self.bus_details_frame, text="To", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        to_label.place(x=190, y=20)
        self.combo_box_to_var = StringVar()
        self.combo_box_to = ttk.Combobox(self.bus_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2", textvariable=self.combo_box_to_var)
        self.combo_box_to["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet", "Dhangadi", "Biratnagar", "Dailekh"]
        self.combo_box_to.current(0)
        self.combo_box_to.place(x=190, y=50, height=35)
        
        date_label = Label(self.bus_details_frame, text="Departure Date", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        date_label.place(x=10, y=100)
        self.date_entry_var = StringVar()
        self.date_entry = DateEntry(self.bus_details_frame, selectmode="day", cursor="hand2", font=("Arial", 12, "bold"), state="readonly", date_pattern="yyyy-mm-dd", textvariable=self.date_entry_var)
        self.date_entry.place(x=10, y=130, width=160, height=35)

        self.search_bus_button = Button(self.bus_details_frame, text="Search Bus", font=("Arial", 15, "bold"), bg="green", fg="white", cursor="hand2", bd=5, highlightthickness=5, activebackground="darkgreen", activeforeground="gold", command=self.search_bus_func)
        self.search_bus_button.place(x=100, y=190, width=150, height=50)


        ## --------- View details frame--------
        # Initializing widgets here
        self.view_details_frame = None
        self.searchby_label = None
        self.searchby_commbo_box = None
        self.show_button = None
        # For Scrollable Frame
        self.scrollable_ticket_info_frame = None   

        # Call Functions
        self.create_scrollable_frame()

        self.select_and_set_track_data()
        self.fetch_data_dashboard()



    def create_view_details_frame_and_widgets(self):
        if self.view_details_frame is None:
            ## --------- View details frame--------
            self.view_details_frame = LabelFrame(self.dashboard_frame, text="View Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
            self.view_details_frame.place(x=385, y=55, width=863, height=490)
            
            # Search by
            self.searchby_label = Label(self.view_details_frame, text="Search By:", font=("Arial", 15, "bold"), bg="lightblue", fg="blue")
            self.searchby_label.place(x=10, y=2, width=120, height=40)
            
            self.searchby_entry_var = StringVar()
            self.searchby_entry = ttk.Entry(self.view_details_frame, font=("Arial", 15, "bold"), textvariable=self.searchby_entry_var)
            def combox_func(event=""):
                clicked_value = self.searchby_commbo_box.get()
                if clicked_value not in ("Select", "Available Seats"):
                    self.searchby_entry_var.set("")
                    self.searchby_entry.place(x=350, y=5, width=200, height=35)
                else:
                    self.searchby_entry.place_forget()
                    
            
            opts = ["Select", "Bus no.", "Bus Type", "Available Seats"]
            self.searchby_commbo_box_var = StringVar()
            self.searchby_commbo_box = ttk.Combobox(self.view_details_frame, font=("Arial", 15, "bold"), width= 15, state="readonly", cursor="hand2", values=opts, textvariable=self.searchby_commbo_box_var) 
            self.searchby_commbo_box.current(0)
            self.searchby_commbo_box.place(x=140, y=5, height=35)
            self.searchby_commbo_box.bind("<<ComboboxSelected>>", combox_func)

            self.show_button = Button(self.view_details_frame, text="Show", font=("Arial", 15, "bold"), bg="black", fg="white", cursor="hand2", bd=3, highlightthickness=5, activebackground="gray17", activeforeground="yellow", command=self.show_button_func)
            self.show_button.place(x=580, y=5, width=100, height=35)



    def create_scrollable_frame(self):
        if self.view_details_frame is None:
            # Create view_details_frame_and_widgets
            self.create_view_details_frame_and_widgets()

        if self.scrollable_ticket_info_frame is None:
            # Ticket Show Scrollable Frame Creation
            self.scrollable_ticket_info_frame = ctk.CTkScrollableFrame(self.view_details_frame, width=828, height=400, border_width = 2, corner_radius=1, fg_color="#1f2022", border_color="gray")
            self.scrollable_ticket_info_frame.place(x=5, y=50)


            

    ### Dashboard Functions
    def search_bus_func(self):
        if self.combo_box_from.get() == "" or self.combo_box_to.get() == "" or self.date_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.main_window)

        elif self.combo_box_from.get() == "Select" or self.combo_box_to.get() == "Select":
            messagebox.showerror("Error", "Invalid input 'Select'", parent=self.main_window)

        else:
            # Create create_scrollable_frame if
            self.create_scrollable_frame()

            try:
                # Fetching Data According to the input
                connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")       
                my_cursor = connection.cursor()

                query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                my_cursor.execute(query, values)
                rows = my_cursor.fetchall()
                
                # If Scrollable Frame
                if self.scrollable_ticket_info_frame is not None:
                    # Clear existing widgets inside frames
                    self.clear_widgets_inside_scrollable_frame()
                        
                    # Populate frames with respective widgets with fetched data
                    if len(rows) != 0:
                        for row in rows:
                            # Create widgets of scrollable frame
                            self.frame_creation_func(row)


            
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")    
            

            finally:
                connection.commit()
                if connection.is_connected():
                        connection.close()



    def fetch_data_dashboard(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            my_cursor = connection.cursor()

            if self.combo_box_from.get() == "Select" and self.combo_box_to.get() == "Select":
                if self.searchby_commbo_box.get() == "Select":      # Searchby Combobox     
                    my_cursor.execute("select * from details_table")
                    rows = my_cursor.fetchall()

                    # If Scrollable Frame
                    if self.scrollable_ticket_info_frame is not None:
                        # Clear existing widgets inside frames
                        self.clear_widgets_inside_scrollable_frame()
                        # Populate frames with respective widgets with fetched data
                        if len(rows) != 0:
                            for row in rows:
                                self.frame_creation_func(row)
                

                elif self.searchby_commbo_box.get() == "Available Seats":
                    my_cursor.execute("select * from details_table")
                    rows = my_cursor.fetchall()

                    # If Scrollable Frame
                    if self.scrollable_ticket_info_frame is not None:
                        # Clear existing widgets inside frames
                        self.clear_widgets_inside_scrollable_frame()
                        # Populate frames with respective widgets with fetched data
                        if len(rows) != 0:
                            for row in rows:
                                if int(row[10]) > 1:
                                    self.frame_creation_func(row)


                else:  # Bus no  
                    if self.searchby_commbo_box.get() == "Bus no.":
                        my_cursor.execute("select * from details_table")
                        rows = my_cursor.fetchall()

                        if self.searchby_entry.get() == "":
                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets inside frames
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_no = %s"
                            values = (self.searchby_entry.get(),)
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                    else:    # Bus Type
                        if self.searchby_entry.get() == "":
                            my_cursor.execute("select * from details_table")
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets inside frames
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_type = %s"
                            values = (self.searchby_entry.get(),)
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


            else:       # If commbox boxes show be there for from and to place
                if self.searchby_commbo_box.get() == "Select":
                    query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                    values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                    my_cursor.execute(query, values)
                    rows = my_cursor.fetchall()

                    # If Scrollable Frame
                    if self.scrollable_ticket_info_frame is not None:
                        # Clear existing widgets inside frames
                        self.clear_widgets_inside_scrollable_frame()
                        # Populate frames with respective widgets with fetched data
                        if len(rows) != 0:
                            for row in rows:
                                self.frame_creation_func(row)


                elif self.searchby_commbo_box.get() == "Available Seats":
                    query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                    values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                    my_cursor.execute(query, values)
                    rows = my_cursor.fetchall()

                    # If Scrollable Frame
                    if self.scrollable_ticket_info_frame is not None:
                        # Clear existing widgets inside frames
                        self.clear_widgets_inside_scrollable_frame()
                        # Populate frames with respective widgets with fetched data
                        if len(rows) != 0:
                            for row in rows:
                                if int(row[10]) > 1:
                                    self.frame_creation_func(row)


                else:   # Bus no 
                    if self.searchby_commbo_box.get() == "Bus no.":
                        if self.searchby_entry.get() == "":
                            query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                            values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets inside frames
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_no = %s and (from_place = %s and to_place = %s)"
                            values = (self.searchby_entry.get(), self.combo_box_from.get(), self.combo_box_to.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)

                    
                    else:   # Bus Type
                        if self.searchby_entry.get() == "":
                            query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                            values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets inside frames
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_type = %s and (from_place = %s and to_place = %s)"
                            values = (self.searchby_entry.get(), self.combo_box_from.get(), self.combo_box_to.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)



        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")    
        
        finally:
            connection.commit()
            if connection.is_connected():
                    connection.close()



    def show_button_func(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            my_cursor = connection.cursor()

            if self.combo_box_from.get() == "" or self.combo_box_to.get() == "" or self.date_entry.get() == "" or self.searchby_commbo_box == "":
                messagebox.showerror("Error", "All fields are required", parent=self.main_window)

            elif self.searchby_commbo_box.get() == "Select":
                messagebox.showerror("Error", "Invalid input 'Select'", parent=self.main_window)

            elif self.searchby_commbo_box.get() == "Available Seats":

                    if self.combo_box_from.get() == "Select" and self.combo_box_to.get() == "Select":
                        my_cursor.execute("select * from details_table")
                        rows = my_cursor.fetchall()

                        # If Scrollable Frame
                        if self.scrollable_ticket_info_frame is not None:
                            # Clear existing widgets inside frames
                            self.clear_widgets_inside_scrollable_frame()
                            # Populate frames with respective widgets with fetched data
                            if len(rows) != 0:
                                for row in rows:
                                    if int(row[10]) > 1:
                                        self.frame_creation_func(row)

                
                    else:
                        query = "select * from details_table where (from_place = %s and to_place = %s) or (from_place = %s and to_place = %s and departure_date = %s)"
                        values = (self.combo_box_from.get(), self.combo_box_to.get(), self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get())
                        my_cursor.execute(query, values)
                        rows = my_cursor.fetchall()

                        # If Scrollable Frame
                        if self.scrollable_ticket_info_frame is not None:
                            # Clear existing widgets inside frames
                            self.clear_widgets_inside_scrollable_frame()
                            # Populate frames with respective widgets with fetched data
                            if len(rows) != 0:
                                for row in rows:
                                    if int(row[10]) > 1:
                                        self.frame_creation_func(row)


            else:   # Bus no
                if self.searchby_commbo_box.get() == "Bus no.":
                    if self.searchby_entry.get()== "":
                        messagebox.showerror("Error", "Searchby entry required", parent=self.main_window)

                    else:
                        if self.combo_box_from.get() == "Select" and self.combo_box_to.get() == "Select":
                            query = "select * from details_table where bus_no = %s"
                            values = (self.searchby_entry.get(),)
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_no = %s and (from_place = %s and to_place = %s)"
                            values = (self.searchby_entry.get(), self.combo_box_from.get(), self.combo_box_to.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                else:   # Bus Type
                    if self.searchby_entry.get()== "":
                        messagebox.showerror("Error", "Searchby entry required", parent=self.main_window)

                    else:
                        if self.combo_box_from.get() == "Select" and self.combo_box_to.get() == "Select":
                            query = "select * from details_table where bus_type = %s"
                            values = (self.searchby_entry.get(),)
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)


                        else:
                            query = "select * from details_table where bus_type = %s and (from_place = %s and to_place = %s)"
                            values = (self.searchby_entry.get(), self.combo_box_from.get(), self.combo_box_to.get())
                            my_cursor.execute(query, values)
                            rows = my_cursor.fetchall()

                            # If Scrollable Frame
                            if self.scrollable_ticket_info_frame is not None:
                                # Clear existing widgets iside frame
                                self.clear_widgets_inside_scrollable_frame()
                                # Populate frames with respective widgets with fetched data
                                if len(rows) != 0:
                                    for row in rows:
                                        self.frame_creation_func(row)



        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")    
        
        finally:
            connection.commit()
            if connection.is_connected():
                    connection.close()



    def frame_creation_func(self, row):
        # Creating clickable frames for each data with its widgets
        each_info_frame = ctk.CTkFrame(self.scrollable_ticket_info_frame, height=150, fg_color="#323645", bg_color="#1f2022", corner_radius=10, border_width=1, border_color="#2f3134", cursor="hand2")
        each_info_frame.pack(padx=10, pady=7, fill=X)

        logo_pil = Image.open("System_Images/bus_logo1.png")
        logo_pil = logo_pil.resize((30, 30), Image.LANCZOS)
        logo_ctk = ctk.CTkImage(logo_pil, size=(30, 30))
        logo_label = ctk.CTkLabel(each_info_frame, image=logo_ctk, text="")
        logo_label.place(x=5, y=5)

        bg_color = "#323645"
        fg_color = "white"

        bus_no_label = Label(each_info_frame, text=f"Bus No:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold")) 
        bus_no_label.place(x=430, y=5)
        bus_no_entry_label = Label(each_info_frame, text=f"{row[0]}", bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        bus_no_entry_label.place(x=510, y=5)

        price_entry_label = Label(each_info_frame, text=f"Rs. {row[8]}", bg=bg_color, fg="gold", font=("Arial", 19, "bold"))
        price_entry_label.place(x=675, y=5)

        bus_agency_label = Label(each_info_frame, text=row[5], bg=bg_color, fg=fg_color, font=("Arial", 17, "bold"))
        bus_agency_label.place(x=35, y=5)

        bus_type_label = Label(each_info_frame, text=row[7], bg=bg_color, fg=fg_color, font=("Arial", 11, "bold"))
        bus_type_label.place(x=35, y=35)

        from_label = Label(each_info_frame, text="From:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold"))
        from_label.place(x=10, y=60)
        frome_entry_label = Label(each_info_frame, text=row[1], bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        frome_entry_label.place(x=65, y=60)

        to_label = Label(each_info_frame, text="To:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold"))
        to_label.place(x=250, y=60)
        to_entry_label = Label(each_info_frame, text=row[2], bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        to_entry_label.place(x=285, y=60)

        departure_date_label = Label(each_info_frame, text=f"Dept. Date:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold")) 
        departure_date_label.place(x=10, y=87)
        departure_date_entry_label = Label(each_info_frame, text=f"{row[3]}", bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        departure_date_entry_label.place(x=110, y=87)

        departure_time_label = Label(each_info_frame, text=f"Dept. Time:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold")) 
        departure_time_label.place(x=250, y=87)
        departure_time_entry_label = Label(each_info_frame, text=f"{row[4]}", bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        departure_time_entry_label.place(x=350, y=87)

        reporting_time_label = Label(each_info_frame, text=f"Rept. Time:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold")) 
        reporting_time_label.place(x=250, y=113)
        reporting_time_entry_label = Label(each_info_frame, text=f"{row[9]}", bg=bg_color, fg="gold", font=("Arial", 13, "bold"))
        reporting_time_entry_label.place(x=350, y=113)

        available_seats_label = Label(each_info_frame, text=f"Available Seats:", bg=bg_color, fg=fg_color, font=("Arial", 13, "bold"))
        available_seats_label.place(x=10, y=115)
        available_seat_entry_label = Label(each_info_frame, text=f"{row[10]} / {row[13]}", bg=bg_color, fg="gold", font=("Arial", 14, "bold"))
        available_seat_entry_label.place(x=145, y=113)

        # Create a button for each row
        ticket_button = ctk.CTkButton(each_info_frame, text="BUY TICKET", text_color="white", fg_color="#34cc15", cursor="hand2", font=("times new roman", 17, "bold"), width=125, height=50, hover_color="#59e23d", corner_radius=10, command=lambda row=row: self.assign_var_buy_tickets(row))
        ticket_button.place(x=670, y=87)



        # Binding hover events
        on_enter, on_leave = self.create_hover_functions(each_info_frame)
        each_info_frame.bind("<Enter>", on_enter)
        each_info_frame.bind("<Leave>", on_leave)
        for widget in each_info_frame.winfo_children():
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
        
        # Bind the button click event to the function and pass the row
        each_info_frame.bind("<Button-1>", lambda event, row=row: self.assign_var_buy_tickets(row))
        for widget in each_info_frame.winfo_children():
            widget.bind("<Button-1>", lambda event, row=row: self.assign_var_buy_tickets(row))




    def create_hover_functions(self, frame, og_bg_color="#323645", hover_color="#404863", event=""):
        # Function to change background color on hover
        def on_enter(event):
            frame.configure(fg_color=hover_color)           # Change background color of frame on hover
            for widget in frame.winfo_children():
                if isinstance(widget, (ctk.CTkLabel,)):
                    widget.configure(bg_color=hover_color)  # Change background color of ctk labels inside frame on hover
                elif isinstance(widget, (Label,)):
                    widget.configure(bg=hover_color)        # Change background color of normal labels and buttons inside frame on hover
                elif isinstance(widget, (ctk.CTkButton,)):
                    widget.configure(bg_color=hover_color)  # Change background color of ctk buttons inside frame on hover


        def on_leave(event):
            frame.configure(fg_color=og_bg_color)           # Restore background color of frame when mouse leaves
            for widget in frame.winfo_children():
                if isinstance(widget, (ctk.CTkLabel,)):
                    widget.configure(bg_color=og_bg_color)  # Restore background color of ctk labels inside frame when mouse leaves
                elif isinstance(widget, (Label,)):
                    widget.configure(bg=og_bg_color)        # Restore background color of normal labels inside frame when mouse leaves
                elif isinstance(widget, (ctk.CTkButton,)):
                    widget.configure(bg_color=og_bg_color)  # Restore background color of ctk buttons inside frame when mouse leaves

        return on_enter, on_leave
    

    
    def assign_var_buy_tickets(self, row):
        # Copying data to ticket module 
        if len(row) >= 15:
            self.ticket_obj.buy_ticket_section_bus_no_var.set(row[0])
            self.ticket_obj.buy_ticket_section_from_var.set(row[1])
            self.ticket_obj.buy_ticket_section_to_var.set(row[2])
            self.ticket_obj.buy_ticket_section_departure_date_var.set(row[3])
            self.ticket_obj.buy_ticket_section_departure_time_var.set(row[4])
            self.ticket_obj.buy_ticket_section_bus_agency_var.set(row[5])
            self.ticket_obj.buy_ticket_section_fare_var.set(row[8])
            self.ticket_obj.buy_ticket_section_reporting_time_var.set(row[9])

            # Update bus_info (assuming these are StringVar variables)
            self.ticket_obj.bus_type.set(row[7])

            # Passeger data
            # self.ticket_obj.buy_ticket_section_passenger_name_var.set(f"{self.dashboard_section_fname_var.get()} {self.dashboard_section_lname_var.get()}")
            # self.ticket_obj.buy_ticket_section_passenger_contact_var.set(self.dashboard_section_contact_var.get())

            # self.ticket_obj.buy_ticket_section_username_var.set(self.dashboard_section_username_var.get())
            # self.ticket_obj.buy_ticket_section_email_var.set(self.dashboard_section_email_var.get())
            # self.ticket_obj.buy_ticket_section_password_var.set(self.dashboard_section_password_var.get())

            # Button for opening buy_ticket_selection along with data transfer (after the data have been saved)
            self.buy_ticket_combined_func()


    def clear_widgets_inside_scrollable_frame(self):
        # Clear existing widgets iside frame
        for widget in self.scrollable_ticket_info_frame.winfo_children():
            widget.pack_forget()
            widget.place_forget()
            widget = None


    def insert_track_data(self):
        # Perform deletion from the database
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")   
            cursor = connection.cursor()

            # if self.combo_box_from.get() != "Select" and self.combo_box_to.get() != "Select":
            query = "insert into track_table (from_place, to_place, departure_date, searchby_combox, searchby_entry) values (%s, %s, %s, %s, %s)"
            values = (self.combo_box_from.get(), self.combo_box_to.get(), self.date_entry.get(), self.searchby_commbo_box.get(), self.searchby_entry.get())
            cursor.execute(query, values)
            
            # Commit the transaction
            connection.commit()
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"An error occurred: {str(error)}")

        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()


    def select_and_set_track_data(self):
        # Perform deletion from the database
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")   
            cursor = connection.cursor()

            # Execute the SQL DELETE statement to remove all data from the table
            cursor.execute("SELECT * FROM track_table ORDER BY track_id DESC LIMIT 1")
            row = cursor.fetchone()

            if row is not None:
                if row[1] != "Select" and row[2] != "Select":
                    self.combo_box_from_var.set(row[1])
                    self.combo_box_to_var.set(row[2])
                
                if row[3] != f"{datetime.now().strftime('%Y-%m-%d')}":
                    self.date_entry_var.set(row[3])

                if self.searchby_commbo_box.winfo_exists():
                    if row[4] != "Select":
                        self.searchby_commbo_box_var.set(row[4])
                        self.searchby_entry.place_forget()
                        self.searchby_entry.place(x=350, y=5, width=200, height=35)

                if self.searchby_entry.winfo_exists():
                    if row[5] != "":
                        self.searchby_entry_var.set(row[5])


            # Commit the transaction
            connection.commit()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"An error occurred: {str(error)}")

        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()
    


    def on_destroy_window(self, eveny=""):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")   
            cursor = connection.cursor()

            # Execute the SQL DELETE statement to remove all data from the table
            cursor.execute("DELETE FROM track_table")

            # Commit the transaction
            connection.commit()

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"An error occurred: {str(error)}")


        finally:
            # Close cursor and connection
            cursor.close()
            connection.close()

        self.main_window.destroy()



    #########################################  FUNCTIONS  #######################################
        
    def dashboard_combined_func(self):
        # Check if the buy_ticket_frame and add_ticket_frame are already created
        if hasattr(self.ticket_obj, 'ticket_button_frame') and self.ticket_obj.ticket_button_frame.winfo_exists():
            # print("Inside 2") 
            self.ticket_obj.ticket_button_frame.destroy()
            self.dashboard()

        elif hasattr(self.account_obj, 'account_button_frame') and self.account_obj.account_button_frame.winfo_exists():
            # print("Inside 2") 
            self.account_obj.account_button_frame.destroy()
            self.dashboard()

        elif hasattr(self, 'dashboard_frame') and self.dashboard_frame.winfo_exists():
            # print("Inside 3")
            self.insert_track_data() 
            self.dashboard_frame.destroy()
            self.dashboard()



    def buy_ticket_combined_func(self):
        # Check if the add_ticket_frame or dashboard are already created
        if hasattr(self, 'dashboard_frame') and self.dashboard_frame.winfo_exists():
            # print("Inside 5") 
            self.insert_track_data() 
            self.dashboard_frame.destroy()
            self.ticket_obj.buy_ticket(self.main_frame)

        elif hasattr(self.account_obj, 'account_button_frame') and self.account_obj.account_button_frame.winfo_exists():
            self.account_obj.account_button_frame.destroy()
            self.ticket_obj.buy_ticket(self.main_frame)

        elif hasattr(self.ticket_obj, 'ticket_button_frame') and self.ticket_obj.ticket_button_frame.winfo_exists():
            # print("Inside 6") 
            self.ticket_obj.ticket_button_frame.destroy()
            self.ticket_obj.buy_ticket(self.main_frame)



    def account_combined_func(self):
        # Check if the ticket_button_frame or dashboard are already created
        if hasattr(self.ticket_obj, 'ticket_button_frame') and self.ticket_obj.ticket_button_frame.winfo_exists():
            # If it exists
            self.ticket_obj.ticket_button_frame.destroy()            
            self.account_obj.account(self.main_frame)
            # self.assign_var_account_section()

        elif hasattr(self, 'dashboard_frame') and self.dashboard_frame.winfo_exists():
            self.insert_track_data() 
            self.dashboard_frame.destroy()
            self.account_obj.account(self.main_frame)
            # self.assign_var_account_section()

        elif hasattr(self.account_obj, 'account_button_frame') and self.account_obj.account_button_frame.winfo_exists():
            self.account_obj.account_button_frame.destroy()
            self.account_obj.account(self.main_frame) 
            # self.assign_var_account_section()


    

def main(): 
    window = Tk()
    travel_obj = Travel(window)
    window.mainloop()

if __name__ == "__main__":
    main() 