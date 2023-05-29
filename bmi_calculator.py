import tkinter as tk

class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KALKULATOR BMI")
        self.geometry("300x200")

        label_berat = tk.Label(self, text="Berat (kg):")
        label_berat.pack()

        self.entry_berat = tk.Entry(self)
        self.entry_berat.pack()

        label_tinggi = tk.Label(self, text="Tinggi (cm):")
        label_tinggi.pack()

        self.entry_tinggi = tk.Entry(self)
        self.entry_tinggi.pack()

        button_submit = tk.Button(self, text="Hitung", command=self.calculate_bmi)
        button_submit.pack(pady=10)

        self.label_bmi = tk.Label(self, text="BMI:")
        self.label_bmi.pack()

        self.label_kategori = tk.Label(self, text="Kategori:")
        self.label_kategori.pack()

    def calculate_bmi(self):
        berat = float(self.entry_berat.get())
        tinggi = float(self.entry_tinggi.get())

        bmi = berat / ((tinggi/100) ** 2)

        self.label_bmi.config(text="BMI: {:.2f}".format(bmi))

        if bmi < 18.5:
            self.label_kategori.config(text="Kategori: Berat Badan Kurang")
        elif bmi < 24.9:
            self.label_kategori.config(text="Kategori: Berat Badan Normal")
        elif bmi < 29.9:
            self.label_kategori.config(text="Kategori: Berat Badan Berlebih")
        else:
            self.label_kategori.config(text="Kategori: Obesitas")

def main():
    bmi_calculator = BMICalculator()
    bmi_calculator.mainloop()

if __name__ == "__main__":
    main()