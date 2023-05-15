import tkinter as tk
from tkinter import ttk
import subprocess

def update_packages():
    progress_bar["value"] = 0
    progress_label["text"] = "Updating packages..."
    try:
        subprocess.check_output(["sudo", "apt", "update"])
        subprocess.check_output(["sudo", "apt-get", "update"])
        progress_bar["value"] = 100
        progress_label["text"] = "Update complete!"
    except subprocess.CalledProcessError as e:
        progress_label["text"] = "Error: {}".format(e.output)

root = tk.Tk()
root.title("Package Updater")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="Update Packages", command=update_packages).grid(column=1, row=1, sticky=tk.W)
progress_bar = ttk.Progressbar(mainframe, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress_bar.grid(column=2, row=1, sticky=tk.W)
progress_label = ttk.Label(mainframe, text="")
progress_label.grid(column=2, row=2, sticky=tk.W)

root.mainloop()
