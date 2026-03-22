import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == '+':
            res = num1 + num2
        elif operation == '-':
            res = num1 - num2
        elif operation == '*':
            res = num1 * num2
        elif operation == '/':
            if num2 == 0:
                label_result.config(text="Ошибка: деление на 0!")
                return
            res = num1 / num2
            
        label_result.config(text=f"Результат: {res}")
        
    except ValueError:
        label_result.config(text="Ошибка: введите числа!")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("250x200")

entry1 = tk.Entry(root, width=20, font=("Arial", 12))
entry1.pack(pady=10)

entry2 = tk.Entry(root, width=20, font=("Arial", 12))
entry2.pack(pady=5)


label_result = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)


btn_add = tk.Button(frame_buttons, text="+", width=4, font=("Arial", 12), command=lambda: calculate('+'))
btn_add.grid(row=0, column=0, padx=5)

btn_sub = tk.Button(frame_buttons, text="-", width=4, font=("Arial", 12), command=lambda: calculate('-'))
btn_sub.grid(row=0, column=1, padx=5)

btn_mul = tk.Button(frame_buttons, text="*", width=4, font=("Arial", 12), command=lambda: calculate('*'))
btn_mul.grid(row=0, column=2, padx=5)

btn_div = tk.Button(frame_buttons, text="/", width=4, font=("Arial", 12), command=lambda: calculate('/'))
btn_div.grid(row=0, column=3, padx=5)


root.mainloop()
