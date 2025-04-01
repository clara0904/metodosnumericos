import math

def f(x):
    return math.log(x) + x**2 - 3

def PosicaoFalsa(a, b, erro, iterMax):
    Fa = f(a)
    Fb = f(b)

    if (Fa * Fb) > 0:
        print("Erro: função não muda de sinal entre a e b")
        return None

    itervX = abs(b - a)

    if abs(Fa) < erro:
        return a

    if abs(Fb) < erro:
        return b

    k = 0
    raiz = None

    while k < iterMax:
        x = (a * Fb - b * Fa) / (Fb - Fa) 
        Fx = f(x)
        print(f"Iteração {k}: a = {a:.6f} | Fa = {Fa:.6f} | b = {b:.6f} | Fb = {Fb:.6f} | x = {x:.6f} | Fx = {f(x):.6f}")

        if abs(Fx) < erro or itervX <= erro:  
            return x 

        if Fa * Fx > 0:
            a = x
            Fa = Fx
        else:
            b = x
            Fb = Fx

        itervX = abs(b - a)
        k += 1

    return x

raiz = PosicaoFalsa(1, 2, 10**(-4), 25)
if raiz is not None:
    print(f"A raiz aproximada é: {raiz}")