import tkinter as tk
from tkinter import messagebox
from health_options import HealthOptions

class RegistrationFormLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PROFILE")
        self.geometry("300x300")

        label_nama = tk.Label(self, text="Nama:")
        label_nama.pack()

        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack()

        label_umur = tk.Label(self, text="Umur:")
        label_umur.pack()

        self.entry_umur = tk.Entry(self)
        self.entry_umur.pack()

        label_jk = tk.Label(self, text="Jenis Kelamin:")
        label_jk.pack()

        self.jenis_kelamin = tk.StringVar()
        self.jenis_kelamin.set(str)

        rb_pria = tk.Radiobutton(self, text="Pria", variable=self.jenis_kelamin, value="Pria")
        rb_pria.pack()

        rb_wanita = tk.Radiobutton(self, text="Wanita", variable=self.jenis_kelamin, value="Wanita")
        rb_wanita.pack()

        label_berat_badan = tk.Label(self, text="Berat Badan:")
        label_berat_badan.pack()

        self.entry_berat_badan = tk.Entry(self)
        self.entry_berat_badan.pack()

        label_tinggi_badan = tk.Label(self, text="Tinggi Badan:")
        label_tinggi_badan.pack()

        self.entry_tinggi_badan = tk.Entry(self)
        self.entry_tinggi_badan.pack()

        button_register = tk.Button(self, text="SUBMIT", command=self.register_submit)
        button_register.pack(pady=10)

    def register_submit(self):
        self.destroy()
        health_options = HealthOptions()
        health_options.show_options()

def main():
    registration_form = RegistrationFormLogin()
    registration_form.mainloop()

if __name__ == "__main__":
    main()