menu = """
[c] Criar conta
[u] Criar usuário
[l] Login
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
usuarios = []
contas = []
saldo = 0
limite = 500
extrato = ""
numero_saques: int = 0
limite_saques: int = 3

while True:

    opcao = input(menu)

    if opcao == "u":
        nome = input("Insira o seu nome: ")
        cpf = input("Insira o seu CPF: ")

        usuario = {
            "Nome": nome,
            "CPF": cpf
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    
    elif opcao == "c":
        if len(usuarios) == 0:
            print("Operação falhou: Não há usuarios cadastrados no sistema")
            continue

        cpf_usuario = input("Digite o seu CPF para verificar a conta: ")

        verificar_usuario = None
        for usuario in usuarios:
            if usuario["CPF"] == cpf_usuario:
                verificar_usuario = usuario
                break
        if verificar_usuario:

            numero_conta = input("Digite o número da sua conta: ")
            tipo_conta = input("Digite o tipo da sua conta: ")
            senha = input("Digite a sua senha: ")

            conta = {
                "numero": numero_conta,
                "tipo": tipo_conta,
                "senha": senha
            }
            
            contas.append(conta)
            print("Conta criada com sucesso!")


    elif opcao == "l":
        numero_login = input("Digite o número da sua conta: ")
        login_senha = input("Digite a sua senha: ")

        verificar_login = None

        for conta in contas:
            if conta["numero"] == numero_login:
                verificar_login = conta
                break

        if verificar_login:
            senha_encontrada = verificar_login["senha"]

            if senha_encontrada == verificar_login['senha']:
                usuario_logado = verificar_login["usuario"]
                print("Login realizado com sucesso!")

            else:
                print("Operação falhou: Credencias incorretas")
        else:
            print("Usuário não encotrado")

 
    elif opcao == "d":
        valor = float(input("Insira o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += "Depósito efetuado no valor de R$: {valor:.2f}"
            print ("Depósito efetuado com sucesso!")
        else: 
            print("Operação falho: Valor inválido para depósito")


    elif opcao == "s":
        valor = float(input("Insira o valor que deseja sacar: "))

        sem_saldo = valor > saldo

        sem_limite = valor > limite

        sem_saque = numero_saques >= limite_saques

        if sem_saldo:
            print("Operalçao falhou: Sem saldo disponível")
        
        elif sem_limite:
            print("Operação falhou: Sem limite diponivel")
        
        elif sem_saque: 
            print("Operação falhou: O usuário excedeu o limite de saque")
        
        elif valor > 0:
            saldo -= valor
            extrato += "Saque efetuado no valor de R$: {valor:.2f}"
            numero_saques += 1
            print("Saque efetuado com sucesso")

        else:
            print("Operação falho: Valor inválido para saque")

    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        break

else:
    print("Operação inválida: Por favor selecione novamente a operação desejada")