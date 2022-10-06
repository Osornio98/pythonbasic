

infija = []
prefija = []
resultado = []

while(1):

    infijax = input ("Ingresa la expresion: ")
    infija = list(infijax)

    for i in infija:
        if str.isdigit(i):
            prefija.append(i)
        else:
            prefija.insert(0,i)

    for a in prefija[::-1]:
        if str.isdigit(a):
            resultado.append(int(a))
        else:
            va1 = resultado.pop()
            va2 = resultado.pop()

            if a == '+':
                resultado.append(va1 + va2)
            elif a == '-':
                resultado.append(va1 - va2)
            elif a == '*':
                resultado.append(va1 * va2)
            elif a == '/':
                resultado.append(va1 / va2)
    
    
    print(infija)
    print(prefija)
    print(resultado)
    prefija.clear()
    resultado.clear()