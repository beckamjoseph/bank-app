import tkinter as tk
from tkinter import messagebox

class Bank:
    def __init__(self):
        self.savings_balance = 2000
        self.current_balance = 3000

    def deposit_savings(self, amount):
        if amount > 20000:
            messagebox.showinfo("Error", "You can only deposit up to 20000 in savings.")
        else:
            self.savings_balance += amount
            messagebox.showinfo("Success", "Deposit successful!")

    def withdraw_savings(self, amount):
        if amount > 5000:
            messagebox.showinfo("Error", "You can only withdraw up to 5000 from savings.")
        elif amount > self.savings_balance:
            messagebox.showinfo("Error", "Insufficient balance in savings account.")
        else:
            self.savings_balance -= amount
            messagebox.showinfo("Success", "Withdrawal successful!")

    def deposit_current(self, amount):
        self.current_balance += amount
        messagebox.showinfo("Success", "Deposit successful!")

    def withdraw_current(self, amount):
        if amount > self.current_balance:
            messagebox.showinfo("Error", "Insufficient balance in current account.")
        else:
            self.current_balance -= amount
            messagebox.showinfo("Success", "Withdrawal successful!")

bank = Bank()

def open_signup_window():
    signup_window = tk.Toplevel(window)
    signup_window.title("Sign Up")
    signup_window.geometry("300x200")

    # Sign up logic here

def open_account_window():
    account_window = tk.Toplevel(window)
    account_window.title("Account")
    account_window.geometry("300x200")

    savings_button = tk.Button(account_window, text="Savings Account", command=open_savings_window)
    savings_button.pack(pady=20)

    current_button = tk.Button(account_window, text="Current Account", command=open_current_window)
    current_button.pack(pady=10)

def open_savings_window():
    savings_window = tk.Toplevel(window)
    savings_window.title("Savings Account")
    savings_window.geometry("300x200")

    deposit_button = tk.Button(savings_window, text="Deposit", command=open_savings_deposit_window)
    deposit_button.pack(pady=20)

    withdraw_button = tk.Button(savings_window, text="Withdraw", command=open_savings_withdraw_window)
    withdraw_button.pack(pady=10)

def open_savings_deposit_window():
    deposit_window = tk.Toplevel(window)
    deposit_window.title("Savings Deposit")
    deposit_window.geometry("300x200")

    def deposit():
        amount = float(amount_entry.get())
        bank.deposit_savings(amount)

    amount_label = tk.Label(deposit_window, text="Amount:")
    amount_label.pack(pady=10)

    amount_entry = tk.Entry(deposit_window)
    amount_entry.pack(pady=5)

    deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit)
    deposit_button.pack(pady=10)

def open_savings_withdraw_window():
    withdraw_window = tk.Toplevel(window)
    withdraw_window.title("Savings Withdraw")
    withdraw_window.geometry("300x200")

    def withdraw():
        amount = float(amount_entry.get())
        bank.withdraw_savings(amount)

    amount_label = tk.Label(withdraw_window, text="Amount:")
    amount_label.pack(pady=10)

    amount_entry = tk.Entry(withdraw_window)
    amount_entry.pack(pady=5)

    withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw)
    withdraw_button.pack(pady=10)

def open_current_window():
    current_window = tk.Toplevel(window)
    current_window.title("Current Account")
    current_window.geometry("300x200")

    deposit_button = tk.Button(current_window, text="Deposit", command=open_current_deposit_window)
    deposit_button.pack(pady=20)

    withdraw_button = tk.Button(current_window, text="Withdraw", command=open_current_withdraw_window)
    withdraw_button.pack(pady=10)

def open_current_deposit_window():
    deposit_window = tk.Toplevel(window)
    deposit_window.title("Current Deposit")
    deposit_window.geometry("300x200")

    def deposit():
        amount = float(amount_entry.get())
        bank.deposit_current(amount)
        messagebox.showinfo("Balance", f"Current Balance: {bank.current_balance}")

    amount_label = tk.Label(deposit_window, text="Amount:")
    amount_label.pack(pady=10)

    amount_entry = tk.Entry(deposit_window)
    amount_entry.pack(pady=5)

    deposit_button = tk.Button(deposit_window, text="Deposit", command=deposit)
    deposit_button.pack(pady=10)

def open_current_withdraw_window():
    withdraw_window = tk.Toplevel(window)
    withdraw_window.title("Current Withdraw")
    withdraw_window.geometry("300x200")

    def withdraw():
        amount = float(amount_entry.get())
        bank.withdraw_current(amount)
        messagebox.showinfo("Balance", f"Current Balance: {bank.current_balance}")

    amount_label = tk.Label(withdraw_window, text="Amount:")
    amount_label.pack(pady=10)

    amount_entry = tk.Entry(withdraw_window)
    amount_entry.pack(pady=5)

    withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=withdraw)
    withdraw_button.pack(pady=10)

window = tk.Tk()
window.title("Bank User Interface")

signup_button = tk.Button(window, text="Sign Up", command=open_signup_window)
signup_button.pack(pady=20)

login_button = tk.Button(window, text="Login", command=open_account_window)
login_button.pack(pady=10)

window.mainloop()
