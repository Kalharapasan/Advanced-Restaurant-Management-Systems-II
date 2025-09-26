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
    
    def insert_default_menu_items(self):
        """Insert default menu items"""
        cursor = self.connection.cursor()
        
        menu_items = [
            # Drinks
            ('Latta', 'drinks', 1.20),
            ('Espresso', 'drinks', 1.99),
            ('Iced Latte', 'drinks', 2.05),
            ('Vale Coffee', 'drinks', 1.89),
            ('Cappuccino', 'drinks', 1.99),
            ('African Coffee', 'drinks', 2.99),
            ('American Coffee', 'drinks', 2.39),
            ('Iced Cappuccino', 'drinks', 1.29),
            
            # Cakes
            ('School Cake', 'cakes', 1.35),
            ('Sunny AO Cake', 'cakes', 2.20),
            ('Jonathan YO Cake', 'cakes', 1.99),
            ('West African Cake', 'cakes', 1.49),
            ('Lagos Chocolate Cake', 'cakes', 1.80),
            ('Kilburn Chocolate Cake', 'cakes', 1.67),
            ('Carlton Hill Chocolate Cake', 'cakes', 1.60),
            ('Queen Park Chocolate Cake', 'cakes', 1.99)
        ]
        
        insert_query = "INSERT INTO menu_items (name, category, price) VALUES (%s, %s, %s)"
        cursor.executemany(insert_query, menu_items)
        self.connection.commit()
    
    def setup_ui(self):
        """Setup the user interface with responsive design"""
        # Configure root window
        self.root.title("Restaurant Management System - Enhanced Edition")
        self.root.configure(background='#f0f0f0')
        
        # Make window responsive
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Get screen dimensions for responsive sizing
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set window size based on screen size
        window_width = min(1400, int(screen_width * 0.9))
        window_height = min(800, int(screen_height * 0.9))
        
        # Center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.minsize(1000, 600)

         # Title Frame
        self.setup_title_frame()
        
        # Main content frame
        self.main_frame = Frame(self.root, bg='#f0f0f0')
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        # Setup frames
        self.setup_menu_frame()
        self.setup_receipt_calc_frame()
        
    def setup_title_frame(self):
        """Setup the title frame"""
        title_frame = Frame(self.root, bg='#2c3e50', height=80)
        title_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_propagate(False)
        
        title_label = Label(title_frame, 
                          text="🍽️ Restaurant Management System",
                          font=('Segoe UI', 24, 'bold'),
                          bg='#2c3e50', 
                          fg='white',
                          pady=20)
        title_label.grid(row=0, column=0)
    
    def setup_menu_frame(self):
        """Setup the menu frame with drinks and cakes"""
        menu_main_frame = Frame(self.main_frame, bg='#ecf0f1', relief=RIDGE, bd=2)
        menu_main_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        menu_main_frame.grid_rowconfigure(0, weight=1)
        menu_main_frame.grid_rowconfigure(1, weight=1)
        menu_main_frame.grid_rowconfigure(2, weight=0)
        menu_main_frame.grid_columnconfigure(0, weight=1)
        menu_main_frame.grid_columnconfigure(1, weight=1)

        # Drinks Frame
        drinks_frame = LabelFrame(menu_main_frame, text="☕ Beverages", 
                                font=('Segoe UI', 14, 'bold'),
                                bg='#e8f4fd', fg='#2c3e50', 
                                relief=RIDGE, bd=2)
        drinks_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Cakes Frame
        cakes_frame = LabelFrame(menu_main_frame, text="🧁 Desserts", 
                               font=('Segoe UI', 14, 'bold'),
                               bg='#fef9e7', fg='#2c3e50', 
                               relief=RIDGE, bd=2)
        cakes_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
        # Cost Frame
        self.setup_cost_frame(menu_main_frame)
        
        # Setup drinks items
        self.setup_drinks_items(drinks_frame)
        
        # Setup cakes items
        self.setup_cakes_items(cakes_frame)
    
    
    # Calculator methods
    def btnClick(self, numbers):
        self.operator = self.operator + str(numbers)
        self.text_Input.set(self.operator)

    def btnClear(self):
        self.operator = ""
        self.text_Input.set("")

    def btnEquals(self):
        try:
            sumup = str(eval(self.operator))
            self.text_Input.set(sumup)
            self.operator = ""
        except:
            self.text_Input.set("Error")
            self.operator = ""
    
    
    
    

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
