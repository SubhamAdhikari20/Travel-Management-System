from tkinter import *
from tkinter import ttk
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
        self.main_window.iconbitmap("Travel-Management-System/System_Images/title_logo.ico")
        self.main_window.minsize(1465, 740)
        
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

        #intializaing object
        self.ticket_obj = Ticket()

        # Top image
        top_img = Image.open("Travel-Management-System/System_Images/top_img2.jpg")
        top_img = top_img.resize((1465, 740), Image.LANCZOS) 
        self.top_img = ImageTk.PhotoImage(top_img)
        label_top_img = Label(self.main_window, image=self.top_img)
        label_top_img.place(x=0, y=0, width=1465, height=140)
        
        # Top left image/logo
        top_left_img = Image.open("Travel-Management-System/System_Images/logo.png")
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

        # Menu Buttons
        dashboard_button = Button(menu_button_frame, text="Dashboard", font=("Arial", 15, "bold"),bg="gray17", fg="gold", cursor="hand2", highlightthickness=5, activebackground="gray12", activeforeground="red")
        dashboard_button.place(x=0, y=1, width=190, height=50)

        logout_button = Button(menu_button_frame, text="Logout", font=("Arial", 15, "bold"),bg="gray17", fg="gold", cursor="hand2", highlightthickness=5, activebackground="gray12", activeforeground="red")
        logout_button.place(x=0, y=52, width=190, height=50)

        self.dashboard()




    ################################## Dashboard Section ####################################

    def dashboard(self):
        ## Bus Details
        # Title Label
        ### ------------------------------Main Frame---------------------------------------
        self.dashboard_frame = Frame(self.main_frame, bg="lightblue")      
        self.dashboard_frame.place(x=0, y=0, width=1253, height=551)                        

        bus_details_label = Label(self.dashboard_frame, text="Bus Details", font=("Arial", 20, "bold"), bg="black", fg="gold", bd=5, relief=RIDGE)
        bus_details_label.place(x=0, y=0, width=1253, height=50)
        
        # Logo
        top_left_logo = Image.open("Travel-Management-System/System_Images/logo1.png")
        top_left_logo = top_left_logo.resize((50, 40), Image.LANCZOS) 
        self.top_left_logo = ImageTk.PhotoImage(top_left_logo)
        label_top_left_logo = Label(self.dashboard_frame, image=self.top_left_logo)
        label_top_left_logo.place(x=10, y=5, width=40, height=40)


        # Data Frame, Labels and Entries
        bus_details_frame = LabelFrame(self.dashboard_frame, text= "Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
        bus_details_frame.place(x=5, y=55, width=375, height=490)

        from_label = Label(bus_details_frame, text="From", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        from_label.place(x=10, y=20)
        self.combo_box_from = ttk.Combobox(bus_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2")
        self.combo_box_from["values"] = ["Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet"]
        self.combo_box_from.current(0)
        self.combo_box_from.place(x=10, y=50, height=35)

        to_label = Label(bus_details_frame, text="To", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        to_label.place(x=190, y=20)
        self.combo_box_to = ttk.Combobox(bus_details_frame, font=("Arial", 12, "bold"), width=15, state="readonly", cursor="hand2")
        self.combo_box_to["values"] = ("Select", "Kathmandu", "Pokhara", "Nepalgunj", "Surkhet")
        self.combo_box_to.current(0)
        self.combo_box_to.place(x=190, y=50, height=35)
        
        date_label = Label(bus_details_frame, text="Departure Date", font=("Arial", 15, "bold"), fg="blue",bg="lightblue")
        date_label.place(x=10, y=100)
        self.date_entry = DateEntry(bus_details_frame, selectmode="day", cursor="hand2", font=("Arial", 12, "bold"), state="readonly", date_pattern="yyyy-mm-dd")
        self.date_entry.place(x=10, y=130, width=160, height=35)

        search_bus_button = Button(bus_details_frame, text="Search Bus", font=("Arial", 15, "bold"), bg="green", fg="white", cursor="hand2", bd=5, highlightthickness=5, activebackground="darkgreen", activeforeground="black")
        search_bus_button.place(x=100, y=190, width=150, height=50)

        ## --------- View details frame---------
        view_details_frame = LabelFrame(self.dashboard_frame, text="View Details", font=("Arial", 17, "bold"), bg="lightblue", fg="blue")
        view_details_frame.place(x=385, y=55, width=863, height=490)

        # Search by
        searchby_label = Label(view_details_frame, text="Search By:", font=("Arial", 15, "bold"), bg="lightblue", fg="blue")
        searchby_label.place(x=10, y=10, width=120, height=40)

        opts = ["Select", "Bus no.", "Bus Type"]
        searchby_commbo_box = ttk.Combobox(view_details_frame, font=("Arial", 15, "bold"), width= 15, state="readonly", cursor="hand2", values=opts) 
        searchby_commbo_box.current(0)
        searchby_commbo_box.place(x=140, y=10, height=35)

        searchby_entry = ttk.Entry(view_details_frame, font=("Arial", 15, "bold"))
        searchby_entry.place(x=350, y=10, width=200, height=35)

        show_button = Button(view_details_frame, text="Show", font=("Arial", 15, "bold"), bg="black", fg="white", cursor="hand2", bd=3, highlightthickness=5, activebackground="gray17", activeforeground="yellow")
        show_button.place(x=580, y=10, width=100, height=35)


        ## ------------Show Table Frame---------------
        details_table_frame = Frame(view_details_frame, bg="white", bd = 2, relief=RIDGE)
        details_table_frame.place(x=5, y=60, width=848, height=320)
        # details_table_frame.place(x=5, y=60, width=848, height=395)

        # Scroll bar
        scroll_bar_x = ttk.Scrollbar(details_table_frame, orient=HORIZONTAL, cursor="hand2")
        scroll_bar_y = ttk.Scrollbar(details_table_frame, orient=VERTICAL, cursor="hand2")

        self.details_table_dashboard = ttk.Treeview(details_table_frame, column= ("bus_no", "from", "to", "departure_date", "departure_time", "bus_agency", "station", "type", "fare", "reporting_time", "no_seat_available", "seats_sold", "seats_booked", "total_seats", "date"), xscrollcommand=scroll_bar_x.set, yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.details_table_dashboard.xview)
        scroll_bar_y.config(command=self.details_table_dashboard.yview)



####

        self.details_table_dashboard.heading("bus_no", text="Bus No")
        self.details_table_dashboard.heading("bus_agency", text="Bus Agency")
        self.details_table_dashboard.heading("station", text="Station")
        self.details_table_dashboard.heading("no_seat_available", text="Available Seats")
        self.details_table_dashboard.heading("departure_date", text="Departure Date")
        self.details_table_dashboard.heading("departure_time", text="Departure Time")
        self.details_table_dashboard.heading("from", text="From")
        self.details_table_dashboard.heading("to", text="To")
        self.details_table_dashboard.heading("fare", text="Fare (Rs)")
        self.details_table_dashboard.heading("type", text="Type")
        self.details_table_dashboard.heading("reporting_time", text="Reporting Time")
        self.details_table_dashboard.heading("seats_sold", text="Seats Sold")
        self.details_table_dashboard.heading("seats_booked", text="Seats Booked")
        self.details_table_dashboard.heading("total_seats", text="Total Seats")
        self.details_table_dashboard.heading("date", text="Date")

        self.details_table_dashboard["show"] = "headings"

        self.details_table_dashboard.column("bus_no", width=125)
        self.details_table_dashboard.column("bus_agency", width=125)
        self.details_table_dashboard.column("station", width=125)
        self.details_table_dashboard.column("no_seat_available", width=125)
        self.details_table_dashboard.column("departure_date", width=125)
        self.details_table_dashboard.column("departure_time", width=125)
        self.details_table_dashboard.column("from", width=125)
        self.details_table_dashboard.column("to", width=125)
        self.details_table_dashboard.column("fare", width=125)
        self.details_table_dashboard.column("type", width=125)
        self.details_table_dashboard.column("reporting_time", width=125)
        self.details_table_dashboard.column("seats_sold", width=125)
        self.details_table_dashboard.column("seats_booked", width=125)
        self.details_table_dashboard.column("total_seats", width=125)
        self.details_table_dashboard.column("date", width=125)

        self.details_table_dashboard.pack(fill=BOTH, expand=True)

        ticket_button = Button(view_details_frame, text="Buy Ticket", font=("Arial", 15, "bold"),bg="red", fg="white", cursor="hand2", bd=5, highlightthickness=5, activebackground="gray12", activeforeground="gold", command=lambda:self.ticket_obj.buy_ticket(self.main_frame))
        ticket_button.place(x=10, y=395, width=150, height=50)
#
        self.style_func()



    def style_func(self):
        # Add Style
        self.style = ttk.Style()

        # self.style.theme_use("default")

        # Configure the treeview colors 
        self.style.configure("Treeview.Heading", font=('Arial', 10, 'bold'), foreground="black")
        self.style.configure("Treeview", font=('Arial', 9), rowheight=25)

        # Change the selected color
        self.style.map("Treeview", background=[("selected", "#347083")])

        # Create Striped rows
        self.details_table_dashboard.tag_configure("oddrow", background="white")
        self.details_table_dashboard.tag_configure("evenrow", background="#c5e3ec")
        
        # Apply tags to alternate rows
        for i, row in enumerate(self.details_table_dashboard.get_children()):
            if i % 2 == 0:
                self.details_table_dashboard.item(row, tags=("evenrow",))
            else:
                self.details_table_dashboard.item(row, tags=("oddrow",))
   

    
def main(): 
    window = Tk()
    travel_obj = Travel(window)
    window.mainloop()

if __name__ == "__main__":
    main() 