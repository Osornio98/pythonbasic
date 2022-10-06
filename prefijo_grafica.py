
from tkinter import *

raiz =  Tk()
raiz.title("Notacion Prefija")
raiz.resizable(False, False)

frame1 = Frame(raiz)
frame1.pack()
frame2 = Frame(raiz)
frame2.pack()

infijax = StringVar()
resultado = StringVar()
prefijax = StringVar()

titulolabel = Label(frame1, text="INFIJA A PREFIJA", font=24).grid(row= 0, column=1, padx=10, pady=10)

infijalabel = Label(frame2, text="Ingresa la expresion infija:").grid(row= 0, column= 0, padx=10, pady=10)
infija = Entry(frame2, textvariable=infijax).grid(row= 0, column= 1, padx=10, pady=10)

prefijalabel = Label(frame2, text="Prefija").grid(row= 1, column=0, padx=10, pady=10)
prefijavista = Entry(frame2, textvariable=prefijax, state=DISABLED).grid(row=1, column=1, padx=10, pady=10)

resultadolabel = Label(frame2, text="Resultado =").grid(row=2, column=0,padx=10, pady=10)
resultadox = Entry(frame2, textvariable=resultado, state=DISABLED).grid(row=2, column=1, padx=10, pady=10) 

def codigoprefija():
    infijalist = ""
    infijalist+= infijax.get()
    prefija = []
    resultados = []
    for i in infijalist:
        if str.isdigit(i):
            prefija.append(i)
        else: 
            prefija.insert(0,i)
            
    for a in prefija[::-1]:
        if str.isdigit(a):
            resultados.append(int(a))
        else:
            va1 = resultados.pop()
            va2 = resultados.pop()

            if a == '+':
                resultados.append(va1 + va2)
            elif a == '-':
                resultados.append(va1 - va2)
            elif a == '*':
                resultados.append(va1 * va2)
            elif a == '/':
                resultados.append(va1 / va2)
            
    prefijax.set(prefija)
    resultado.set(resultados)

Baceptar = Button(raiz, text= "Aceptar", command= codigoprefija)
Baceptar.pack(padx=10, pady=10)

def eliminar():
    infijax.set('')
    prefijax.set('')
    resultado.set('')

Beliminar = Button(raiz, text="Eliminiar", command= eliminar)
Beliminar.pack(padx=10, pady=10)

raiz.mainloop()