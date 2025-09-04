import tkinter as tk

vent = tk.Tk()
vent.geometry("300x300")
vent.title("Calculator")

result = tk.Label(vent, text="<<Resultado>>")
result.pack(pady=2)
lab1 = tk.Label(vent, text="Numero 1")
lab1.pack(pady=2)
num1 = tk.Entry(vent)
num1.pack(pady=5)
lab2 = tk.Label(vent, text="Numero 2")
lab2.pack(pady=2)
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

def mult():
    val1 = int(num1.get())
    val2 = int(num2.get())
    result.config(text=f"{val1 * val2}")

def div():
    val1 = int(num1.get())
    val2 = int(num2.get())
    if val2 == 0:
        error.config(text="Division por cero")
        return
    result.config(text=f"{val1 / val2}")

btn_sum = tk.Button(vent, text="+", command=suma)
btn_sum.pack(pady=2)

btn_rest = tk.Button(vent,text="-", command=resta)
btn_rest.pack(pady=2)

btn_mult = tk.Button(vent, text="*", command=mult)
btn_mult.pack(pady=2)

btn_div = tk.Button(vent, text="/", command=div)
btn_div.pack(pady=2)

error = tk.Label(vent, text="")
error.pack(pady=5)

vent.mainloop()

