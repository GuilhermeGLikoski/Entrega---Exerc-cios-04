nota = float(input("Digite a nota do aluno (0 a 10): "))

while nota < 0 or nota > 10:
    print("Erro: A nota deve estar entre 0 e 10.")
    nota = float(input("Digite uma nota válida (0 a 10): "))

print(f"Nota {nota} registrada com sucesso!")
