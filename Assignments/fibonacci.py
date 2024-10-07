# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:52:46 2024

@author: akhta
"""

import tkinter as tk
from tkinter import messagebox

# Function to generate Fibonacci series
def generate_fibonacci(n):
    # Start with the first two numbers in the series
    fibonacci = [0, 1]
    
    # Generate more numbers if n is greater than 2
    for i in range(2, n):
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)
    
    # If the user only wants 1 number, just return [0]
    return fibonacci[:n]

# Function to handle button click
def on_generate_button_click():
    try:
        # Get the number of terms from the entry box
        n = int(entry.get())
        
        # Ensure the user enters a positive number
        if n <= 0:
            raise ValueError("The number must be greater than zero.")
        
        # Generate the Fibonacci series
        series = generate_fibonacci(n)
        
        # Display the result in the label
        result_label.config(text="Fibonacci Series: " + ', '.join(map(str, series)))
    except ValueError:
        # Show an error message if the input is invalid
        messagebox.showerror("Error", "Please enter a valid positive number.")

# Set up the GUI window
root = tk.Tk()
root.title("Fibonacci Series Generator")

# Create a label to ask the user for input
prompt_label = tk.Label(root, text="Enter the number of terms:")
prompt_label.grid(row=0, column=0, padx=10, pady=10)

# Create an entry box for the user to type a number
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button that will generate the Fibonacci series
generate_button = tk.Button(root, text="Generate", command=on_generate_button_click)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create a label that will display the Fibonacci series
result_label = tk.Label(root, text="Fibonacci Series: ")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI loop (this keeps the window open and responsive)
root.mainloop()
