# 🍽️ Restaurant Management System
<img width="1366" height="737" alt="image" src="https://github.com/user-attachments/assets/ee3de0aa-56b5-433a-bb5f-43a86a466271" />

This is a **Python-based Restaurant Management System** built with **Tkinter** (GUI) and **MySQL** (database).  
It allows users to:
- Manage food & drinks orders
- Calculate bills (subtotal, tax, service charge, total)
- Generate receipts
- Save orders to a MySQL database

---

## 🚀 Features
✅ GUI built with Tkinter (Drinks, Cakes, Receipt, Calculator)  
✅ Order cost calculation with tax and service charge  
✅ Auto-generated receipt with order details  
✅ Database integration with MySQL (orders & menu items)  
✅ Simple calculator built-in  
✅ Reset & Exit options  

---

## 🛠️ Requirements
- Python 3.8+  
- MySQL server running locally  
- The following Python libraries:
  ```bash
  pip install mysql-connector-python
  ```

---

## ⚙️ Setup & Installation

### Windows
```bash
python -m venv venv
venv\Scripts\activate
pip install mysql-connector-python
python main.py
```

### Linux / MacOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python
python3 main.py
```

---

## 🎮 How to Use
1. Select menu items (drinks & cakes) using checkboxes.
2. Enter the quantity of each item.
3. Click **Calculate Total** (or press `Ctrl+T`).
4. Click **Generate Receipt** to view and save receipt.
5. The order will also be stored in the MySQL database.
6. Use **Reset** (`Ctrl+R`) to clear everything.
7. Use **Exit** (`Ctrl+Q`) to close the system.

---

## 📂 Project Structure
```
📁 Restaurant-Management-System
 ┣ 📄 main.py        # Main application
 ┣ 📄 README.md      # Documentation
 ┗ 📄 requirements.txt (optional)
```

---

## 🗄️ Database Structure

### `menu_items`
| id | name                     | category | price | is_active | created_at |
|----|--------------------------|----------|-------|-----------|------------|

### `orders`
| id | receipt_ref | order_date | order_time | items (JSON) | cost_of_drinks | cost_of_cakes | service_charge | subtotal | tax_paid | total_cost | created_at |

---

## 🛠️ Troubleshooting

### ❌ Error: `mysql.connector not found`
👉 Install using:
```bash
pip install mysql-connector-python
```

### ❌ Error: `Access denied for user 'root'@'localhost'`
👉 Check your MySQL username/password inside `DB_CONFIG`.

### ❌ Error: `Can't connect to MySQL server on 'localhost'`
👉 Make sure MySQL server is running:
```bash
sudo service mysql start   # Linux
net start mysql            # Windows
```

---

## 🚧 Future Improvements
- Add **search & filter** for orders  
- Add **admin panel** to manage menu items dynamically  
- Export receipts as **PDF/Excel**  
- Add **login system** (admin / cashier)  
- Cloud database support (AWS RDS, Azure MySQL)  

---

## 📜 License
📄 [License](./LICENSE): Proprietary – Permission Required 

---

## 📖 Changelog
- **v1.0** → Initial Release (Tkinter + MySQL integration, receipt system)

---

## 🤝 Contributing
Pull requests are welcome.  
For major changes, please open an issue first to discuss what you would like to change.

---

## 🙏 Acknowledgements
- **Tkinter** – GUI library  
- **MySQL Connector** – Database driver  
- **Python** – Core language  

---

## 👨‍💻 Author
Developed as a sample **Restaurant Management System with Tkinter + MySQL**.
