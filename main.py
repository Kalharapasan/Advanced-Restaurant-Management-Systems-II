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