import tkinter as tk
from tkinter import ttk
import pandas as pd
from pathlib import Path

path = Path("C:\\Users\\wwwsu\\Desktop\\vote\\database")

def search_voter_data(vid_entry):
    df = pd.read_csv(path / 'voterList.csv')
    df = df[['voter_id', 'Name', 'Gender', 'Zone', 'City', 'Passw', 'hasVoted']]
    vid_entry = int(vid_entry)
    voter_data = df[df['voter_id'] == vid_entry].to_dict(orient='records')
    return voter_data

def search_and_display(root, frame1, vid):
    voter_data = search_voter_data(vid)
    if voter_data:
        for widget in frame1.winfo_children():
            widget.destroy()

        labels = ['voter_id', 'Name', 'Gender', 'Zone', 'City', 'Passw', 'hasVoted']
        ttk.Label(frame1, text="Attribute").grid(row=0, column=0, padx=5, pady=5)
        for i, label in enumerate(labels):
            ttk.Label(frame1, text=label).grid(row=i+1, column=0, padx=5, pady=5)

        ttk.Label(frame1, text="Value").grid(row=0, column=1, padx=5, pady=5)
        for i, label in enumerate(labels):
            ttk.Label(frame1, text=voter_data[0][label]).grid(row=i+1, column=1, padx=5, pady=5)
    else:
        for widget in frame1.winfo_children():
            widget.destroy()

        ttk.Label(frame1, text="Voter ID not found").grid(row=0, column=0, padx=5, pady=5)

def create_search_window():
    root = tk.Tk()
    root.title("Search Voter")
    frame1 = ttk.Frame(root)
    frame1.pack(padx=10, pady=10)

    ttk.Label(frame1, text="Enter Voter ID:").grid(row=0, column=0, padx=5, pady=5)
    vid_entry = ttk.Entry(frame1)
    vid_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = ttk.Button(frame1, text="Search",
                               command=lambda: search_and_display(root, frame1, vid_entry.get()))
    search_button.grid(row=0, column=2, padx=5, pady=5)

    root.mainloop()

def modify_voter_data(vid, field, value):
    df = pd.read_csv(path / 'voterList.csv')
    df.loc[df['voter_id'] == vid, field] = value
    df.to_csv(path / 'voterList.csv', index=False)

def modify_and_display(root, frame1, vid_entry, field_entry, value_entry):
    vid = int(vid_entry.get())
    field = field_entry.get()
    value = value_entry.get()

    modify_voter_data(vid, field, value)
    search_and_display(root, frame1, vid_entry.get())

def create_modify_window():
    root = tk.Tk()
    root.title("Modify Voter Data")
    frame1 = ttk.Frame(root)
    frame1.pack(padx=10, pady=10)

    ttk.Label(frame1, text="Enter Voter ID:").grid(row=0, column=0, padx=5, pady=5)
    vid_entry = ttk.Entry(frame1)
    vid_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame1, text="Enter Field to Modify:").grid(row=1, column=0, padx=5, pady=5)
    field_entry = ttk.Entry(frame1)
    field_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(frame1, text="Enter New Value:").grid(row=2, column=0, padx=5, pady=5)
    value_entry = ttk.Entry(frame1)
    value_entry.grid(row=2, column=1, padx=5, pady=5)

    modify_button = ttk.Button(frame1, text="Modify",
                               command=lambda: modify_and_display(root, frame1, vid_entry, field_entry, value_entry))
    modify_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

# Call the create_search_window function to open the search window

