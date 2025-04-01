#Equação pricipal f(x) = cos(x) - x  
#Intervalo I = [0,1]
import math

#Definição da função principal
def f(x):
    return math.cos(x) - x

#Função do Método da Bisseção
def bissecao(a, b, tol=10**(-4), max_iter=25):
    #Verifica se há raiz dentro do intervalo
    if f(a) * f(b) >= 0:
        raise ValueError("A função não muda de sinal no intervalo dado.")
    
    iter_count = 0
    #Laço das iteraçãoes, irá até a quantidade maxima de iterações definida
    while (b - a) / 2 > tol and iter_count < max_iter:
        x = (a + b) / 2
        print(f"iteração = {iter_count:5d}   | a = {a:.6f}  | b = {b:.6f}  | x = {x:.6f}  | f(x) = {f(x):.6f}")
        
        #Vericação do sinal da função
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        iter_count += 1
    
    return (a + b) / 2

#Chamada da função do método da Bissseção
raiz_bissecao = bissecao(0, 1)
print("\nRaiz encontrada:", f"{raiz_bissecao:.6f}")