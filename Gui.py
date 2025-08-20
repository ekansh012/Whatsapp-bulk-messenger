import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pywhatkit
from threading import Thread


def send_message():
    # Get the phone numbers from the Excel file
    phone_numbers_file = phone_numbers_entry.get()
    phone_numbers_df = pd.read_excel(phone_numbers_file)
    phone_numbers = phone_numbers_df.iloc[:, 0].tolist()  # Assuming the phone numbers are in the first column

    # Get the text message from the file
    message_file = message_entry.get()
    with open(message_file, 'r') as f:
        message = f.read()

    # Send the message to all phone numbers using WhatsApp
    def send_message_to_all(phone_numbers, message):
        for phone_number in phone_numbers:
            pywhatkit.sendwhatmsg_instantly(f"+91{phone_number}", message, 15, True, 5)

    thread = Thread(target=send_message_to_all, args=(phone_numbers, message))
    thread.start()


def browse_phone_numbers_file():
    file_path = filedialog.askopenfilename(title="Select phone numbers file", filetypes=[("Excel files", "*.xlsx *.xls")])
    phone_numbers_entry.delete(0, tk.END)
    phone_numbers_entry.insert(0, file_path)


def browse_message_file():
    file_path = filedialog.askopenfilename(title="Select message file", filetypes=[("Text files", "*.txt")])
    message_entry.delete(0, tk.END)
    message_entry.insert(0, file_path)

# Create the GUI


root = tk.Tk()
root.title("WhatsApp Message Sender")

# Create input fields for phone numbers file and message file
phone_numbers_label = tk.Label(root, text="Select phone numbers file:")
phone_numbers_label.grid(row=0, column=0, padx=5, pady=5)
phone_numbers_entry = tk.Entry(root, width=50)
phone_numbers_entry.grid(row=0, column=1, padx=5, pady=5)
phone_numbers_browse_button = tk.Button(root, text="Browse", command=browse_phone_numbers_file)
phone_numbers_browse_button.grid(row=0, column=2, padx=5, pady=5)

message_label = tk.Label(root, text="Select message file:")
message_label.grid(row=1, column=0, padx=5, pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=1, column=1, padx=5, pady=5)
message_browse_button = tk.Button(root, text="Browse", command=browse_message_file)
message_browse_button.grid(row=1, column=2, padx=5, pady=5)

# Create send message button
send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
