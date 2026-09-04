# Informando a usuário a utilidade do programa
print("\tCriação de usuários e suas respectivas informações")
# Listas vazias para serem adicionadas informações
users = []
idades = []

def criar_usuario(nome, idade, cidade):
    ''' Criação de dicionário das informações de um usuário'''
    dicio = {}
    dicio['nome'] = nome
    dicio['idade'] = idade
    dicio['cidade'] = cidade
    return dicio
# Solicitando ao usuário informações das pessoas a serem cadastradas
while len(users) != 5:
    print("\nInforme para criar um usuário(Limite: 5): ")
    nome_informado = input("Qual o nome do usuário? ")
    idade_informado = int(input(
        "Qual a idade do usuário?(Apenas números inteiros) "))
    cidade_informado = input("Qual a cidade do usuário? ")
    user1 = criar_usuario(nome_informado, idade_informado, cidade_informado)
    users.append(user1)
# Criação de lista com todas idades de usuários na mesma ordem
for ordem in range (0,5):
    idades.append(users[ordem]['idade'])
# Informando todos usuários
print("\n\tTodos os usuários: ")
for user in users:
    print("\n" + str(user))
# Informando os usuário mais velhos
print("\n\tUsuários mais velhos: ")
for user in users:
    if user['idade'] == max(idades):
        print(user['nome'] + " é um dos usuários mais velhos.")
# Informando os usuários mais novos
print("\n\tUsuários mais novos: ")
for user in users:
    if user['idade'] == min(idades):
        print(user['nome'] + " é um dos usuários mais jovens.")
# Informando a média das idades dos usuários
print("\n\tMédia das idades: ")
print("A média da idade dos usuários é: " + str(sum(idades)/len(idades)))