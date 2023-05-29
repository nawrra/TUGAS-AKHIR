import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class MenstruasiForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PREDIKSI MENSTRUASI")
        self.geometry("300x100")

        label_terakhir = tk.Label(self, text="Tanggal Terakhir Menstruasi")
        label_terakhir.pack()

        self.entry_terakhir = tk.Entry(self)
        self.entry_terakhir.pack()

        button_submit = tk.Button(self, text="Submit", command=self.predict_menstruation)
        button_submit.pack(pady=10)

    def predict_menstruation(self):
        last_period = self.entry_terakhir.get()
        try:
            last_period_date = datetime.strptime(last_period, "%d/%m/%Y")
            next_period_date = last_period_date + timedelta(days=28)
            messagebox.showinfo("PREDIKSI MENSTRUASI", f"Menstruasi Anda berikutnya diperkirakan pada {next_period_date.strftime('%d/%m/%Y')}")
        except ValueError:
            messagebox.showerror("ERRORRR", "Kesalahan Memasukkan Tanggal!")

def main():
    menstruasi = MenstruasiForm()
    menstruasi.mainloop()

if __name__ == "__main__":
    main()