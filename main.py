import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import json

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'restDB',
    'user': 'root',
    'password': 'kalharamax' 
}

class RestaurantManagementSystem:
    def __init__(self,root):
        self.root =root
        self.setup_database()
        self.setup_variables()
        self.setup_ui()
    
    def setup_database(self):
        """Initialize database connection and create tables if they don't exist"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                
                # Create database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS restDB")
                cursor.execute("USE restaurant_db")
                
                # Create orders table
                create_orders_table = """
                CREATE TABLE IF NOT EXISTS orders (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    receipt_ref VARCHAR(50) UNIQUE NOT NULL,
                    order_date DATE NOT NULL,
                    order_time TIME NOT NULL,
                    items JSON NOT NULL,
                    cost_of_drinks DECIMAL(10,2),
                    cost_of_cakes DECIMAL(10,2),
                    service_charge DECIMAL(10,2),
                    subtotal DECIMAL(10,2),
                    tax_paid DECIMAL(10,2),
                    total_cost DECIMAL(10,2),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                cursor.execute(create_orders_table)
                
                # Create menu_items table
                create_menu_table = """
                CREATE TABLE IF NOT EXISTS menu_items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    category ENUM('drinks', 'cakes') NOT NULL,
                    price DECIMAL(5,2) NOT NULL,
                    is_active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                cursor.execute(create_menu_table)
                
                # Insert default menu items if table is empty
                cursor.execute("SELECT COUNT(*) FROM menu_items")
                if cursor.fetchone()[0] == 0:
                    self.insert_default_menu_items()
                
                self.connection.commit()
                print("Database connected and tables created successfully")
                
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.connection = None
            
    def setup_variables(self):
        """Initialize all tkinter variables"""
        # Checkbox variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()

        # Cost variables
        self.DateofOrder = StringVar()
        self.Receipt_Ref = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
        self.CostofCakes = StringVar()
        self.CostofDrinks = StringVar()
        self.ServiceCharge = StringVar()

        # Calculator variable
        self.text_Input = StringVar()
        self.operator = ""

        # Item entry variables
        self.E_Latta = StringVar()
        self.E_Espresso = StringVar()
        self.E_Iced_Latta = StringVar()
        self.E_Vale_Coffe = StringVar()
        self.E_Cappuccino = StringVar()
        self.E_African_Coffee = StringVar()
        self.E_American_Coffee = StringVar()
        self.E_Iced_Cappuccino = StringVar()

        self.E_School_Cake = StringVar()
        self.E_Sunny_AO_Cake = StringVar()
        self.E_Jonathan_YO_Cake = StringVar()
        self.E_West_African_Cake = StringVar()
        self.E_Lagos_Chocolate_Cake = StringVar()
        self.E_Kilburn_Chocolate_Cake = StringVar()
        self.E_Carlton_Hill_Chocolate_Cake = StringVar()
        self.E_Queen_Park_Chocolate_Cake = StringVar()

        # Set default values
        for var in [self.E_Latta, self.E_Espresso, self.E_Iced_Latta, self.E_Vale_Coffe,
                   self.E_Cappuccino, self.E_African_Coffee, self.E_American_Coffee, self.E_Iced_Cappuccino,
                   self.E_School_Cake, self.E_Sunny_AO_Cake, self.E_Jonathan_YO_Cake, self.E_West_African_Cake,
                   self.E_Lagos_Chocolate_Cake, self.E_Kilburn_Chocolate_Cake, 
                   self.E_Carlton_Hill_Chocolate_Cake, self.E_Queen_Park_Chocolate_Cake]:
            var.set("0")

        self.DateofOrder.set(time.strftime("%d/%m/%Y"))
    
    
    
    
    

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
