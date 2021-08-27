def PuntoFijo(f, p, tolerancia):
    error = 1
    iteraciones = 0
    
    while error > tolerancia:
        p1 = f(p)
        error = abs(p1 - p)
        p = p1
        iteraciones += 1
        print(f'p{iteraciones} = {p: 0.5f}')
    print(f'Raíz: {p}\nIteraciones: {iteraciones}')

def f(x):
    return x**3 - 2*x + 5

PuntoFijo(f, 0, 10e-5)