import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import 

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'restaurant_db',
    'user': 'root',
    'password': 'kalharamax' 
}


def main():
    """Main function to run the application"""
    root = Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
    # Check if required modules are installed
    try:
        import mysql.connector
        main()
    except ImportError:
        print("MySQL Connector not found. Please install it using:")
        print("pip install mysql-connector-python")
        
        # Create a simple error window
        root = Tk()
        root.title("Missing Dependency")
        root.geometry("400x200")
        
        error_label = Label(root, 
                          text="MySQL Connector not installed!\n\n"
                               "Please install it using:\n"
                               "pip install mysql-connector-python\n\n"
                               "Then restart the application.",
                          font=('Arial', 12),
                          fg='red',
                          justify=CENTER)
        error_label.pack(expand=True)
        
        root.mainloop()
