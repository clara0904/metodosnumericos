def f(x):
    return x ** 3 - 4 * x - 9


def df(x):
    return 3 * (x ** 2) - 4


def newton(x0, err, max_int):
    raiz = 0
    if abs(f(x0)) < err:
            raiz = x0
            print("Raiz: ", raiz)
            return raiz

    k = 1
    while k <= max_int:
        if(df(x0)) == 0:
            return None
       
        x1 = x0 - f(x0) / df(x0)
        print(f"iteração = {k}   | x0 = {x0:.6f}  | x1 = {x1:.6f}")

        if abs(f(x1)) < err or abs(x1 - x0) < 10**(-4) or k >= max_int:
            print("Raiz: ", x1)
            return x1
           
        x0 = x1
        k += 1

x0 = (2 + 3) / 2
newton(x0, 10**(-4), 25)