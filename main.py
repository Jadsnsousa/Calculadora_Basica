from funcoes import functions as FC
from time import sleep
escolhas = ['1', '2', '3', '4', '5', '0', '9']



print(f'{"Calculadora em Python":^30}')

print(f'{"Digite os valores":^30}\n')

A = float(input(f'A = '))
B = float(input(f'B = '))

print(type(A))

while True:
    print(f'\n{"Menu:":^30}'\
        f'\n{"[1] Adição":^30}'\
        f'\n{"[2] Subtração":^30}'\
        f'\n{"[3] Multiplicação":^30}'\
        f'\n{"[4] Divisão":^30}'\
        f'\n{"[5] Potencia":^30}'\
        f'\n{"[0] Novos Numeros":^30}'\
        f'\n{"[9] Sair":^30}')
    
    esc: str = (input(f'\n{"Escolha: ":^15}'))[0]
    
    while esc not in escolhas:
        esc: str = (input(f'Opção invalida. Digite novamente: '))
    
    if '1' in esc:
        result = FC.Adicao(A, B)
        print(f'A soma de {A} + {B} é igual a {result}')
    
    elif '2' in esc:
        result = FC.Subtracao(A, B)
        print(f'A subtracao de {A} - {B} é igual a {result}')

    elif '3' in esc:
        result = FC.Multiplicacao(A, B)
        print(f'A multiplicação de {A} * {B} é igual a {result}')

    elif '4' in esc:
        result = FC.Divisao(A, B)
        print(f'A divisão de {A} por {B} é igual a {result}')

    elif '5' in esc:
        result = FC.Potencia(A, B)
        print(f'A soma de {A} elevado a {B} é igual a {result}')

    elif '6' in esc:
        result = FC.Porcentagem(A, B)
        print(f'{B:.1%} de R${A:.2f} é igual a R${result:.1%}')

    elif '0' in esc:
        A = float(input('A = '))
        B = float(input('B = '))

    elif '9' in esc:
        break

    sleep(2)