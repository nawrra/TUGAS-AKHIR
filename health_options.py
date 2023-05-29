import tkinter as tk
from menstruasi_form import MenstruasiForm
from bmi_calculator import BMICalculator
from calorie_info_form import CalorieInfoForm

class HealthOptions(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("INFORMASI KESEHATAN")
        self.geometry("300x200")

        label_pilihan = tk.Label(self, text="PILIH INFORMASI!", font=("Arial", 14))
        label_pilihan.pack(pady=20)

        button_prediksi_menstruasi = tk.Button(self, text="PREDIKSI MENSTRUASI", width=20, command=self.show_hari_terakhir_menstruasi_form)
        button_prediksi_menstruasi.pack(pady=5)

        button_kalkulator_bmi = tk.Button(self, text="KALKULATOR BMI", width=20, command=self.show_bmi_calculator)
        button_kalkulator_bmi.pack(pady=5)

        button_informasi_kalori = tk.Button(self, text="AKTIVITAS-GOALS", width=20, command=self.show_calorie_info_form)
        button_informasi_kalori.pack(pady=5)

    def show_hari_terakhir_menstruasi_form(self):
        self.destroy()
        menstruasi = MenstruasiForm()
        menstruasi.show_form()

    def show_bmi_calculator(self):
        self.destroy()
        bmi_calculator = BMICalculator()
        bmi_calculator.show_calculator()

    def show_calorie_info_form(self):
        self.destroy()
        calorie_info_form = CalorieInfoForm()
        calorie_info_form.show_form()

def main():
    health_options = HealthOptions()
    health_options.mainloop()

if __name__ == "__main__":
    main()