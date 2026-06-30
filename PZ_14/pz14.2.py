import tkinter as tk


def show_message(title, message, is_error=True):
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry("450x180")
    dialog.resizable(False, False)
    dialog.transient(root)
    dialog.grab_set()  #

    text_color = "red" if is_error else "#d35400"

    msg_label = tk.Label(
        dialog,
        text=message,
        font=("Segoe UI", 12),
        fg=text_color,
        wraplength=400,
        justify="center"
    )
    msg_label.pack(expand=True, padx=20, pady=10)

    ok_button = tk.Button(
        dialog,
        text="OK",
        font=("Segoe UI", 11),
        width=8,
        command=dialog.destroy
    )
    ok_button.pack(pady=5)

    dialog.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (dialog.winfo_width() // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (dialog.winfo_height() // 2)
    dialog.geometry(f"+{x}+{y}")

    dialog.wait_window()

def calculate_day():
    try:
        k = int(entry_k.get())

        if not (1 <= k <= 365):
            show_message(
                "Неверный ввод",
                "Число K должно быть целым и находиться в диапазоне от 1 до 365.",
                is_error=False
            )
            return

        day_number = (4 + (k - 1)) % 7

        days_of_week = {
            0: "Воскресенье", 1: "Понедельник", 2: "Вторник",
            3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота"
        }

        result_label.config(
            text=f"Номер дня недели: {day_number}\n({days_of_week[day_number]})",
            fg="green"
        )

    except ValueError:
        show_message(
            "Ошибка ввода",
            "Пожалуйста, введите корректное целое число (например: 42).",
            is_error=True
        )


root = tk.Tk()
root.title("Определение дня недели")
root.geometry("550x400")
root.resizable(False, False)

task_text = (
    "Дни недели пронумерованы следующим образом:\n"
    "0 — воскресенье, 1 — понедельник, 2 — вторник,\n"
    ". . . , 6 — суббота.\n"
    "Дано целое число K, лежащее в диапазоне 1-365.\n"
    "Определить номер дня недели для K-го дня года,\n"
    "если известно, что в этом году 1 января было четвергом."
)

tk.Label(
    root,
    text=task_text,
    font=("Segoe UI", 11),
    justify="center"
).pack(pady=10, padx=10)

tk.Label(root, text="Введите номер дня года (K):", font=("Segoe UI", 12)).pack(pady=10)

entry_k = tk.Entry(root, font=("Segoe UI", 14), justify="center", width=10)
entry_k.pack(pady=5)
entry_k.focus()

btn_calc = tk.Button(
    root,
    text="Определить день недели",
    font=("Segoe UI", 12),
    bg="#e1e1e1",
    command=calculate_day
)
btn_calc.pack(pady=15)

result_label = tk.Label(root, text="", font=("Segoe UI", 14, "bold"))
result_label.pack(pady=10)

root.bind('<Return>', lambda event: calculate_day())

root.mainloop()
