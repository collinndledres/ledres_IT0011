import tkinter as tk
from tkinter import messagebox

#Function to display a message when "Hello" button is clicked
def say_hello():
    messagebox.showinfo("Message", "Hello, welcome!")

#Create the main window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("300x200")  # Set window size

#Create "Hello" button
hello_button = tk.Button(root, text="Hello", command=say_hello, font=("Arial", 12), bg="lightblue")
hello_button.pack(pady=20)

#Create "Exit" button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
exit_button.pack(pady=10)

#Run the Tkinter event loop
root.mainloop()