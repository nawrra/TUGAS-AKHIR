import tkinter as tk

class CalorieInfoForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AKTIVITAS-GOALS")
        self.geometry("300x300")

        label_aktivitas = tk.Label(self, text="Pilih Aktivitas Anda:")
        label_aktivitas.pack()

        self.var_aktivitas = tk.StringVar()
        self.var_aktivitas.set(str)
        rb_aktivitas1 = tk.Radiobutton(self, text="Menetap", variable=self.var_aktivitas, value="Menetap")
        rb_aktivitas1.pack()
        rb_aktivitas2 = tk.Radiobutton(self, text="Sedikit Aktif", variable=self.var_aktivitas, value="Sedikit Aktif")
        rb_aktivitas2.pack()
        rb_aktivitas3 = tk.Radiobutton(self, text="Cukup Aktif", variable=self.var_aktivitas, value="Cukup Aktif")
        rb_aktivitas3.pack()
        rb_aktivitas4 = tk.Radiobutton(self, text="Sangat Aktif", variable=self.var_aktivitas, value="Sangat Aktif")
        rb_aktivitas4.pack()

        label_goal = tk.Label(self, text="Pilih Goals Anda:")
        label_goal.pack()

        self.var_goal = tk.StringVar()
        self.var_goal.set(str)
        rb_goal1 = tk.Radiobutton(self, text="Menurunkan Berat Badan", variable=self.var_goal, value="Menurunkan Berat Badan")
        rb_goal1.pack()
        rb_goal2 = tk.Radiobutton(self, text="Menjaga Berat Badan", variable=self.var_goal, value="Menjaga Berat Badan")
        rb_goal2.pack()
        rb_goal3 = tk.Radiobutton(self, text="Menambah Berat Badan", variable=self.var_goal, value="Menambah Berat Badan")
        rb_goal3.pack()

        button_submit = tk.Button(self, text="Submit", command=self.calculate_calorie)
        button_submit.pack(pady=10)

        self.label_calorie = tk.Label(self, text="Total Kalori:")
        self.label_calorie.pack()

    def calculate_calorie(self):
        aktivitas = self.var_aktivitas.get()
        goal = self.var_goal.get()

        if aktivitas == "Sedentary":
            activity_factor = 1.2
        elif aktivitas == "Lightly Active":
            activity_factor = 1.375
        elif aktivitas == "Moderately Active":
            activity_factor = 1.55
        else:
            activity_factor = 1.725

        if goal == "Lose Weight":
            calorie_factor = 0.8
        elif goal == "Maintain Weight":
            calorie_factor = 1.0
        else:
            calorie_factor = 1.2

        calorie_intake = 2000 * activity_factor * calorie_factor
        self.label_calorie.config(text="Total Kalori: {:.0f}".format(calorie_intake))

def main():
    calorie_info_form = CalorieInfoForm()
    calorie_info_form.mainloop()

if __name__ == "__main__":
    main()