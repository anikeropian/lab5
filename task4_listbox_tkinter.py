import tkinter as tk
from tkinter import messagebox


def show_selection():
    """Показывает выбранный элемент из списка."""
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_text = listbox.get(selected_indices[0])
        messagebox.showinfo('Выбор', f'Вы выбрали: {selected_text}')
    else:
        messagebox.showwarning('Внимание', 'Сначала выберите элемент!')


# Создание главного окна
root = tk.Tk()
root.title('Listbox и выбор элемента')
root.geometry('300x250')

# Создание списка
listbox = tk.Listbox(root, height=5, width=30)
listbox.pack(pady=10)

# Заполнение списка
for item in ['Python', 'Java', 'C++', 'JavaScript', 'C#', 'Go']:
    listbox.insert(tk.END, item)

# Кнопка выбора
btn_select = tk.Button(root, text='Выбрать элемент', command=show_selection)
btn_select.pack(pady=5)

# Запуск приложения
root.mainloop()
