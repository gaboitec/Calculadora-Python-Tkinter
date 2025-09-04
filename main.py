import tkinter as tk

vent = tk.Tk()
vent.geometry("300x300")
vent.title("Calculator")

result = tk.Label(vent, text="")
result.pack(pady=2)
num1 = tk.Entry(vent)
num1.pack(pady=30)
num2 = tk.Entry(vent)
num2.pack(pady=5)

def suma():
    val1 = int(num1.get())
    val2 = int(num2.get())
    result.config(text=f"{val1 + val2}")

def resta():
    val1 = int(num1.get())
    val2 = int(num2.get())
    result.config(text=f"{val1 - val2}")

btn_sum = tk.Button(vent, text="+", command=suma)
btn_sum.pack(pady=2)

btn_rest = tk.Button(vent,text="-", command=resta)
btn_rest.pack(pady=2)

vent.mainloop()

