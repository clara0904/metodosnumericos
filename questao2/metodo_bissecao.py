import math

def f(x):
    return math.cos(x) - x

def bissecao(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    print("Iteração |   a        |   b        |   c        |   f(c)      ")
    print("-------------------------------------------------------------")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        print(f"{iter_count:5d}   | {a:.6f}  | {b:.6f}  | {c:.6f}  | {f(c):.6f}")
        
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2

raiz_bissecao = bissecao(0, 1)
print("\nRaiz encontrada:", f"{raiz_bissecao:.6f}")