while True:
    print("\n--- Calculadora ---")
    print("1: soma")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")
    print("0: sair")
    
    opcao = input("Escolha uma opção: ")
    

    if opcao == '0':
        print("Encerrando a calculadora...")
        break
        
  
    elif opcao in ['1', '2', '3', '4']:

        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))
        

        if opcao == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcao == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcao == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcao == '4':

            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
    else:

        print("Opção inválida! Por favor, digite um número de 0 a 4.")
