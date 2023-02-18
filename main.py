# código
from Banco import Operacoes

loop = 0

while loop == 0:
    Operacoes.menu()
    menu = int(input('O que deseja fazer?'))

    if menu == 1:
        valor = float(input('digite o valor que deseja adicionar: '))
        Operacoes.depositar(valor)
        continue

    elif menu == 2:
        valor = float(input('digite o valor que deseja retirar: '))
        Operacoes.sacar(valor)
        continue

    elif menu == 3:
        Operacoes.extrato()

    elif menu == 4:
        loop = 1
