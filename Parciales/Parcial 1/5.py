import math

def NewtonModificado(f, df, ddf, x, tolerancia):
    error = 1
    iteraciones = 0
    while error > tolerancia:
        fx = f(x)
        dx = df(x)
        x1 = x - (fx*dx)/(dx*dx - fx*ddf(x))
        error = abs(x1 - x)
        x = x1
        iteraciones += 1
        print(f'x{iteraciones}: {error}')
    print(f"Resultado = {x:.15f}\nIteraciones: {iteraciones}")
    
if __name__ == '__main__':
    f = lambda x: math.e**x - x - 1 
    df = lambda x: math.e**x - 1 
    ddf = lambda x: math.e**x
    NewtonModificado(f, df, ddf, 1, 1e-5)