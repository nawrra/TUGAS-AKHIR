import tkinter as tk
from tkinter import messagebox
from registration_form_login import RegistrationFormLogin
from registration_form import RegistrationForm

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN")
        self.geometry("300x200")

        label_username = tk.Label(self, text="Username:")
        label_username.pack()

        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        label_password = tk.Label(self, text="Password:")
        label_password.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        button_login = tk.Button(self, text="LOGIN", command=self.login)
        button_login.pack(pady=10)

        button_register = tk.Button(self, text="REGISTER", command=self.register)
        button_register.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "naura" and password == "20022":
            self.destroy()
            registration_form = RegistrationFormLogin()
            registration_form.show_form()
        else:
            messagebox.showerror("LOGIN GAGAL", "Terjadi kesalahan saat memasukkan username atau password!")

    def register(self):
        self.destroy()
        registration_form = RegistrationForm()
        registration_form.show_form()

def main():
    login_page = LoginPage()
    login_page.mainloop()

if __name__ == "__main__":
    main()