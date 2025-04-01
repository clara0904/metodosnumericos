#Equação principal f(x) =e^x - 4x
#Equação phi(x) = (e^x)/4
#Intervalo I  = [0, 1]
e = 2.71828
def f(x):
    return e**x-4*x

#Definição da função phi
def g(x):
    return (e**x)/4  

#Função do metodo de Ponto Fixo
def pontofixo(x0, erro, maxInter):
    if abs(f(x0)) < erro:
        return x0  

    k = 1
    #Laço das iteraçãoes, irá até a quantidade maxima de iterações definida
    while k <= maxInter:
        x1 = g(x0)
        print(f"Iteração {k}: x1 = {x1:.6f} | x0 = {x0:.6f} | |x1 - x0| = {abs(x1 - x0):.6f} | f(x1) = {f(x1):.6f}")

        #Verifica a condição de parada do laço
        if abs(f(x1)) < erro or abs(x1 - x0) < erro:
            print(f"Aproximação da raiz: {x1}")
            return x1  
        
        x0 = x1
        k += 1

    return x0  

x0 = (0 + 1) / 2

#Chamada da função do método do Ponto Fixo
pontofixo(x0, 10**(-4), 25)
