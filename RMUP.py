import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = customtkinter.CTk()
root.title("Rate my Unicode instructor")
root.geometry("750x500")

connect = sqlite3.connect('rmup.db')

cur = connect.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS userdata(
        username text NOT NULL UNIQUE,
        password text
        )''')

def change_appearance_mode_event():
    if appearance_switch.get() == 1:
        customtkinter.set_appearance_mode("light")
    else:
        customtkinter.set_appearance_mode("dark")

def login():

    username = username_entry.get()

    password = password_entry.get()

    cur.execute("SELECT * FROM userdata WHERE username = ? and password = ?", [username, password])

    fetch = cur.fetchone()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    if fetch:

        main_page = customtkinter.CTkToplevel(root)
        main_page.title("Main page")
        main_page.geometry("750x750")

        rNum = [1, 2, 3, 4, 5]

        cc = ["Python", "Flutter", "Web", "Cybersecurity"]
        pI = ["Eng. Nancy El-Sharkawi", "Fatima AlMomen", "Ahmed Maher"]
        fI = ["Eng. Hiba Alenezi", "Hind Alotaibi", "Ali Alfadhli"]
        wI = ["Eng. Mnawer", "Sarah Almarri", "Ali Alshammari"]
        cI = ["Eng. Ahmad Hadeed", "Abdulmohsen Alghanim", "Majed Ramadhan", "Retaj Alotaibi", "Aya Alsagaf"]

        def increment_count(x):
            global count
            count = x
            ans.set("Rating:      " + str(count))
        
        def submit():

            connect = sqlite3.connect('review.db')

            cur = connect.cursor()

            cur.execute(''' CREATE TABLE IF NOT EXISTS reviewdata(
                userreview text
                )''')

            cur.execute("INSERT INTO reviewdata VALUES (:reviewBox)",
                        {
                            'reviewBox': reviewBox.get("1.0", "end")
                        })
            
            connect.commit()

            root.destroy()
        
        def change_appearance_mode_event1():

            if main_appearance_switch.get() == 1:
                customtkinter.set_appearance_mode("light")
            else:
                customtkinter.set_appearance_mode("dark")
        
        def choice1(Choice):
            global count
            count = 0
            ans.set("Unrated")

            if Choice == cc[0]:

                count = 0
                ans.set("Unrated")
                
                mLabel2.pack(pady=1, padx=10)

                mOptionBox2.pack(pady=12, padx=10)

                mOptionBox3.pack_forget()
                mOptionBox4.pack_forget()
                mOptionBox5.pack_forget()

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cc[1]:

                count = 0
                
                ans.set("Unrated")
                
                mLabel2.pack(pady=1, padx=10)

                mOptionBox3.pack(pady=12, padx=10)

                mOptionBox2.pack_forget()
                mOptionBox4.pack_forget()
                mOptionBox5.pack_forget()

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cc[2]:
                
                count = 0
                
                ans.set("Unrated")

                mLabel2.pack(pady=1, padx=10)

                mOptionBox4.pack(pady=12, padx=10)

                mOptionBox3.pack_forget()
                mOptionBox2.pack_forget()
                mOptionBox5.pack_forget()

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cc[3]:

                count = 0
                
                ans.set("Unrated")
                
                mLabel2.pack(pady=1, padx=10)

                mOptionBox5.pack(pady=12, padx=10)

                mOptionBox3.pack_forget()
                mOptionBox4.pack_forget()
                mOptionBox2.pack_forget()

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()
        
        def choice2(Choice):
            global count
            count = 0
            
            ans.set("Unrated")

            if Choice == pI[0]:

                count = 0
                
                ans.set("Unrated")

                p1label.pack(pady=12, padx=10)

                rating_button.configure(state="normal")

                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == pI[1]:

                count = 0
                
                ans.set("Unrated")

                p2label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == pI[2]:

                count = 0
                
                ans.set("Unrated")

                p3label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p2label.pack_forget()
                p1label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == fI[0]:

                count = 0
                
                ans.set("Unrated")

                f1label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()
            
            elif Choice == fI[1]:

                count = 0
                
                ans.set("Unrated")

                f2label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == fI[2]:

                count = 0
                
                ans.set("Unrated")

                f3label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()
            
            elif Choice == wI[0]:

                count = 0
                
                ans.set("Unrated")
            
                w1label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == wI[1]:

                count = 0
                
                ans.set("Unrated")
                
                w2label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == wI[2]:

                count = 0
                
                ans.set("Unrated")

                w3label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()

                c1label.pack_forget()
                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cI[0]:

                count = 0
                
                ans.set("Unrated")

                c1label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cI[1]:

                count = 0
                
                ans.set("Unrated")

                c2label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c1label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cI[2]:

                count = 0
                
                ans.set("Unrated")

                c3label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c2label.pack_forget()
                c1label.pack_forget()
                c4label.pack_forget()
                c5label.pack_forget()

            elif Choice == cI[3]:

                count = 0
                
                ans.set("Unrated")

                c4label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c2label.pack_forget()
                c3label.pack_forget()
                c1label.pack_forget()
                c5label.pack_forget()

            elif Choice == cI[4]:

                count = 0
                
                ans.set("Unrated")

                c5label.pack(pady=12, padx=10)
                
                rating_button.configure(state="normal")

                p1label.pack_forget()
                p2label.pack_forget()
                p3label.pack_forget()

                f1label.pack_forget()
                f2label.pack_forget()
                f3label.pack_forget()

                w1label.pack_forget()
                w2label.pack_forget()
                w3label.pack_forget()

                c2label.pack_forget()
                c3label.pack_forget()
                c4label.pack_forget()
                c1label.pack_forget()
        global choice3
        def choice3(choice):

            if choice == rNum[0]: 

                increment_count(0)

            elif choice == rNum[1]: 

                increment_count(1)
            
            elif choice == rNum[2]: 

                increment_count(2)
            
            elif choice == rNum[3]: 

                increment_count(3)
            
            elif choice == rNum[4]: 

                increment_count(4)
        
        textFont = customtkinter.CTkFont(family="Gill Sans MT")

        unicode_image = ImageTk.PhotoImage(Image.open("unicode logo.png")) 
            
        mFrame1 = customtkinter.CTkFrame(main_page)
        mFrame1.pack(pady=20, padx=60, fill="both", expand=True)

        main_title_label = customtkinter.CTkLabel(mFrame1, text="Rate my Unicode 3 Instructor", font = (textFont,24))
        main_title_label.pack()

        main_image_label = customtkinter.CTkLabel(mFrame1, image= unicode_image, text="")
        main_image_label.pack(pady=(1,12))

        global ans
        ans = customtkinter.StringVar(mFrame1)
        ans.set("Unrated")

        mLabel1 = customtkinter.CTkLabel(mFrame1, text = "Choose a Unicode 3 course:", font= (textFont,24))
        mLabel1.pack(pady=1, padx=10)

        mLabel2 = customtkinter.CTkLabel(mFrame1, text = "Choose an instructor:", font= (textFont,24))

        mOptionBox1 = customtkinter.CTkOptionMenu(mFrame1, values = cc, command = choice1, font= textFont)
        mOptionBox1.pack(pady=12, padx=10)

        mOptionBox2 = customtkinter.CTkOptionMenu(mFrame1, values = pI, font= textFont, command=choice2)
        mOptionBox3 = customtkinter.CTkOptionMenu(mFrame1, values = fI, font= textFont, command=choice2)
        mOptionBox4 = customtkinter.CTkOptionMenu(mFrame1, values = wI, font= textFont, command=choice2)
        mOptionBox5 = customtkinter.CTkOptionMenu(mFrame1, values = cI, font= textFont, command=choice2)

        # Python instructors get an automatic 5/5 because I'm biased :D

        p1label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        p2label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        p3label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)

        f1label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        f2label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        f3label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)

        w1label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        w2label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        w3label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)

        c1label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        c2label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        c3label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        c4label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)
        c5label = customtkinter.CTkLabel(mFrame1, textvariable=ans, font= textFont)

        main_appearance_switch = customtkinter.CTkSwitch(mFrame1, text= "Dark / Light mode", command = change_appearance_mode_event1, font= textFont)
        main_appearance_switch.pack(side ="bottom", pady=12, padx=10)

        submitButton = customtkinter.CTkButton(mFrame1, text="Submit", font = textFont, command = submit)
        submitButton.pack(side ="bottom", pady=(12,0), padx=10)

        reviewBox = customtkinter.CTkTextbox(mFrame1, width=250, font= textFont)
        reviewBox.pack(side ="bottom", pady=1, padx=10)

        rating_button_frame = customtkinter.CTkFrame(mFrame1)
        rating_button_frame.pack(side="bottom", pady=(0,12), padx=10)

        rating_button = customtkinter.CTkSegmentedButton(rating_button_frame, values = rNum, state="disabled", command = increment_count)
        rating_button.pack()

        connect.commit()
            
    else:
        messagebox.showerror(title="Invalid Credentials", message="Invalid username and/or password")

def register():
    global register_popup
    register_popup = customtkinter.CTkToplevel(root)
    register_popup.title("Register")
    register_popup.geometry("750x500")

    connect = sqlite3.connect('rmup.db')

    cur = connect.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS userdata(
        username text NOT NULL UNIQUE,
        password text
        )''')

    def change_appearance_mode_event():
        if popup_appearance_switch.get() == 1:
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")

    def createAccount():

        connect = sqlite3.connect('rmup.db')

        cur = connect.cursor()

        cur.execute("SELECT * FROM userdata WHERE username = ?", [username_entry.get()])

        fetch = cur.fetchone()

        print(cur)
        
        if fetch:
            messagebox.showerror(title="Username Already Exists", message="Please enter a different username")
            return

        cur.execute("INSERT INTO userdata VALUES (:popup_username_entry, :popup_password_entry)",
                    {
                        'popup_username_entry': popup_username_entry.get(),
                        'popup_password_entry': popup_password_entry.get()
                    })

        popup_username_entry.delete(0, END)
        popup_password_entry.delete(0, END)

        connect.commit()

        register_popup.destroy()


    textFont = customtkinter.CTkFont(family="Gill Sans MT")

    unicode_image = ImageTk.PhotoImage(Image.open("unicode logo.png"))

    popup_frame1 = customtkinter.CTkFrame(register_popup)
    popup_frame1.pack(pady=20, padx=60, fill="both", expand=True)

    popup_title_label = customtkinter.CTkLabel(popup_frame1, text='Rate my Unicode instructor', font=(textFont, 24))
    popup_title_label.pack(pady=12, padx=10)

    popup_image_label = customtkinter.CTkLabel(popup_frame1, image= unicode_image, text="")
    popup_image_label.pack(pady=(1,12))

    popup_ca_label = customtkinter.CTkLabel(popup_frame1, text='Create an account', font=(textFont, 24))
    popup_ca_label.pack(pady=12, padx=10)

    popup_username_entry = customtkinter.CTkEntry(popup_frame1, placeholder_text="Username", font=textFont)
    popup_username_entry.bind('<Return>', createAccount)
    popup_username_entry.pack(pady=12, padx=10)

    popup_password_entry = customtkinter.CTkEntry(popup_frame1, placeholder_text="Password", show="*", font=textFont)
    popup_password_entry.bind('<Return>', createAccount)
    popup_password_entry.pack(pady=12, padx=10)

    popup_cAccount_button = customtkinter.CTkButton(popup_frame1, text="Create account", font=textFont, command =createAccount)
    popup_cAccount_button.bind('<Return>', createAccount)
    popup_cAccount_button.pack(pady=12, padx=10)

    popup_appearance_switch = customtkinter.CTkSwitch(popup_frame1, text= "Dark / Light mode", font=textFont, command = change_appearance_mode_event)
    popup_appearance_switch.pack(pady=12, padx=10)

    connect.commit()
    
unicode_image = ImageTk.PhotoImage(Image.open("unicode logo.png"))

textFont = customtkinter.CTkFont(family="Gill Sans MT")

frame = customtkinter.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

title_label = customtkinter.CTkLabel(frame, text='Rate my Unicode instructor', font=(textFont,24))
title_label.pack(pady=12, padx=10)

image_label = customtkinter.CTkLabel(frame, image= unicode_image, text="")
image_label.pack(pady=(1,12))

login_label = customtkinter.CTkLabel(frame, text='Login', font=(textFont, 24))
login_label.pack(pady=12, padx=10)

username_entry = customtkinter.CTkEntry(frame, placeholder_text="Username", font=textFont)
username_entry.pack(pady=12, padx=10)

password_entry = customtkinter.CTkEntry(frame, placeholder_text="Password", show="*", font=textFont)
password_entry.pack(pady=12, padx=10)

login_button = customtkinter.CTkButton(frame, text="Login", command=login)
login_button.pack(pady=12, padx=10)

register_button = customtkinter.CTkButton(frame, text="Register", command=register)
register_button.pack(pady=12, padx=10)

appearance_switch = customtkinter.CTkSwitch(frame, text= "Dark / Light mode", command = change_appearance_mode_event)
appearance_switch.pack(pady=12, padx=10)

connect.commit()

root.mainloop()