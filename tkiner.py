import tkinter as tk
from tkinter import messagebox

# Dummy account data
ACCOUNTS = {
    'admin': 'password'
}

class BankApp:
    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title('Bank App - Login')

        self.signup_window = tk.Tk()
        self.signup_window.title('Bank App - Signup')
        self.signup_window.withdraw()

        self.account_window = tk.Tk()
        self.account_window.title('Bank App - Account')
        self.account_window.withdraw()

        self.current_balance = 30000

        self.create_login_window()
        self.create_signup_window()
        self.create_account_window()

    def create_login_window(self):
        login_frame = tk.Frame(self.login_window)
        login_frame.pack()

        username_label = tk.Label(login_frame, text='Username:')
        username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1)

        password_label = tk.Label(login_frame, text='Password:')
        password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(login_frame, show='*')
        self.password_entry.grid(row=1, column=1)

        login_button = tk.Button(login_frame, text='Login', command=self.login)
        login_button.grid(row=2, columnspan=2, padx=5, pady=10)

        signup_button = tk.Button(login_frame, text='Sign Up', command=self.show_signup_window)
        signup_button.grid(row=3, columnspan=2, padx=5, pady=10)

    def create_signup_window(self):
        signup_frame = tk.Frame(self.signup_window)
        signup_frame.pack()

        signup_username_label = tk.Label(signup_frame, text='New Username:')
        signup_username_label.grid(row=0, column=0)
        self.signup_username_entry = tk.Entry(signup_frame)
        self.signup_username_entry.grid(row=0, column=1)

        signup_password_label = tk.Label(signup_frame, text='New Password:')
        signup_password_label.grid(row=1, column=0)
        self.signup_password_entry = tk.Entry(signup_frame, show='*')
        self.signup_password_entry.grid(row=1, column=1)

        signup_button = tk.Button(signup_frame, text='Create Account', command=self.signup)
        signup_button.grid(row=2, columnspan=2, padx=5, pady=10)

    def create_account_window(self):
        account_frame = tk.Frame(self.account_window)
        account_frame.pack()

        balance_label = tk.Label(account_frame, text='Current Balance: ${}'.format(self.current_balance))
        balance_label.pack(padx=10, pady=5)

        deposit_button = tk.Button(account_frame, text='Deposit', command=self.deposit)
        deposit_button.pack(padx=10, pady=5)

        withdraw_button = tk.Button(account_frame, text='Withdraw', command=self.withdraw)
        withdraw_button.pack(padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in ACCOUNTS and ACCOUNTS[username] == password:
            self.login_window.withdraw()
            self.account_window.deiconify()
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password.')

    def show_signup_window(self):
        self.login_window.withdraw()
        self.signup_window.deiconify()

    def signup(self):
        new_username = self.signup_username_entry.get()
        new_password = self.signup_password_entry.get()

        if new_username and new_password:
            if new_username in ACCOUNTS:
                messagebox.showerror('Signup Failed', 'Username already exists.')
            else:
                ACCOUNTS[new_username] = new_password
                messagebox.showinfo('Signup Successful', 'Account created successfully. Please login.')
                self.signup_window.withdraw()
                self.login_window.deiconify()
                self.signup_username_entry.delete(0, tk.END)
                self.signup_password_entry.delete(0, tk.END)
        else:
            messagebox.showerror('Signup Failed', 'Please enter a username and password.')

    def deposit(self):
        amount = tk.simpledialog.askinteger('Deposit', 'Enter deposit amount:')

        if amount is not None:
            if amount > 0:
                self.current_balance += amount
                messagebox.showinfo('Deposit Successful', 'Deposit of ${} successful.'.format(amount))
                self.update_balance_label()
            else:
                messagebox.showerror('Invalid Amount', 'Please enter a positive deposit amount.')
        else:
            messagebox.showerror('Invalid Amount', 'Please enter a valid deposit amount.')

    def withdraw(self):
        amount = tk.simpledialog.askinteger('Withdraw', 'Enter withdrawal amount:')

        if amount is not None:
            if 0 < amount <= self.current_balance:
                self.current_balance -= amount
                messagebox.showinfo('Withdrawal Successful', 'Withdrawal of ${} successful.'.format(amount))
                self.update_balance_label()
            else:
                messagebox.showerror('Insufficient Funds', 'Withdrawal amount exceeds current balance.')
        else:
            messagebox.showerror('Invalid Amount', 'Please enter a valid withdrawal amount.')

    def update_balance_label(self):
        balance_label = tk.Label(self.account_window, text='Current Balance: ${}'.format(self.current_balance))
        balance_label.pack(padx=10, pady=5)


app = BankApp()
tk.mainloop()
