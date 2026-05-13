def cadastrar_aluno():
    nome = input("digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("digite a nota 2: "))

    aluno = {
    "nome": nome,
    "nota1": nota1,
    "nota2": nota2
    }
    
    return aluno



