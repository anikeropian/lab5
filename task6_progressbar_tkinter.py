import tkinter as tk
from tkinter import ttk
import time


def start_progress():
    """Запускает заполнение прогрессбара."""
    progress['value'] = 0
    btn['state'] = 'disabled'
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.02)
    btn['state'] = 'normal'


root = tk.Tk()
root.title('Прогрессбар')
root.geometry('300x150')

progress = ttk.Progressbar(root, orient='horizontal', length=250, mode='determinate')
progress.pack(pady=20)

btn = tk.Button(root, text='Запустить', command=start_progress)
btn.pack(pady=10)

root.mainloop()
