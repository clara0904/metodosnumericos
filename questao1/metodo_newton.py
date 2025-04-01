#Equação principal f(x) = x³-4x - 9
#Intevalo I = [2,3]

#Definição da função principal
def f(x):
    return x ** 3 - 4 * x - 9

#Derivada da função
def df(x):
    return 3 * (x ** 2) - 4

#Função do Método de Newton
def newton(x0, err, max_int):
    raiz = 0
#Verificção se o primeiro valor de x já é a raiz
    if abs(f(x0)) < err:
            raiz = x0
            print("Raiz: ", raiz)
            return raiz

    k = 1

#Laço das iteraçãoes, irá até a quantidade maxima de iterações definida
    while k <= max_int:
        if(df(x0)) == 0:
            return None
        
        #Essa variavel guardará o calculo do método de newton
        x1 = x0 - f(x0) / df(x0)
        print(f"iteração = {k}   | x0 = {x0:.6f}  | x1 = {x1:.6f}")

        #Faz as verificações das condições de parada
        if abs(f(x1)) < err or abs(x1 - x0) < 10**(-4) or k >= max_int:
            print("Raiz: ", x1)
            return x1
           
        x0 = x1
        k += 1

x0 = (2 + 3) / 2

#Chamada da função do método de newton
newton(x0, 10**(-4), 25)