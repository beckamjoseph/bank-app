import tkinter as tk
from tkinter import messagebox, simpledialog


class BankApp:
    def __init__(self):
        self.password_entry = None
        self.username_entry = None
        self.login_window = tk.Tk()
        self.login_window.title('JABS BANK')
        self.login_window.geometry("300x500")
        self.create_login_window()

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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'Admin' and password == '1234':
            self.login_window.withdraw()
            self.show_account_selection()
        else:
            messagebox.showerror('Login Failed', 'Invalid username or password.')

    def show_account_selection(self):
        selection_window = tk.Toplevel()
        selection_window.title('Bank App - Account Selection')

        savings_button = tk.Button(selection_window, text='Savings Account', command=self.show_savings_account)
        savings_button.pack(padx=10, pady=5)

        current_button = tk.Button(selection_window, text='Current Account', command=self.show_current_account)
        current_button.pack(padx=10, pady=5)

    def show_savings_account(self):
        savings_window = tk.Toplevel()
        savings_window.title('Bank App - Savings Account')

        deposit_button = tk.Button(savings_window, text='Deposit', command=self.deposit_savings)
        deposit_button.pack(padx=10, pady=5)

        withdraw_button = tk.Button(savings_window, text='Withdraw', command=self.withdraw_savings)
        withdraw_button.pack(padx=10, pady=5)

    def deposit_savings(self):
        amount = self.show_dialog('Deposit', 'Enter deposit amount:')
        if amount is not None:
            if amount <= 5000:
                messagebox.showinfo('Deposit Successful', 'Deposit of {} accepted.'.format(amount))
            else:
                messagebox.showerror('Deposit Failed', 'You can only deposit an amount on or below 5000.')

    def withdraw_savings(self):
        amount = self.show_dialog('Withdraw', 'Enter withdrawal amount:')
        if amount is not None:
            if amount <= 10000:
                messagebox.showinfo('Withdrawal Successful', 'Withdrawal of {} accepted.'.format(amount))
            else:
                messagebox.showerror('No Cash', 'Insufficient fund you can only withdraw 10000.')

    def show_current_account(self):
        current_window = tk.Toplevel()
        current_window.title('Bank App - Current Account')

        deposit_button = tk.Button(current_window, text='Deposit', command=self.deposit_current)
        deposit_button.pack(padx=10, pady=5)

        withdraw_button = tk.Button(current_window, text='Withdraw', command=self.withdraw_current)
        withdraw_button.pack(padx=10, pady=5)

    def deposit_current(self):
        amount = self.show_dialog('Deposit', 'Enter deposit amount:')
        if amount is not None:
            messagebox.showinfo('Deposit Successful', 'Deposit of {} accepted.'.format(amount))

    def withdraw_current(self):
        amount = self.show_dialog('Withdraw', 'Enter withdrawal amount:')
        if amount is not None:
            if amount <= 10000:
                messagebox.showinfo('Withdrawal Successful', 'Withdrawal of {} accepted.'.format(amount))
            else:
                messagebox.showerror('Sorry Blud ', 'Insufficient funds. You can only withdraw (10000).')

    @staticmethod
    def show_dialog(title, prompt):
        value = tk.simpledialog.askinteger(title, prompt)
        return value


app = BankApp()
tk.mainloop()
