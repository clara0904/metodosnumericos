import math

def f(x):
    return math.cos(x) - x

def bissecao(a, b, tol=10**(-4), max_iter=25):
    if f(a) * f(b) >= 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        x = (a + b) / 2
        print(f"iteração = {iter_count:5d}   | a = {a:.6f}  | b = {b:.6f}  | x = {x:.6f}  | f(x) = {f(x):.6f}")
        
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iter_count += 1
    
    return (a + b) / 2

raiz_bissecao = bissecao(0, 1)
print("\nRaiz encontrada:", f"{raiz_bissecao:.6f}")