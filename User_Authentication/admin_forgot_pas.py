from tkinter import*
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import ttk


class admin_forgot:
    def __init__(self,forgot_window):
        self.forgot_window   =forgot_window
        self.forgot_window.title('Forgot Password') 
        self.forgot_window.geometry('1440x900+0+0')
        self.forgot_window.resizable(0,0)    

        self.bg_img=Image.open('Travel-Management-System/User_Authentication/images/forget_password.jpg')
        self.bg_resize=self.bg_img.resize((1440,900))
        self.bg_con=ImageTk.PhotoImage(self.bg_resize)
        self.bg_label=Label(self.forgot_window,image=self.bg_con)
        self.bg_label.place(x=0,y=0)

        self.frame=ctk.CTkFrame(self.forgot_window,fg_color='#5B5858',width=400,height=560,bg_color='transparent')
        self.frame.place(x=510,y=150)
        
        # admin Label
        self.ad_label=ctk.CTkLabel(self.forgot_window,text='Admin',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',25))
        self.ad_label.place(x=680,y=160)
        self.label=ctk.CTkLabel(self.forgot_window,text='Forgot password?',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',20))
        self.label.place(x=640,y=200)

        # username/email
        self.username_label=ctk.CTkLabel(self.forgot_window,text='Username/Email',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15)).place(x=600,y=240)
        self.user_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.user_entry.place(x=600,y=270)

        # security Question
        self.sec_ques=ctk.CTkLabel(self.forgot_window,text='Security Question',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.sec_ques.place(x=600,y=320)
        self.security_qn_combo_box = ttk.Combobox(self.forgot_window, font=("Aerial", 15), state="readonly",width=18,background='#5B5858')
        self.security_qn_combo_box["values"] = ("Select", "Favorite movie")
        self.security_qn_combo_box.current(0)
        self.security_qn_combo_box.place(x=600, y=350)


        # security Answer
        self.sec_ans=ctk.CTkLabel(self.forgot_window,text='Security Answer',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.sec_ans.place(x=600,y=400)
        self.ans_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.ans_entry.place(x=600,y=430)

        # reset password
        self.reset_label=ctk.CTkLabel(self.forgot_window,text='Reset Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.reset_label.place(x=600,y=480)
        self.reset_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.reset_entry.place(x=600,y=510)

        def hide():
           self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/closeye.png')
           self.reset_entry.configure(show='*')
           self.open_btn.configure(command=show)
        def show():
            self.open_eye.configure(file='Travel-Management-System/User_Authentication/images/openeye.png')
            self.reset_entry.configure(show='')
            self.open_btn.configure(command=hide)
            
        self.open_eye=PhotoImage(file='Travel-Management-System/User_Authentication/images/openeye.png')
        self.open_btn=Button(self.forgot_window,image=self.open_eye,bg='white',bd=0,height=24,cursor='hand',command=hide)
        self.open_btn.place(x=783,y=511)

    # confirm password
        self.confirm=ctk.CTkLabel(self.forgot_window,text='Comfirm Password',fg_color='#5B5858',bg_color='transparent',text_color='white',font=('Aerial',15))
        self.confirm.place(x=600,y=560)
        self.con_entry=Entry(self.forgot_window,fg='black',bg='white',font=('Aerial',15))
        self.con_entry.place(x=600,y=590)


        def hide1():
           self.open_eye1.configure(file='Travel-Management-System/User_Authentication/images/closeye.png')
           self.con_entry.configure(show='*')
           self.open_btn1.configure(command=show1)
        def show1():
            self.open_eye1.configure(file='Travel-Management-System/User_Authentication/images/openeye.png')
            self.con_entry.configure(show='')
            self.open_btn1.configure(command=hide1)
            
        self.open_eye1=PhotoImage(file='Travel-Management-System/User_Authentication/images/openeye.png')
        self.open_btn1=Button(self.forgot_window,image=self.open_eye1,bg='white',bd=0,height=24,cursor='hand',command=hide1)
        self.open_btn1.place(x=783,y=591)
        


    # reset Button
        self.reset_btn=ctk.CTkButton(self.forgot_window,text='Reset',fg_color='white',text_color='black',font=('aerial',20),width=70)
        self.reset_btn.place(x=670,y=650)



if __name__ == "__main__":    
    root = Tk()
    obj = admin_forgot(root)
    root.mainloop()