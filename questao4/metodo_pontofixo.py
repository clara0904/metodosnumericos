e = 2.71828
def f(x):
    return e**x-4*x

def g(x):
    return (e**x)/4  

def pontofixo(x0, erro, maxInter):
    if abs(f(x0)) < erro:
        return x0  

    k = 1
    while k <= maxInter:
        x1 = g(x0)
        print(f"Iteração {k}: x1 = {x1:.6f} | x0 = {x0:.6f} | |x1 - x0| = {abs(x1 - x0):.6f} | f(x1) = {f(x1):.6f}")

        if abs(f(x1)) < erro or abs(x1 - x0) < erro:
            print(f"Aproximação da raiz: {x1}")
            return x1  
        
        x0 = x1
        k += 1

    return x0  

x0 = (0 + 1) / 2
pontofixo(x0, 10**(-4), 25)
