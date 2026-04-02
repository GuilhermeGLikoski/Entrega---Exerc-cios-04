while True:
    expressao = input("\nDigite a expressão (ex: 2 + 5) ou 'sair' para encerrar: ")
    
    if expressao.lower() == 'sair':
        print("Encerrando a calculadora...")
        break
        

    partes = expressao.split()
    

    if len(partes) != 3:
        print("Formato inválido! Certifique-se de usar espaços entre os números e o operador (exemplo: 10 - 4).")
        continue
        
    try:

        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])
        

        if operador == '+':
            print(f"Resultado: {num1 + num2}")
        elif operador == '-':
            print(f"Resultado: {num1 - num2}")
        elif operador == '*':
            print(f"Resultado: {num1 * num2}")
        elif operador == '/':
            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                print(f"Resultado: {num1 / num2}")
        else:
            print("Operador inválido! Use apenas +, -, * ou /.")
            
    except ValueError:

        print("Erro: Certifique-se de digitar números válidos na sua expressão.")
