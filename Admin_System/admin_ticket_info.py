from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector
import customtkinter as ctk
from datetime import datetime
import random,os
from tkinter import scrolledtext, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from mysql.connector import Error
import json

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
        self.main_window.iconbitmap("System_Images/title_logo.ico")
        self.main_window.resizable(0, 0)


        #image
        top_left_img = Image.open("System_Images/logo.png")
        top_left_img = top_left_img.resize((200, 140), Image.LANCZOS) 
        self.top_left_img = ImageTk.PhotoImage(top_left_img)
        label_top_left_img = Label(self.main_window, image=self.top_left_img, relief=RIDGE)
        label_top_left_img.place(x=0, y=0, width=200, height=140)

        
        
        
        ### ------------------------------Title---------------------------------

        title_label = Label(self.main_window, text="Ticket" , font=("Arial", 30, "bold"), bd=5, relief=RIDGE, fg="gold",bg="gray12")
        title_label.place(x=0, y=0, width=800, height=50)

        bill_frame = Frame(self.main_window, bg="lightblue", bd = 5, relief=RIDGE)
        bill_frame.place(x=0, y=50, width=800, height=690)

        # rightframe Bill aria
        detailLabelFrame=LabelFrame(bill_frame,text="Bill Aria",font = ("Arail",15,"bold"), bg="#323645",fg="gold")
        detailLabelFrame.place(x=10 ,y=20,width=775, height=550)

        # Text Area
        self.textarea = scrolledtext.ScrolledText(detailLabelFrame, font=("Arial", 12, "bold"), wrap=WORD, width=40, height=10, bg="white", fg="black")
        self.textarea.pack(fill=BOTH, expand=TRUE)
        
        self.fetch_ticket_info_data()
        self.welcome()

        buy_ticket_button = Button(bill_frame, text="Print", font=("Arial", 15, "bold"), bg="green", fg="gold", cursor="hand2", bd=5, highlightthickness=5, activebackground="darkgreen", activeforeground="black", command=self.save_to_pdf)
        buy_ticket_button.place(x=325, y=600, width=120, height=50)

        self.main_window.grab_set()


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


    def save_to_pdf(self):
        text_content =  self.textarea.get("1.0", END)
        if not text_content.strip():
            messagebox.showerror("Error", "No content to save!", parent=self.main_window)
            return


        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], parent=self.main_window)
        if file_path:
            try:
                c = canvas.Canvas(file_path, pagesize=A4)
                
                # Adjust x-y position based on paper size
                x_offset = 20  # Left margin
                y_offset = A4[1] - 25  # Top margin

                # Split the text content by newline character
                lines = text_content.split('\n')

                # Draw each line separately
                for line in lines:
                    # Split each line by tab character
                    parts = line.split('\t')
                    x_coordinate = x_offset
                    for part in parts:
                        c.drawString(x_coordinate, y_offset, part)
                        x_coordinate += 80  # Adjust spacing between parts
                    y_offset -= 20  # Move to the next line
                
                c.save()
                # messagebox.showinfo("Success", "PDF saved successfully!")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save PDF: {e}", parent=self.main_window)

            finally:
                from admin_buy_tickets import Ticket
                Ticket.destroy_confirm_window()
                self.main_window.destroy()

    def fetch_ticket_info_data(self):
        try:
            connection = mysql.connector.connect(host = "localhost", username = "root", password = "Root@123", database = "travel_ms_db")
            cursor = connection.cursor()
            
            query = "SELECT * from ticket_info_table WHERE bus_no = %s AND passenger_name = %s AND mobile_no = %s ORDER BY ticket_id DESC LIMIT 1"
            values = (self.info_ticket_section_bus_no_var.get(), self.info_ticket_section_passenger_name_var.get(), self.info_ticket_section_passenger_contact_var.get())
            cursor.execute(query, values)
            row = cursor.fetchone() 
            if row is not None:
                # Set the data for ticket generation  
                self.info_ticket_section_ticket_no_var.set(row[0])      
                self.info_ticket_section_passenger_name_var.set(row[1])
                self.info_ticket_section_passenger_contact_var.set(row[2])
                self.info_ticket_section_booked_date_var.set(row[3])
                self.info_ticket_section_bus_no_var.set(row[4])
                self.info_ticket_section_bus_agency_var.set(row[5])
                self.info_ticket_section_bus_type_var.set(row[6])
                self.info_ticket_section_from_var.set(row[7])
                self.info_ticket_section_to_var.set(row[8])
                self.info_ticket_section_departure_date_var.set(row[9])
                self.info_ticket_section_departure_time_var.set(row[10])

                seat_ls = json.loads(row[11])
                seat_no = ", ".join(seat_ls)
                self.info_ticket_section_seats_no_var.set(seat_no)

                self.info_ticket_section_total_passenger_var.set(row[12])
                self.info_ticket_section_fare_var.set(row[13])
                self.info_ticket_section_total_price_var.set(row[14])
                self.info_ticket_section_reporting_time_var.set(row[15])
            connection.commit()      

        except Error as e:
            messagebox.showerror("Error while connecting to MySQL", f"{str(e)}", parent=self.main_window)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


def main(): 
    window = Tk()
    # travel_obj = Travel(window)
    travel_obj = Ticket_Info()
    travel_obj.ticket_info_class(window)
    window.mainloop()

if __name__ == "__main__":
    main() 


