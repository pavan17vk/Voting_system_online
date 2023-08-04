import tkinter as tk
import hashlib

def register_admin(root, frame1, admin_id, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open('admin_credentials.txt', 'r+') as file:
        admin_data = file.readlines()
        for line in admin_data:
            existing_admin_id, _ = line.strip().split(':')
            if existing_admin_id == admin_id:
                msg = tk.Message(frame1, text="Admin ID already exists!", width=500)
                msg.grid(row=4, column=0, columnspan=2)
                return

        file.write(f"{admin_id}:{hashed_password}\n")

    msg = tk.Message(frame1, text="Admin registered successfully!", width=500)
    msg.grid(row=4, column=0, columnspan=2)

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
    frame1 = tk.Frame(root)
    AdminRegistration(root, frame1)
    root.mainloop()
