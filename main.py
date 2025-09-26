import random
import time
import datetime
import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import json


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
                
                
                cursor.execute("CREATE DATABASE IF NOT EXISTS restDB")
                cursor.execute("USE restaurant_db")
                
              
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

        
        self.DateofOrder = StringVar()
        self.Receipt_Ref = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
        self.CostofCakes = StringVar()
        self.CostofDrinks = StringVar()
        self.ServiceCharge = StringVar()

        
        self.text_Input = StringVar()
        self.operator = ""

      
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
         
            ('Latta', 'drinks', 1.20),
            ('Espresso', 'drinks', 1.99),
            ('Iced Latte', 'drinks', 2.05),
            ('Vale Coffee', 'drinks', 1.89),
            ('Cappuccino', 'drinks', 1.99),
            ('African Coffee', 'drinks', 2.99),
            ('American Coffee', 'drinks', 2.39),
            ('Iced Cappuccino', 'drinks', 1.29),
            
            
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
       
        self.root.title("Restaurant Management System - Enhanced Edition")
        self.root.configure(background='#f0f0f0')
        
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
       
        window_width = min(1400, int(screen_width * 0.9))
        window_height = min(800, int(screen_height * 0.9))
        
        
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.minsize(1000, 600)

        
        self.setup_title_frame()
        
        
        self.main_frame = Frame(self.root, bg='#f0f0f0')
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
       
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

     
        drinks_frame = LabelFrame(menu_main_frame, text="☕ Beverages", 
                                font=('Segoe UI', 14, 'bold'),
                                bg='#e8f4fd', fg='#2c3e50', 
                                relief=RIDGE, bd=2)
        drinks_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
      
        cakes_frame = LabelFrame(menu_main_frame, text="🧁 Desserts", 
                               font=('Segoe UI', 14, 'bold'),
                               bg='#fef9e7', fg='#2c3e50', 
                               relief=RIDGE, bd=2)
        cakes_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        
       
        self.setup_cost_frame(menu_main_frame)
        
        
        self.setup_drinks_items(drinks_frame)
        
        
        self.setup_cakes_items(cakes_frame)
    
    def setup_drinks_items(self, parent):
        """Setup drinks items with checkboxes and entry fields"""
        drinks_data = [
            ("Latta", self.var1, self.E_Latta, self.chkLatta),
            ("Espresso", self.var2, self.E_Espresso, self.chkEspresso),
            ("Iced Latte", self.var3, self.E_Iced_Latta, self.chkIced_Latte),
            ("Vale Coffee", self.var4, self.E_Vale_Coffe, self.chkVale_Coffee),
            ("Cappuccino", self.var5, self.E_Cappuccino, self.chkCappuccino),
            ("African Coffee", self.var6, self.E_African_Coffee, self.chkAfrican_Coffee),
            ("American Coffee", self.var7, self.E_American_Coffee, self.chkAmerican_Coffee),
            ("Iced Cappuccino", self.var8, self.E_Iced_Cappuccino, self.chkIced_Cappuccino)
        ]
        
        self.drink_entries = {}
        
        for i, (name, var, text_var, command) in enumerate(drinks_data):
            
            chk = Checkbutton(parent, text=name, variable=var,
                            font=('Segoe UI', 11, 'bold'),
                            bg='#e8f4fd', fg='#2c3e50',
                            activebackground='#d4edfa',
                            command=command)
            chk.grid(row=i, column=0, sticky=W, padx=10, pady=2)
            
            
            entry = Entry(parent, textvariable=text_var,
                        font=('Segoe UI', 10),
                        width=8, state=DISABLED,
                        bg='#ffffff', fg='#2c3e50',
                        bd=1, relief=SOLID)
            entry.grid(row=i, column=1, sticky=E, padx=10, pady=2)
            
            self.drink_entries[name] = entry
    
    def setup_cakes_items(self, parent):
        """Setup cakes items with checkboxes and entry fields"""
        cakes_data = [
            ("School Cake", self.var9, self.E_School_Cake, self.chkSchool_Cake),
            ("Sunday O Cake", self.var10, self.E_Sunny_AO_Cake, self.chkSunny_AO_Cake),
            ("Jonathan O Cake", self.var11, self.E_Jonathan_YO_Cake, self.chkJonathan_YO_Cake),
            ("West African Cake", self.var12, self.E_West_African_Cake, self.chkWest_African_Cake),
            ("Lagos Chocolate Cake", self.var13, self.E_Lagos_Chocolate_Cake, self.chkLagos_Chocolate_Cake),
            ("Kilburn Chocolate Cake", self.var14, self.E_Kilburn_Chocolate_Cake, self.chkKilburn_Chocolate_Cake),
            ("Carlton Hill Cake", self.var15, self.E_Carlton_Hill_Chocolate_Cake, self.chkCarlton_Hill_Cake),
            ("Queen's Park Cake", self.var16, self.E_Queen_Park_Chocolate_Cake, self.chkQueen_Park_Cake)
        ]
        
        self.cake_entries = {}
        
        for i, (name, var, text_var, command) in enumerate(cakes_data):
         
            chk = Checkbutton(parent, text=name, variable=var,
                            font=('Segoe UI', 11, 'bold'),
                            bg='#fef9e7', fg='#2c3e50',
                            activebackground='#fcf4dd',
                            command=command)
            chk.grid(row=i, column=0, sticky=W, padx=10, pady=2)
            
          
            entry = Entry(parent, textvariable=text_var,
                        font=('Segoe UI', 10),
                        width=8, state=DISABLED,
                        bg='#ffffff', fg='#2c3e50',
                        bd=1, relief=SOLID)
            entry.grid(row=i, column=1, sticky=E, padx=10, pady=2)
            
            self.cake_entries[name] = entry
    
    def setup_receipt_calc_frame(self):
        """Setup the receipt and calculator frame"""
        right_frame = Frame(self.main_frame, bg='#ecf0f1')
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        right_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        
     
        self.setup_buttons_frame(right_frame)
        
       
        self.setup_receipt_frame(right_frame)
        
       
        self.setup_calculator_frame(right_frame)
    
    def setup_buttons_frame(self, parent):
        """Setup the action buttons"""
        buttons_frame = Frame(parent, bg='#ecf0f1')
        buttons_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        buttons_frame.grid_columnconfigure(0, weight=1)
        buttons_frame.grid_columnconfigure(1, weight=1)
        buttons_frame.grid_columnconfigure(2, weight=1)
        buttons_frame.grid_columnconfigure(3, weight=1)
        
        
        button_style = {
            'font': ('Segoe UI', 12, 'bold'),
            'fg': 'white',
            'bd': 2,
            'relief': RAISED,
            'cursor': 'hand2',
            'height': 2
        }
        
        
        btn_total = Button(buttons_frame, text="Calculate Total",
                         bg='#27ae60', activebackground='#2ecc71',
                         command=self.CostofItem, **button_style)
        btn_total.grid(row=0, column=0, sticky="ew", padx=2)
        
       
        btn_receipt = Button(buttons_frame, text="Generate Receipt",
                           bg='#3498db', activebackground='#5dade2',
                           command=self.Receipt, **button_style)
        btn_receipt.grid(row=0, column=1, sticky="ew", padx=2)
        
        
        btn_reset = Button(buttons_frame, text="Reset",
                         bg='#f39c12', activebackground='#f8c471',
                         command=self.Reset, **button_style)
        btn_reset.grid(row=0, column=2, sticky="ew", padx=2)
        
       
        btn_exit = Button(buttons_frame, text="Exit",
                        bg='#e74c3c', activebackground='#ec7063',
                        command=self.iExit, **button_style)
        btn_exit.grid(row=0, column=3, sticky="ew", padx=2)
    
    def setup_cost_frame(self, parent):
        """Setup the cost display frame"""
        cost_frame = LabelFrame(parent, text="💰 Order Summary", 
                              font=('Segoe UI', 14, 'bold'),
                              bg='#f8f9fa', fg='#2c3e50',
                              relief=RIDGE, bd=2)
        cost_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        
        for i in range(6):
            cost_frame.grid_columnconfigure(i, weight=1)
        
        
        cost_data = [
            ("Cost of Drinks:", self.CostofDrinks, 0, 0),
            ("Paid Tax:", self.PaidTax, 0, 2),
            ("Cost of Cakes:", self.CostofCakes, 1, 0),
            ("Sub Total:", self.SubTotal, 1, 2),
            ("Service Charge:", self.ServiceCharge, 2, 0),
            ("Total Cost:", self.TotalCost, 2, 2)
        ]
        
        for label_text, var, row, col in cost_data:
            label = Label(cost_frame, text=label_text,
                        font=('Segoe UI', 10, 'bold'),
                        bg='#f8f9fa', fg='#2c3e50')
            label.grid(row=row, column=col, sticky=W, padx=5, pady=2)
            
            entry = Entry(cost_frame, textvariable=var,
                        font=('Segoe UI', 10),
                        width=15, state='readonly',
                        bg='#ffffff', fg='#2c3e50',
                        bd=1, relief=SOLID)
            entry.grid(row=row, column=col+1, sticky=EW, padx=5, pady=2)
    
    def setup_receipt_frame(self, parent):
        """Setup the receipt display area"""
        receipt_frame = LabelFrame(parent, text="📄 Receipt", 
                                 font=('Segoe UI', 12, 'bold'),
                                 bg='#f8f9fa', fg='#2c3e50',
                                 relief=RIDGE, bd=2)
        receipt_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        receipt_frame.grid_rowconfigure(0, weight=1)
        receipt_frame.grid_columnconfigure(0, weight=1)
        
       
        text_frame = Frame(receipt_frame)
        text_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        text_frame.grid_rowconfigure(0, weight=1)
        text_frame.grid_columnconfigure(0, weight=1)
        
        self.txtReceipt = Text(text_frame, 
                              font=('Courier New', 10),
                              bg='#ffffff', fg='#2c3e50',
                              bd=1, relief=SOLID,
                              wrap=WORD)
        self.txtReceipt.grid(row=0, column=0, sticky="nsew")
        
        
        scrollbar = Scrollbar(text_frame, orient=VERTICAL, command=self.txtReceipt.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.txtReceipt.config(yscrollcommand=scrollbar.set)
    
    def setup_calculator_frame(self, parent):
        """Setup the calculator"""
        calc_frame = LabelFrame(parent, text="🧮 Calculator", 
                              font=('Segoe UI', 12, 'bold'),
                              bg='#f8f9fa', fg='#2c3e50',
                              relief=RIDGE, bd=2)
        calc_frame.grid(row=2, column=0, sticky="ew")
        
        
        self.txtDisplay = Entry(calc_frame, textvariable=self.text_Input,
                              font=('Segoe UI', 14), 
                              bg='#ffffff', fg='#2c3e50',
                              bd=2, relief=SOLID, justify=RIGHT)
        self.txtDisplay.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5)
        
       
        self.setup_calculator_buttons(calc_frame)
    
    def setup_calculator_buttons(self, parent):
        """Setup calculator buttons"""
       
        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)
        
        button_style = {
            'font': ('Segoe UI', 12, 'bold'),
            'bd': 1,
            'relief': RAISED,
            'cursor': 'hand2'
        }
        
        
        buttons = [
            ['7', '8', '9', '+'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '*'],
            ['0', 'C', '=', '/']
        ]
        
        for row, button_row in enumerate(buttons, 1):
            for col, button_text in enumerate(button_row):
                if button_text.isdigit():
                    bg_color = '#ecf0f1'
                    command = lambda x=button_text: self.btnClick(x)
                elif button_text in ['+', '-', '*', '/']:
                    bg_color = '#3498db'
                    command = lambda x=button_text: self.btnClick(x)
                elif button_text == '=':
                    bg_color = '#27ae60'
                    command = self.btnEquals
                else:  
                    bg_color = '#e74c3c'
                    command = self.btnClear
                
                btn = Button(parent, text=button_text,
                           bg=bg_color, fg='white' if button_text != '0' and not button_text.isdigit() else '#2c3e50',
                           command=command, **button_style)
                btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
    
    def chkLatta(self):
        if self.var1.get() == 1:
            self.drink_entries["Latta"].configure(state=NORMAL)
            self.drink_entries["Latta"].focus()
            self.E_Latta.set("")
        else:
            self.drink_entries["Latta"].configure(state=DISABLED)
            self.E_Latta.set("0")
    
    def chkEspresso(self):
        if self.var2.get() == 1:
            self.drink_entries["Espresso"].configure(state=NORMAL)
            self.drink_entries["Espresso"].focus()
            self.E_Espresso.set("")
        else:
            self.drink_entries["Espresso"].configure(state=DISABLED)
            self.E_Espresso.set("0")
    
    def chkIced_Latte(self):
        if self.var3.get() == 1:
            self.drink_entries["Iced Latte"].configure(state=NORMAL)
            self.drink_entries["Iced Latte"].focus()
            self.E_Iced_Latta.set("")
        else:
            self.drink_entries["Iced Latte"].configure(state=DISABLED)
            self.E_Iced_Latta.set("0")
    
    def chkVale_Coffee(self):
        if self.var4.get() == 1:
            self.drink_entries["Vale Coffee"].configure(state=NORMAL)
            self.drink_entries["Vale Coffee"].focus()
            self.E_Vale_Coffe.set("")
        else:
            self.drink_entries["Vale Coffee"].configure(state=DISABLED)
            self.E_Vale_Coffe.set("0")
    
    def chkCappuccino(self):
        if self.var5.get() == 1:
            self.drink_entries["Cappuccino"].configure(state=NORMAL)
            self.drink_entries["Cappuccino"].focus()
            self.E_Cappuccino.set("")
        else:
            self.drink_entries["Cappuccino"].configure(state=DISABLED)
            self.E_Cappuccino.set("0")
    
    def chkAfrican_Coffee(self):
        if self.var6.get() == 1:
            self.drink_entries["African Coffee"].configure(state=NORMAL)
            self.drink_entries["African Coffee"].focus()
            self.E_African_Coffee.set("")
        else:
            self.drink_entries["African Coffee"].configure(state=DISABLED)
            self.E_African_Coffee.set("0")
    
    def chkAmerican_Coffee(self):
        if self.var7.get() == 1:
            self.drink_entries["American Coffee"].configure(state=NORMAL)
            self.drink_entries["American Coffee"].focus()
            self.E_American_Coffee.set("")
        else:
            self.drink_entries["American Coffee"].configure(state=DISABLED)
            self.E_American_Coffee.set("0")
    
    def chkIced_Cappuccino(self):
        if self.var8.get() == 1:
            self.drink_entries["Iced Cappuccino"].configure(state=NORMAL)
            self.drink_entries["Iced Cappuccino"].focus()
            self.E_Iced_Cappuccino.set("")
        else:
            self.drink_entries["Iced Cappuccino"].configure(state=DISABLED)
            self.E_Iced_Cappuccino.set("0")
    
    def chkSchool_Cake(self):
        if self.var9.get() == 1:
            self.cake_entries["School Cake"].configure(state=NORMAL)
            self.cake_entries["School Cake"].focus()
            self.E_School_Cake.set("")
        else:
            self.cake_entries["School Cake"].configure(state=DISABLED)
            self.E_School_Cake.set("0")
    
    def chkSunny_AO_Cake(self):
        if self.var10.get() == 1:
            self.cake_entries["Sunday O Cake"].configure(state=NORMAL)
            self.cake_entries["Sunday O Cake"].focus()
            self.E_Sunny_AO_Cake.set("")
        else:
            self.cake_entries["Sunday O Cake"].configure(state=DISABLED)
            self.E_Sunny_AO_Cake.set("0")
    
    def chkJonathan_YO_Cake(self):
        if self.var11.get() == 1:
            self.cake_entries["Jonathan O Cake"].configure(state=NORMAL)
            self.cake_entries["Jonathan O Cake"].focus()
            self.E_Jonathan_YO_Cake.set("")
        else:
            self.cake_entries["Jonathan O Cake"].configure(state=DISABLED)
            self.E_Jonathan_YO_Cake.set("0")
    
    def chkWest_African_Cake(self):
        if self.var12.get() == 1:
            self.cake_entries["West African Cake"].configure(state=NORMAL)
            self.cake_entries["West African Cake"].focus()
            self.E_West_African_Cake.set("")
        else:
            self.cake_entries["West African Cake"].configure(state=DISABLED)
            self.E_West_African_Cake.set("0")
    
    def chkLagos_Chocolate_Cake(self):
        if self.var13.get() == 1:
            self.cake_entries["Lagos Chocolate Cake"].configure(state=NORMAL)
            self.cake_entries["Lagos Chocolate Cake"].focus()
            self.E_Lagos_Chocolate_Cake.set("")
        else:
            self.cake_entries["Lagos Chocolate Cake"].configure(state=DISABLED)
            self.E_Lagos_Chocolate_Cake.set("0")
    
    def chkKilburn_Chocolate_Cake(self):
        if self.var14.get() == 1:
            self.cake_entries["Kilburn Chocolate Cake"].configure(state=NORMAL)
            self.cake_entries["Kilburn Chocolate Cake"].focus()
            self.E_Kilburn_Chocolate_Cake.set("")
        else:
            self.cake_entries["Kilburn Chocolate Cake"].configure(state=DISABLED)
            self.E_Kilburn_Chocolate_Cake.set("0")
    
    def chkCarlton_Hill_Cake(self):
        if self.var15.get() == 1:
            self.cake_entries["Carlton Hill Cake"].configure(state=NORMAL)
            self.cake_entries["Carlton Hill Cake"].focus()
            self.E_Carlton_Hill_Chocolate_Cake.set("")
        else:
            self.cake_entries["Carlton Hill Cake"].configure(state=DISABLED)
            self.E_Carlton_Hill_Chocolate_Cake.set("0")
    
    def chkQueen_Park_Cake(self):
        if self.var16.get() == 1:
            self.cake_entries["Queen's Park Cake"].configure(state=NORMAL)
            self.cake_entries["Queen's Park Cake"].focus()
            self.E_Queen_Park_Chocolate_Cake.set("")
        else:
            self.cake_entries["Queen's Park Cake"].configure(state=DISABLED)
            self.E_Queen_Park_Chocolate_Cake.set("0")
    
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
    
    def CostofItem(self):
        """Calculate the cost of all items"""
        try:
            items = {
                'Latta': float(self.E_Latta.get() or 0),
                'Espresso': float(self.E_Espresso.get() or 0),
                'Iced_Latta': float(self.E_Iced_Latta.get() or 0),
                'Vale_Coffe': float(self.E_Vale_Coffe.get() or 0),
                'Cappuccino': float(self.E_Cappuccino.get() or 0),
                'African_Coffee': float(self.E_African_Coffee.get() or 0),
                'American_Coffee': float(self.E_American_Coffee.get() or 0),
                'Iced_Cappuccino': float(self.E_Iced_Cappuccino.get() or 0),
                'School_Cake': float(self.E_School_Cake.get() or 0),
                'Sunny_AO_Cake': float(self.E_Sunny_AO_Cake.get() or 0),
                'Jonathan_YO_Cake': float(self.E_Jonathan_YO_Cake.get() or 0),
                'West_African_Cake': float(self.E_West_African_Cake.get() or 0),
                'Lagos_Chocolate_Cake': float(self.E_Lagos_Chocolate_Cake.get() or 0),
                'Kilburn_Chocolate_Cake': float(self.E_Kilburn_Chocolate_Cake.get() or 0),
                'Carlton_Hill_Chocolate_Cake': float(self.E_Carlton_Hill_Chocolate_Cake.get() or 0),
                'Queen_Park_Chocolate_Cake': float(self.E_Queen_Park_Chocolate_Cake.get() or 0)
            }

          
            drink_prices = {
                'Latta': 1.20, 'Espresso': 1.99, 'Iced_Latta': 2.05, 'Vale_Coffe': 1.89,
                'Cappuccino': 1.99, 'African_Coffee': 2.99, 'American_Coffee': 2.39, 'Iced_Cappuccino': 1.29
            }
            
            cake_prices = {
                'School_Cake': 1.35, 'Sunny_AO_Cake': 2.20, 'Jonathan_YO_Cake': 1.99, 'West_African_Cake': 1.49,
                'Lagos_Chocolate_Cake': 1.80, 'Kilburn_Chocolate_Cake': 1.67, 
                'Carlton_Hill_Chocolate_Cake': 1.60, 'Queen_Park_Chocolate_Cake': 1.99
            }

           
            drinks_cost = sum(items[item] * price for item, price in drink_prices.items())
            cakes_cost = sum(items[item] * price for item, price in cake_prices.items())
            
            service_charge = 1.59
            subtotal = drinks_cost + cakes_cost + service_charge
            tax = subtotal * 0.15
            total = subtotal + tax

            
            self.CostofDrinks.set(f"${drinks_cost:.2f}")
            self.CostofCakes.set(f"${cakes_cost:.2f}")
            self.ServiceCharge.set(f"${service_charge:.2f}")
            self.SubTotal.set(f"${subtotal:.2f}")
            self.PaidTax.set(f"${tax:.2f}")
            self.TotalCost.set(f"${total:.2f}")
            
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter valid numbers for quantities.")
    
    def Receipt(self):
        """Generate and display receipt, also save to database"""
        self.txtReceipt.delete("1.0", END)
        
    
        x = random.randint(10908, 500876)
        receipt_ref = f"BILL{x}"
        self.Receipt_Ref.set(receipt_ref)
        
       
        current_date = time.strftime("%d/%m/%Y")
        current_time = time.strftime("%H:%M:%S")
        
       
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        self.txtReceipt.insert(END, "      🍽️ RESTAURANT RECEIPT 🍽️\n")
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        self.txtReceipt.insert(END, f"Receipt Ref: {receipt_ref}\n")
        self.txtReceipt.insert(END, f"Date: {current_date}    Time: {current_time}\n")
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        
    
        self.txtReceipt.insert(END, "ITEMS ORDERED:\n")
        self.txtReceipt.insert(END, "-" * 50 + "\n")
        
       
        ordered_items = {}
        
     
        if float(self.E_Latta.get()) > 0:
            self.txtReceipt.insert(END, f"Latta: {self.E_Latta.get()}\n")
            ordered_items['Latta'] = float(self.E_Latta.get())
        if float(self.E_Espresso.get()) > 0:
            self.txtReceipt.insert(END, f"Espresso: {self.E_Espresso.get()}\n")
            ordered_items['Espresso'] = float(self.E_Espresso.get())
        if float(self.E_Iced_Latta.get()) > 0:
            self.txtReceipt.insert(END, f"Iced Latte: {self.E_Iced_Latta.get()}\n")
            ordered_items['Iced_Latte'] = float(self.E_Iced_Latta.get())
        if float(self.E_Vale_Coffe.get()) > 0:
            self.txtReceipt.insert(END, f"Vale Coffee: {self.E_Vale_Coffe.get()}\n")
            ordered_items['Vale_Coffee'] = float(self.E_Vale_Coffe.get())
        if float(self.E_Cappuccino.get()) > 0:
            self.txtReceipt.insert(END, f"Cappuccino: {self.E_Cappuccino.get()}\n")
            ordered_items['Cappuccino'] = float(self.E_Cappuccino.get())
        if float(self.E_African_Coffee.get()) > 0:
            self.txtReceipt.insert(END, f"African Coffee: {self.E_African_Coffee.get()}\n")
            ordered_items['African_Coffee'] = float(self.E_African_Coffee.get())
        if float(self.E_American_Coffee.get()) > 0:
            self.txtReceipt.insert(END, f"American Coffee: {self.E_American_Coffee.get()}\n")
            ordered_items['American_Coffee'] = float(self.E_American_Coffee.get())
        if float(self.E_Iced_Cappuccino.get()) > 0:
            self.txtReceipt.insert(END, f"Iced Cappuccino: {self.E_Iced_Cappuccino.get()}\n")
            ordered_items['Iced_Cappuccino'] = float(self.E_Iced_Cappuccino.get())
            
    
        if float(self.E_School_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"School Cake: {self.E_School_Cake.get()}\n")
            ordered_items['School_Cake'] = float(self.E_School_Cake.get())
        if float(self.E_Sunny_AO_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Sunday O Cake: {self.E_Sunny_AO_Cake.get()}\n")
            ordered_items['Sunday_AO_Cake'] = float(self.E_Sunny_AO_Cake.get())
        if float(self.E_Jonathan_YO_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Jonathan O Cake: {self.E_Jonathan_YO_Cake.get()}\n")
            ordered_items['Jonathan_YO_Cake'] = float(self.E_Jonathan_YO_Cake.get())
        if float(self.E_West_African_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"West African Cake: {self.E_West_African_Cake.get()}\n")
            ordered_items['West_African_Cake'] = float(self.E_West_African_Cake.get())
        if float(self.E_Lagos_Chocolate_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Lagos Chocolate Cake: {self.E_Lagos_Chocolate_Cake.get()}\n")
            ordered_items['Lagos_Chocolate_Cake'] = float(self.E_Lagos_Chocolate_Cake.get())
        if float(self.E_Kilburn_Chocolate_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Kilburn Chocolate Cake: {self.E_Kilburn_Chocolate_Cake.get()}\n")
            ordered_items['Kilburn_Chocolate_Cake'] = float(self.E_Kilburn_Chocolate_Cake.get())
        if float(self.E_Carlton_Hill_Chocolate_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Carlton Hill Cake: {self.E_Carlton_Hill_Chocolate_Cake.get()}\n")
            ordered_items['Carlton_Hill_Chocolate_Cake'] = float(self.E_Carlton_Hill_Chocolate_Cake.get())
        if float(self.E_Queen_Park_Chocolate_Cake.get()) > 0:
            self.txtReceipt.insert(END, f"Queen's Park Cake: {self.E_Queen_Park_Chocolate_Cake.get()}\n")
            ordered_items['Queen_Park_Chocolate_Cake'] = float(self.E_Queen_Park_Chocolate_Cake.get())
        
       
        self.txtReceipt.insert(END, "-" * 50 + "\n")
        self.txtReceipt.insert(END, "COST BREAKDOWN:\n")
        self.txtReceipt.insert(END, "-" * 50 + "\n")
        self.txtReceipt.insert(END, f"Cost of Drinks: {self.CostofDrinks.get()}\n")
        self.txtReceipt.insert(END, f"Cost of Cakes: {self.CostofCakes.get()}\n")
        self.txtReceipt.insert(END, f"Service Charge: {self.ServiceCharge.get()}\n")
        self.txtReceipt.insert(END, f"Sub Total: {self.SubTotal.get()}\n")
        self.txtReceipt.insert(END, f"Tax (15%): {self.PaidTax.get()}\n")
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        self.txtReceipt.insert(END, f"TOTAL COST: {self.TotalCost.get()}\n")
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        self.txtReceipt.insert(END, "Thank you for dining with us! 🍽️\n")
        self.txtReceipt.insert(END, "=" * 50 + "\n")
        self.save_order_to_database(receipt_ref, ordered_items)
    
    def save_order_to_database(self, receipt_ref, ordered_items):
        """Save order to MySQL database"""
        if not self.connection:
            tkinter.messagebox.showwarning("Database Warning", "Database connection not available. Order not saved.")
            return
        
        try:
            cursor = self.connection.cursor()
            
          
            cost_drinks = float(self.CostofDrinks.get().replace('$', '')) if self.CostofDrinks.get() else 0.0
            cost_cakes = float(self.CostofCakes.get().replace('$', '')) if self.CostofCakes.get() else 0.0
            service_charge = float(self.ServiceCharge.get().replace('$', '')) if self.ServiceCharge.get() else 0.0
            subtotal = float(self.SubTotal.get().replace('$', '')) if self.SubTotal.get() else 0.0
            tax_paid = float(self.PaidTax.get().replace('$', '')) if self.PaidTax.get() else 0.0
            total_cost = float(self.TotalCost.get().replace('$', '')) if self.TotalCost.get() else 0.0
            
            
            insert_query = """
            INSERT INTO orders (receipt_ref, order_date, order_time, items, 
                              cost_of_drinks, cost_of_cakes, service_charge, 
                              subtotal, tax_paid, total_cost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            order_data = (
                receipt_ref,
                time.strftime("%Y-%m-%d"),
                time.strftime("%H:%M:%S"),
                json.dumps(ordered_items),
                cost_drinks,
                cost_cakes,
                service_charge,
                subtotal,
                tax_paid,
                total_cost
            )
            
            cursor.execute(insert_query, order_data)
            self.connection.commit()
            
            tkinter.messagebox.showinfo("Success", f"Order {receipt_ref} saved to database successfully!")
            
        except Error as e:
            tkinter.messagebox.showerror("Database Error", f"Failed to save order: {e}")
    
    def Reset(self):
        """Reset all fields and values"""
       
        self.PaidTax.set("")
        self.SubTotal.set("")
        self.TotalCost.set("")
        self.CostofCakes.set("")
        self.CostofDrinks.set("")
        self.ServiceCharge.set("")
        
      
        self.txtReceipt.delete("1.0", END)

       
        for var in [self.E_Latta, self.E_Espresso, self.E_Iced_Latta, self.E_Vale_Coffe,
                   self.E_Cappuccino, self.E_African_Coffee, self.E_American_Coffee, self.E_Iced_Cappuccino,
                   self.E_School_Cake, self.E_Sunny_AO_Cake, self.E_Jonathan_YO_Cake, self.E_West_African_Cake,
                   self.E_Lagos_Chocolate_Cake, self.E_Kilburn_Chocolate_Cake, 
                   self.E_Carlton_Hill_Chocolate_Cake, self.E_Queen_Park_Chocolate_Cake]:
            var.set("0")
        
        
        for var in [self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.var7, self.var8,
                   self.var9, self.var10, self.var11, self.var12, self.var13, self.var14, self.var15, self.var16]:
            var.set(0)
        
       
        for entry in self.drink_entries.values():
            entry.configure(state=DISABLED)
        for entry in self.cake_entries.values():
            entry.configure(state=DISABLED)
        
        
        self.operator = ""
        self.text_Input.set("")
    
    def iExit(self):
        """Exit the application"""
        result = tkinter.messagebox.askyesno("Exit Restaurant System", 
                                           "Are you sure you want to exit the application?")
        if result:
            if self.connection and self.connection.is_connected():
                self.connection.close()
            self.root.destroy()

    def __del__(self):
        """Cleanup database connection"""
        if hasattr(self, 'connection') and self.connection and self.connection.is_connected():
            self.connection.close()
    
    

def main():
    """Main function to run the application"""
    root = Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()

if __name__ == "__main__":
   
    try:
        import mysql.connector
        main()
    except ImportError:
        print("MySQL Connector not found. Please install it using:")
        print("pip install mysql-connector-python")
        
     
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
