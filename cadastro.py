loop = 0

menu = '''
===== Menu =======================

[mostrar] mostrar todos os cadastros
[cadastrar] cadastrar novo cliente
[pesquisar] pesquisar cliente

==================================

'''
lista_dados = []
id = 0


def mostrar():
    for itens in lista_dados:
        print(itens)


def cadastrar():
    global id
    global lista_dados
    nome = input('digite seu nome:')
    cpf = int(input('digite seu cpf:'))
    data_de_nascimento = input('digite sua data de nascimento:')
    endereco = input('digite seu endereço:')

    lista_dados.append({
        'id': id,
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_de_nascimento,
        'endereço': endereco
    })
    id = id + 1
    print('Usuário cadastrado com sucesso')


def pesquisar(busca):
    try:
        print(lista_dados[busca])
    except:
        print('id não encontrado')


while loop == 0:
    print(menu)
    escolha = input('digite a opção: ')
    if escolha == 'mostrar':
        mostrar()

    elif escolha == 'cadastrar':
        cadastrar()

    elif escolha == 'pesquisar':
        buscador = int(input('digite o id do cliente:'))
