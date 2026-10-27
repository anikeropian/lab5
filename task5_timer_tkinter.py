import tkinter as tk


class TimerApp:
    """Секундомер на Tkinter."""

    def __init__(self, root):
        self.root = root
        self.root.title('Секундомер')
        self.root.geometry('300x200')

        self.running = False
        self.time_elapsed = 0

        self.label = tk.Label(root, text='00:00:00', font=('Arial', 24))
        self.label.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.btn_start = tk.Button(btn_frame, text='Старт', command=self.start)
        self.btn_start.pack(side=tk.LEFT, padx=5)

        self.btn_stop = tk.Button(btn_frame, text='Стоп', command=self.stop)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        self.btn_reset = tk.Button(btn_frame, text='Сброс', command=self.reset)
        self.btn_reset.pack(side=tk.LEFT, padx=5)

    def update_time(self):
        """Обновляет время на экране."""
        if self.running:
            self.time_elapsed += 1
            hours = self.time_elapsed // 3600
            minutes = (self.time_elapsed % 3600) // 60
            seconds = self.time_elapsed % 60
            self.label.config(text=f'{hours:02d}:{minutes:02d}:{seconds:02d}')
            self.root.after(1000, self.update_time)

    def start(self):
        """Запускает секундомер."""
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        """Останавливает секундомер."""
        self.running = False

    def reset(self):
        """Сбрасывает время на ноль."""
        self.running = False
        self.time_elapsed = 0
        self.label.config(text='00:00:00')


if __name__ == '__main__':
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
