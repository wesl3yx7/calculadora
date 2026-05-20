from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry("408x355")
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ""
divisao = FALSE
multiplicacao = FALSE
soma = FALSE
subtracao = FALSE

root.configure(bg="#000000")

e = Entry(root, width=15, borderwidth=3, relief=FLAT, fg="#FFFFFF", bg="#a7a28f", font=("futura", 24, "bold"), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=3,
    pady=2,
)
#funcoes operadores
def button_click(num):
    e.insert(END, num)
def button_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def button_multiplicacao():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def button_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)

def button_soma():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)

def button_limpar():
    e.delete(0, END)
def button_igual():
    global subtracao
    global soma
    global multiplicacao
    global divisao
    numero2 = e.get()
    e.delete(0, END)

    if soma == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        soma = FALSE

    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE

    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE

    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE

divide = Button(root,
                text="÷",
                padx=40,
                pady=20,
                command=button_divisao,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#59543D",
                activebackground="#59543D",
                relief=FLAT,
                font=("futura", 12, "bold")
)
divide.grid(row=0, column=4)
#primeira filheira
um = Button(root,
                text="1",
                padx=40,
                pady=20,
                command=lambda: button_click(1),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
um.grid(row=1, column=0)

dois = Button(root,
                text="2",
                padx=40,
                pady=20,
                command=lambda: button_click(2),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
dois.grid(row=1, column=1)

tres = Button(root,
                text="3",
                padx=40,
                pady=20,
                command=lambda: button_click(3),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
tres.grid(row=1, column=2)

multiplicacao = Button(root,
                text="x",
                padx=40,
                pady=20,
                command=button_multiplicacao,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#59543D",
                activebackground="#59543D",
                relief=FLAT,
                font=("futura", 12, "bold")
)
multiplicacao.grid(row=1, column=4)
#segunda filheira

quatro = Button(root,
                text="4",
                padx=40,
                pady=20,
                command=lambda: button_click(4),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
quatro.grid(row=2, column=0)


cinco = Button(root,
                text="5",
                padx=40,
                pady=20,
                command=lambda: button_click(5),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
cinco.grid(row=2, column=1)

seis = Button(root,
                text="6",
                padx=40,
                pady=20,
                command=lambda: button_click(6),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
seis.grid(row=2, column=2)

menos = Button(root,
                text="-",
                padx=41.5,
                pady=20,
                command=button_subtracao,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#59543D",
                activebackground="#59543D",
                relief=FLAT,
                font=("futura", 12, "bold")
)
menos.grid(row=2, column=4)
#terceira filheira

sete = Button(root,
                text="7",
                padx=40,
                pady=20,
                command=lambda: button_click(7),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
sete.grid(row=3, column=0)

oito = Button(root,
                text="8",
                padx=40,
                pady=20,
                command=lambda: button_click(8),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
oito.grid(row=3, column=1)

nove = Button(root,
                text="9",
                padx=40,
                pady=20,
                command=lambda: button_click(9),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
nove.grid(row=3, column=2)

soma = Button(root,
                text="+",
                padx=40,
                pady=20,
                command=button_soma,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#59543D",
                activebackground="#59543D",
                relief=FLAT,
                font=("futura", 12, "bold")
)
soma.grid(row=3, column=4)

zero = Button(root,
                text="0",
                padx=91,
                pady=20,
                command=lambda: button_click(0),
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
zero.grid(row=4, column=0, columnspan=2)

limpar = Button(root,
                text="C",
                padx=38,
                pady=20,
                command=button_limpar,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#0A1738",
                activebackground="#0A1738",
                relief=FLAT,
                font=("futura", 12, "bold")
)
limpar.grid(row=4, column=2)

igual= Button(root,
                text="=",
                padx=40,
                pady=20,
                command=button_igual,
                fg="#FFFFFF",
                activeforeground="#FFFFFF",
                bg="#59543D",
                activebackground="#59543D",
                relief=FLAT,
                font=("futura", 12, "bold")
)
igual.grid(row=4, column=4)

root.mainloop()