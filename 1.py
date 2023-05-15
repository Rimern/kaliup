import subprocess
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Обновление пакетов и приложений")
        self.window.geometry("400x200")

        self.progress_label = ttk.Label(self.window, text="Прогресс:")
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.window, length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.update_button = ttk.Button(self.window, text="Обновить", command=self.update_packages)
        self.update_button.pack(pady=10)

    def update_packages(self):
        subprocess.Popen(["sudo", "apt", "update"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo", "apt-get", "update"], stdout=subprocess.PIPE)

        self.progress_bar.start(10)

        self.check_progress()

    def check_progress(self):
        process = subprocess.Popen(["apt-get", "update"], stdout=subprocess.PIPE)
        output = process.communicate()[0].decode("utf-8")

        progress = 0
        if "Reading package lists..." in output:
            progress = 50
        if "Building dependency tree" in output:
            progress = 75
        if "Reading state information" in output:
            progress = 100

        self.progress_bar["value"] = progress

        if progress < 100:
            self.window.after(1000, self.check_progress)
        else:
            self.progress_bar.stop()

if __name__ == "__main__":
    app = App()
    app.window.mainloop()
