import tkinter as tk
from tkinter import ttk, scrolledtext

window = tk.Tk()
window.title("Регистрационная страница электронной библиотеки")
window.geometry("580x750")
window.configure(bg="pink")

# Основной контейнер с отступами
main_frame = tk.Frame(window, bg="pink")
main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Заголовок
title = tk.Label(main_frame, text="Регистрационная страница электронной библиотеки",
                 font=("Arial", 14, "bold"), bg="pink")
title.pack(anchor="w", pady=(0, 5))

# Подзаголовок
subtitle = tk.Label(main_frame, text="Заполнив анкету, вы сможете пользоваться нашей электронной библиотекой",
                    font=("Arial", 10), bg="pink", anchor="w")
subtitle.pack(anchor="w", pady=(0, 15))

# Поля ввода (сетка)
grid_frame = tk.Frame(main_frame, bg="pink")
grid_frame.pack(anchor="w")

# Строка 0
tk.Label(grid_frame, text="Введите регистрационное имя", bg="pink", anchor="w").grid(row=0, column=0, sticky="w", padx=(0, 10), pady=5)
entry_name = tk.Entry(grid_frame, width=25)
entry_name.grid(row=0, column=1, padx=(0, 20), pady=5)

# Строка 1
tk.Label(grid_frame, text="Введите пароль", bg="pink", anchor="w").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=5)
entry_pass = tk.Entry(grid_frame, width=25, show="*")
entry_pass.grid(row=1, column=1, padx=(0, 20), pady=5)

# Строка 2
tk.Label(grid_frame, text="Подтвердите пароль", bg="pink", anchor="w").grid(row=2, column=0, sticky="w", padx=(0, 10), pady=5)
entry_confirm = tk.Entry(grid_frame, width=25, show="*")
entry_confirm.grid(row=2, column=1, padx=(0, 20), pady=5)

# Возраст (радиокнопки в строку)
tk.Label(grid_frame, text="Ваш возраст", bg="pink", anchor="w").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=5)
age_frame = tk.Frame(grid_frame, bg="pink")
age_frame.grid(row=3, column=1, sticky="w")
age_var = tk.StringVar(value="")
tk.Radiobutton(age_frame, text="До 20", variable=age_var, value="20-", bg="pink").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(age_frame, text="20-30", variable=age_var, value="20-30", bg="pink").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(age_frame, text="30-50", variable=age_var, value="30-50", bg="pink").pack(side=tk.LEFT, padx=5)
tk.Radiobutton(age_frame, text="Старше 50", variable=age_var, value="50+", bg="pink").pack(side=tk.LEFT, padx=5)

# Языки (чекбоксы в строку)
tk.Label(grid_frame, text="На каких языках читаете:", bg="pink", anchor="w").grid(row=4, column=0, sticky="w", padx=(0, 10), pady=5)
lang_frame = tk.Frame(grid_frame, bg="pink")
lang_frame.grid(row=4, column=1, sticky="w")
lang_ru = tk.BooleanVar()
lang_en = tk.BooleanVar()
lang_fr = tk.BooleanVar()
lang_de = tk.BooleanVar()
tk.Checkbutton(lang_frame, text="русский", variable=lang_ru, bg="pink").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(lang_frame, text="английский", variable=lang_en, bg="pink").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(lang_frame, text="французский", variable=lang_fr, bg="pink").pack(side=tk.LEFT, padx=5)
tk.Checkbutton(lang_frame, text="немецкий", variable=lang_de, bg="pink").pack(side=tk.LEFT, padx=5)

# Предпочтительный формат
tk.Label(grid_frame, text="Какой формат данных является для вас предпочтительным?", bg="pink", anchor="w").grid(row=5, column=0, sticky="w", padx=(0, 10), pady=5)
format_var = tk.StringVar()
format_combo = ttk.Combobox(grid_frame, textvariable=format_var, values=["HTML", "Plain text"], state="readonly", width=23)
format_combo.grid(row=5, column=1, sticky="w", pady=5)
format_combo.current(0)

# Ваши любимые авторы - большое окно с прокруткой
tk.Label(main_frame, text="Ваши любимые авторы:", bg="pink", anchor="w", font=("Arial", 10, "bold")).pack(anchor="w", pady=(15, 5))
authors_text = scrolledtext.ScrolledText(main_frame, width=60, height=5)
authors_text.pack(pady=(0, 10), anchor="w")

# Кнопки OK и Отменить
button_frame = tk.Frame(main_frame, bg="pink")
button_frame.pack(pady=10)

def ok_action():
    print("Имя:", entry_name.get())
    print("Пароль:", entry_pass.get())
    print("Возраст:", age_var.get())
    print("Языки: русский={}, английский={}, французский={}, немецкий={}".format(lang_ru.get(), lang_en.get(), lang_fr.get(), lang_de.get()))
    print("Формат:", format_var.get())
    print("Авторы:", authors_text.get("1.0", tk.END))

def cancel_action():
    entry_name.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    entry_confirm.delete(0, tk.END)
    age_var.set("")
    lang_ru.set(False)
    lang_en.set(False)
    lang_fr.set(False)
    lang_de.set(False)
    format_combo.current(0)
    authors_text.delete("1.0", tk.END)

tk.Button(button_frame, text="OK", width=10, command=ok_action).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Отменить", width=10, command=cancel_action).pack(side=tk.LEFT, padx=10)

# Текст "Проверка PHP Лабораторные по базам данных"
line1 = tk.Label(main_frame, text="Проверка PHP Лабораторные по базам данных", bg="pink", anchor="center")
line1.pack(pady=(20, 0), anchor="center")

# Кнопка "Лабораторные по базам данных"
lab_button = tk.Button(main_frame, text="Лабораторные по базам данных")
lab_button.pack(pady=(5, 15), anchor="center")

# Последний абзац - по центру
last_text = tk.Label(main_frame,
                     text="Сегодня замечательный день.\nЯ сделал свою первую интернет страничку.\n",
                     bg="pink", justify="center", anchor="center")
last_text.pack(anchor="center")

# Синий текст
blue_text = tk.Label(main_frame, text="я буду богатым и свободным человеком!",
                     fg="blue", bg="pink", justify="center", anchor="center")
blue_text.pack(anchor="center")

window.mainloop()
