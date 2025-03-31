e = 2.71828
def f(x):
    return e**x-4*x

def g(x):
    return (e**x)/4  

def pontofixo(x0, erro1, erro2, maxInter):
    if abs(f(x0)) < erro1:
        return x0  

    k = 1
    while k <= maxInter:
        x1 = g(x0)
        print(f"Iteração {k}: x1={x1}, x0={x0}, |x1 - x0|={abs(x1 - x0)}, f(x1)={f(x1)}")

        if abs(f(x1)) < erro1 or abs(x1 - x0) < erro2:
            print(f"Aproximação da raiz: {x1}")
            return x1  
        
        x0 = x1
        k += 1

    return x0  

x0 = (0 + 1) / 2
pontofixo(x0, 10**(-4), 10**(-4), 15)
