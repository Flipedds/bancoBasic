saldo = 0
saques_por_dia = 3
VALOR_MAXIMO_OPERACAO = 500
lista_saques = []


class Operacoes:
    def menu():
        print("Opções:")
        print('1 - Depositar')
        print('2 - Sacar ')
        print('3- Extrato ')
        print('4 - Sair')

    def depositar(valor_deposito):
        global saldo
        saldo += valor_deposito
        print(f'O valor de R$ {valor_deposito:.2f} foi adicionado à sua conta')

    def sacar(valor_saque):
        global saques_por_dia
        global VALOR_MAXIMO_OPERACAO
        global saldo

        if valor_saque > VALOR_MAXIMO_OPERACAO or saques_por_dia == 0:
            print('Não será possivel continuar a operação limites ultrapassados')

        elif valor_saque > saldo:
            print('Você não tem saldo suficiente')

        else:
            saldo -= valor_saque
            saques_por_dia = saques_por_dia - 1
            lista_saques.append(valor_saque)
            print(f'O valor de R$ {valor_saque:.2f} foi retirado da sua conta')

    def extrato():
        global saldo
        global lista_saques

        print('Extrato')
        print(f'Saldo: R$ {saldo:.2f}')
        print('Histórico de Saldos:')
        for valores in lista_saques:
            print(f'Saque de: {valores:.2f}')
