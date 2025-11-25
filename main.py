import tkinter as tk
from backend import suma, resta, lista

root = tk.Tk()
root.title("window")
# root.geometry("400x300")
root.configure(background="blue")
textbox1 = tk.Entry(root, width=20)
textbox1.grid(row=0, column=0, padx=5, pady=10)

textbox2 = tk.Entry(root, width=20)
textbox2.grid(row=0, column=1, padx=5, pady=10)

label = tk.Label(root, text="")
label.grid(row=1, column=0, columnspan=2, pady=5)

btn = tk.Button(root, text="sumar", command=lambda: suma(
    textbox1, textbox2, label))
btn.grid(row=2, column=0, columnspan=2, pady=10)

btn2 = tk.Button(root, text="restar",
                 command=lambda: resta(textbox1, textbox2, label))
btn2.grid(row=2, column=1, columnspan=2, pady=10)

label2 = tk.Label(root, text="")
label2.grid(row=3, column=0, columnspan=2, pady=5)

btn3 = tk.Button(root, text="historial", command=lambda: lista(label2))
btn3.grid(row=4, column=1, columnspan=2, pady=10)


root.mainloop()
