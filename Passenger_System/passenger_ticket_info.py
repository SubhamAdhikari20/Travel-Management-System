from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import customtkinter as ctk
from datetime import datetime
from tkinter import scrolledtext, filedialog

class Ticket_Info:
    def __init__(self):
        # ======================Variables======================
        self.info_ticket_section_ticket_no_var = StringVar()
        self.info_ticket_section_passenger_name_var = StringVar()
        self.info_ticket_section_passenger_contact_var = StringVar()
        self.info_ticket_section_bus_no_var = StringVar()
        self.info_ticket_section_booked_date_var = StringVar()
        self.info_ticket_section_bus_agency_var = StringVar()
        self.info_ticket_section_bus_type_var = StringVar()
        self.info_ticket_section_departure_date_var = StringVar()
        self.info_ticket_section_departure_time_var = StringVar()
        self.info_ticket_section_from_var = StringVar()
        self.info_ticket_section_to_var = StringVar()
        self.info_ticket_section_seats_no_var = StringVar()
        self.info_ticket_section_fare_var = StringVar()
        self.info_ticket_section_total_price_var = StringVar()
        self.info_ticket_section_total_passenger_var = StringVar()
        self.info_ticket_section_reporting_time_var = StringVar()
           


    def ticket_info_class(self, root):
        self.main_window = root
        self.main_window.title("Travel Managemet System")
        self.main_window.geometry("800x740+330+0")
        self.main_window.iconbitmap("Travel-Management-System/System_Images/title_logo.ico")
        self.main_window.resizable(0, 0)


        #image
        top_left_img = Image.open("Travel-Management-System/System_Images/logo.png")
        top_left_img = top_left_img.resize((200, 140), Image.LANCZOS) 
        self.top_left_img = ImageTk.PhotoImage(top_left_img)
        label_top_left_img = Label(self.main_window, image=self.top_left_img, relief=RIDGE)
        label_top_left_img.place(x=0, y=0, width=200, height=140)

        
        
        
        ### ------------------------------Title---------------------------------
        title_label = Label(self.main_window, text="Tickets" , font=("Arial", 30, "bold"), bd=5, relief=RIDGE, fg="gold",bg="gray12")
        title_label.place(x=0, y=0, width=800, height=50)

        bill_frame = Frame(self.main_window, bg="lightblue", bd = 5, relief=RIDGE)
        bill_frame.place(x=0, y=50, width=800, height=690)

        # rightframe Bill aria
        detailLabelFrame=LabelFrame(bill_frame,text="Bill Aria",font = ("Arail",15,"bold"), bg="#323645",fg="gold")
        detailLabelFrame.place(x=10 ,y=20,width=775, height=550)


        # Text Area
        self.textarea = scrolledtext.ScrolledText(detailLabelFrame, font=("Arial", 12, "bold"), wrap=WORD, width=40, height=10, bg="white", fg="black")
        self.textarea.pack(fill=BOTH, expand=TRUE)
        
        self.welcome()

        buy_ticket_button = Button(bill_frame, text="Print", font=("Arial", 15, "bold"), bg="green", fg="gold", cursor="hand2", bd=5, highlightthickness=5, activebackground="darkgreen", activeforeground="black")
        buy_ticket_button.place(x=325, y=600, width=120, height=50)
  


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\n\t\t              Welcome to Yatru Travels\n")
        self.textarea.insert(END,"\n___________________________________________________________________________________\n")
        self.textarea.insert(END,f"\n Ticket No:\t{self.info_ticket_section_ticket_no_var.get()}")
        self.textarea.insert(END,f"\n Booked By:\t{self.info_ticket_section_passenger_name_var.get()}\t\t\tBus No:\t{self.info_ticket_section_bus_no_var.get()}")
        self.textarea.insert(END,f"\n Mobile No:\t{self.info_ticket_section_passenger_contact_var.get()}\t\t\tBus Agency:\t{self.info_ticket_section_bus_agency_var.get()}")
        self.textarea.insert(END,f"\n Date:\t{self.info_ticket_section_booked_date_var.get()}\t\t\tBus Type:\t{self.info_ticket_section_bus_type_var.get()}")
        self.textarea.insert(END,"\n___________________________________________________________________________________\n")
        self.textarea.insert(END,f"\n From:\t{self.info_ticket_section_from_var.get()}\t\t\tTo:\t{self.info_ticket_section_to_var.get()}")
        self.textarea.insert(END,f"\n Dept Date:\t{self.info_ticket_section_departure_date_var.get()}\t\t\tDept Time:\t{self.info_ticket_section_departure_time_var.get()}")
        self.textarea.insert(END,"\n___________________________________________________________________________________\n")
        self.textarea.insert(END,f"\n Seat Number:\t          {self.info_ticket_section_seats_no_var.get()}")
        self.textarea.insert(END,f"\n Total Passenger:\t          {self.info_ticket_section_total_passenger_var.get()}")
        self.textarea.insert(END,f"\n Fare (NPR):\t          {self.info_ticket_section_fare_var.get()}")
        self.textarea.insert(END,f"\n Total Price (NPR):\t          {self.info_ticket_section_total_price_var.get()}")
        self.textarea.insert(END,f"\n Reporting Time:\t          {self.info_ticket_section_reporting_time_var.get()}")
        self.textarea.insert(END,"\n___________________________________________________________________________________")

        # Disable the ability to edit the content
        self.textarea.config(state='disabled')



def main(): 
    window = Tk()
    # travel_obj = Travel(window)
    travel_obj = Ticket_Info()
    travel_obj.ticket_info_class(window)
    window.mainloop()

if __name__ == "__main__":
    main() 


