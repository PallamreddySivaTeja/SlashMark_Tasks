#password generator
import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame for the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Label and Entry for password length
length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # Default length

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Entry to display generated password
password_entry = tk.Entry(frame, width=30)
password_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
