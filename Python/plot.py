import tkinter as tk

root = tk.Tk()
root.title("Levelogger Setup")
root.geometry("400x300")

# Create a title label
title_label = tk.Label(root, text="Levelogger Setup")
title_label.config(font=("Arial", 20, "bold"))
title_label.pack()

# Create a warning label
warning_label = tk.Label(root, text="WARNING: This program is protected by copyright law and international treaties.")
warning_label.pack()

# Create a next button
next_button = tk.Button(root, text="Next")
next_button.pack()

# Create a back button
back_button = tk.Button(root, text="Back")
back_button.pack()

root.mainloop()