import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("800x600")
        
        self.conn = sqlite3.connect("finance.db")
        self.create_tables()
        
        self.categories = ["Food", "Transport", "Entertainment", "Bills", "Other"]
        self.setup_gui()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                amount REAL,
                category TEXT,
                date TEXT,
                description TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT UNIQUE,
                amount REAL
            )
        """)
        self.conn.commit()
        
    def setup_gui(self):
        # Main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Transaction input
        ttk.Label(self.main_frame, text="Amount:").grid(row=0, column=0, pady=5)
        self.amount_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.amount_var).grid(row=0, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Type:").grid(row=1, column=0, pady=5)
        self.type_var = tk.StringVar(value="Expense")
        ttk.Combobox(self.main_frame, textvariable=self.type_var, 
                    values=["Income", "Expense"]).grid(row=1, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Category:").grid(row=2, column=0, pady=5)
        self.category_var = tk.StringVar()
        ttk.Combobox(self.main_frame, textvariable=self.category_var, 
                    values=self.categories).grid(row=2, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Description:").grid(row=3, column=0, pady=5)
        self.desc_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.desc_var).grid(row=3, column=1, pady=5)
        
        ttk.Button(self.main_frame, text="Add Transaction", 
                  command=self.add_transaction).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Budget setting
        ttk.Label(self.main_frame, text="Set Budget Category:").grid(row=5, column=0, pady=5)
        self.budget_category_var = tk.StringVar()
        ttk.Combobox(self.main_frame, textvariable=self.budget_category_var, 
                    values=self.categories).grid(row=5, column=1, pady=5)
        
        ttk.Label(self.main_frame, text="Budget Amount:").grid(row=6, column=0, pady=5)
        self.budget_amount_var = tk.StringVar()
        ttk.Entry(self.main_frame, textvariable=self.budget_amount_var).grid(row=6, column=1, pady=5)
        
        ttk.Button(self.main_frame, text="Set Budget", 
                  command=self.set_budget).grid(row=7, column=0, columnspan=2, pady=10)
        
        # Report buttons
        ttk.Button(self.main_frame, text="Show Transactions", 
                  command=self.show_transactions).grid(row=8, column=0, pady=5)
        ttk.Button(self.main_frame, text="Show Budget Report", 
                  command=self.show_budget_report).grid(row=8, column=1, pady=5)
        
        # Treeview for transactions
        self.tree = ttk.Treeview(self.main_frame, 
                               columns=("ID", "Type", "Amount", "Category", "Date", "Description"),
                               show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Description", text="Description")
        self.tree.grid(row=9, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=9, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
    def add_transaction(self):
        try:
            amount = float(self.amount_var.get())
            transaction_type = self.type_var.get()
            category = self.category_var.get()
            description = self.desc_var.get()
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if not category:
                messagebox.showerror("Error", "Please select a category")
                return
                
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO transactions (type, amount, category, date, description)
                VALUES (?, ?, ?, ?, ?)
            """, (transaction_type, amount, category, date, description))
            self.conn.commit()
            
            self.amount_var.set("")
            self.desc_var.set("")
            messagebox.showinfo("Success", "Transaction added successfully")
            self.show_transactions()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            
    def set_budget(self):
        try:
            category = self.budget_category_var.get()
            amount = float(self.budget_amount_var.get())
            
            if not category:
                messagebox.showerror("Error", "Please select a category")
                return
                
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO budgets (category, amount)
                VALUES (?, ?)
            """, (category, amount))
            self.conn.commit()
            
            self.budget_amount_var.set("")
            messagebox.showinfo("Success", "Budget set successfully")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
            
    def show_transactions(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)
            
    def show_budget_report(self):
        cursor = self.conn.cursor()
        
        # Get budget data
        cursor.execute("SELECT category, amount FROM budgets")
        budgets = dict(cursor.fetchall())
        
        # Get expenses by category
        cursor.execute("""
            SELECT category, SUM(amount) 
            FROM transactions 
            WHERE type = 'Expense' 
            GROUP BY category
        """)
        expenses = dict(cursor.fetchall())
        
        # Create pie chart
        fig, ax = plt.subplots()
        categories = list(set(list(budgets.keys()) + list(expenses.keys())))
        budget_values = [budgets.get(cat, 0) for cat in categories]
        expense_values = [expenses.get(cat, 0) for cat in categories]
        
        x = range(len(categories))
        width = 0.35
        
        ax.bar([i - width/2 for i in x], budget_values, width, label='Budget')
        ax.bar([i + width/2 for i in x], expense_values, width, label='Expenses')
        
        ax.set_ylabel('Amount')
        ax.set_title('Budget vs Expenses by Category')
        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=45)
        ax.legend()
        
        # Display chart in new window
        report_window = tk.Toplevel(self.root)
        report_window.title("Budget Report")
        canvas = FigureCanvasTkAgg(fig, master=report_window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    def __del__(self):
        self.conn.close()

def main():
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
