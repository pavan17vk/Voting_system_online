import subprocess as sb_p
import tkinter as tk
import registerVoter as regV
import admFunc as adFunc
from tkinter import *
from registerVoter import *
from admFunc import *
from search import *
import hashlib



def AdminHome(root, frame1, frame3):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()

    Button(frame3, text="Admin", command=lambda: AdminHome(root, frame1, frame3)).grid(row=1, column=0)
    frame3.pack(side=TOP)

    Label(frame1, text="Admin", font=('Helvetica', 25, 'bold')).grid(row=0, column=1)
    Label(frame1, text="").grid(row=1, column=0)

    # Admin Login
    runServer = Button(frame1, text="Run Server", width=15, command=lambda: sb_p.call('start python Server.py', shell=True))

    # Voter Login
    registerVoter = Button(frame1, text="Register Voter", width=15, command=lambda: regV.Register(root, frame1))

    # Show Votes
    showVotes = Button(frame1, text="Show Votes", width=15, command=lambda: adFunc.showVotes(root, frame1))

    # Reset Data
    reset = Button(frame1, text="Reset All", width=15, command=lambda: adFunc.resetAll(root, frame1))

    # Search Voter
    searchVoter = Button(frame1, text="Search Voter", width=15, command=lambda: create_search_window())

    # Modify Voter
    modify = Button(frame1, text="Modify Voter", width=15, command=lambda: create_modify_window())

    # Admin Register
    registerAdmin = Button(frame1, text="Admin Register", width=15, command=lambda: AdminRegistration(root, frame1))

    Label(frame1, text="").grid(row=2, column=0)
    Label(frame1, text="").grid(row=4, column=0)
    Label(frame1, text="").grid(row=6, column=0)
    Label(frame1, text="").grid(row=8, column=0)
    Label(frame1, text="").grid(row=10, column=0)
    Label(frame1, text="").grid(row=12, column=0)
    Label(frame1, text="").grid(row=14, column=0)
    runServer.grid(row=3, column=1, columnspan=2)
    registerVoter.grid(row=5, column=1, columnspan=2)
    showVotes.grid(row=7, column=1, columnspan=2)
    reset.grid(row=9, column=1, columnspan=2)
    searchVoter.grid(row=11, column=1, columnspan=2)
    modify.grid(row=13, column=1, columnspan=2)
    registerAdmin.grid(row=15, column=1, columnspan=2)

    frame1.pack()
    root.mainloop()


def log_admin(root, frame1, admin_ID, password):
    with open('admin_credentials.txt', 'r') as file:
        admin_data = file.readlines()
        for line in admin_data:
            existing_admin_id, hashed_password = line.strip().split(':')
            if existing_admin_id == admin_ID and hashlib.sha256(password.encode()).hexdigest() == hashed_password:
                frame3 = root.winfo_children()[1]
                AdminHome(root, frame1, frame3)
                return

    msg = Message(frame1, text="Either ID or Password is Incorrect", width=500)
    msg.grid(row=6, column=0, columnspan=5)



def AdmLogin(root, frame1):
    root.title("Admin Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Admin Login", font=('Helvetica', 18, 'bold')).grid(row=0, column=2, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)
    Label(frame1, text="Admin ID:      ", anchor="e", justify=LEFT).grid(row=2, column=0)
    Label(frame1, text="Password:       ", anchor="e", justify=LEFT).grid(row=3, column=0)

    admin_ID = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable=admin_ID)
    e1.grid(row=2, column=2)
    e2 = Entry(frame1, textvariable=password, show='*')
    e2.grid(row=3, column=2)

    sub = Button(frame1, text="Login", width=10, command=lambda: log_admin(root, frame1, admin_ID.get(), password.get()))
    Label(frame1, text="").grid(row=4, column=0)
    sub.grid(row=5, column=3, columnspan=2)

    frame1.pack()
    root.mainloop()


def register_admin(root, frame1, admin_id, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('admin_credentials.txt', 'r+') as file:
        admin_data = file.readlines()
        for line in admin_data:
            existing_admin_id, _ = line.strip().split(':')
            if existing_admin_id == admin_id:
                msg = tk.Message(frame1, text="Admin ID already exists!", width=500)
                msg.grid(row=6, column=0, columnspan=5)
                return

        file.write(f"{admin_id}:{hashed_password}\n")

    msg = tk.Message(frame1, text="Admin registered successfully!", width=500)
    msg.grid(row=6, column=0, columnspan=5)


def AdminRegistration(root, frame1):
    root.title("Admin Registration")
    for widget in frame1.winfo_children():
        widget.destroy()

    tk.Label(frame1, text="Admin Registration", font=('Helvetica', 18, 'bold')).grid(row=0, column=0, columnspan=2)
    tk.Label(frame1, text="Admin ID:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame1, text="Password:").grid(row=2, column=0, padx=5, pady=5)

    admin_id_entry = tk.Entry(frame1)
    admin_id_entry.grid(row=1, column=1, padx=5, pady=5)
    password_entry = tk.Entry(frame1, show="*")
    password_entry.grid(row=2, column=1, padx=5, pady=5)

    register_button = tk.Button(frame1, text="Register", command=lambda: register_admin(root, frame1, admin_id_entry.get(), password_entry.get()))
    register_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    frame1.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    frame1 = tk.Frame(root)
    frame3 = tk.Frame(root)
    AdmLogin(root, frame1)
