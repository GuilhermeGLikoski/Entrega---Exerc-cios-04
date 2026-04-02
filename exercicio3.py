soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (-1 para calcular a média e sair): "))
    
    if numero == -1:
        break 
        
    soma += numero
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número foi digitado para calcular a média.")
