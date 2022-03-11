import tkinter as tk
from tkinter import ttk


def greeting():
    print(f'High five, {username.get()}!')


root = tk.Tk()

username = tk.StringVar()

input_frame = ttk.Frame(root, padding=(10, 5, 10, 0))
input_frame.pack(fill='both')

username_label = ttk.Label(input_frame, text='Name: ')
username_label.pack(side='left', padx=(5, 10))

username_entry = ttk.Entry(input_frame, width=20, textvariable=username)
username_entry.pack(side='left', padx=(0, 10))
username_entry.focus()

buttons_frame = ttk.Frame(root, padding=(10, 5))
buttons_frame.pack(fill='both', expand=True)


greeting_button = ttk.Button(buttons_frame, text='Hello!',
                             command=greeting)
greeting_button.pack(side='left', fill='x', expand=True)

cancel_button = ttk.Button(buttons_frame, text='Cancel',
                           command=root.destroy)
cancel_button.pack(side='right', fill='x', expand=True)

root.mainloop()
