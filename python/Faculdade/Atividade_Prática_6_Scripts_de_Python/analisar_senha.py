''' O código tá quebrado ainda.
A ideia era criar um validador de senha, acho que dá para entender...
tem que consertar a parte dos números, pelo visto o maisculo e minusculo não
está seguindo boas práticas e é isso'''

def validar_senha(senha):
    caracter = len(senha) >= 8
    maiscula = senha.lower() != senha
    minuscula = senha.upper() != senha
    numeros = str((0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9)) in senha

    if caracter and maiscula and minuscula and numeros:
        print("Sua senha é válida!")
    else:
        print("Sua senha é inválida!")
    
    if caracter:
        print("Critério, pelo menos 8 Caractéres: Atendido.")
    else:
        print("Critério, pelo menos 8 Caractéres: Não atendido.")

    if maiscula:
        print("Critério, ter letra maiúscula: Atendido.")
    else:
        print("Critério, ter letra maiúscula: Não atendido.")

    if minuscula:
        print("Critério, ter letra minúscula: Atendido.")
    else:
        print("Critério, ter letra minúscula: Não atendido.")

    if numeros:
        print("Critério, ter pelo menos 1 número, Atendido.")
    else:
        print("Critério, ter pelo menos 1 número, Não atendido. ")

senha1 = input("Digite a senha para ser validada: ")
validar_senha(senha1)