# Funções da calculadora

# Funções padrão

def Adicao(A, B):
    X: float = A + B
    return float(X)

def Subtracao(A, B):
    X: float = A - B
    return float(X)

def Multiplicacao(A, B):
    X: float = A * B
    return float(X)

def Divisao(A, B):
    X: float = A / B
    return X

def Potencia(base, expoente):
    if base != 0 and expoente == 0:
        return 1
    elif expoente == 1:
        return base
    elif base == 1:
        return 1
    else:
        X: float = base ** expoente
        return float(X)

def Porcentagem(A, desconto):
    X: float = (A * desconto) / 100
    return float(X)


if __name__ == '__main__':
    print(Adicao(200, 10))
    resultado = Adicao(20, 10)
    print(type(resultado))