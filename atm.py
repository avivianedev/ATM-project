from app import Conta

def Atm(): 
    nome = input('Olá! Como deseja se chamado? ').strip()  
    usuario = Conta(nome) 
    print()   
    while True:
        print(f'Olá {usuario.nome}')
        print()
        print("""O que voce deseja fazer hoje? 
(1) Consultar saldo
(2) Saque
(3) Deposito
(4) Sair
    """)
        print()
        options = int(input('Sua opcao: '))
        if options == 1: usuario.consulta_saldo()
        if options == 2: 
            valor = int(input('Qual o valor que deseja sacar?  '))
            usuario.saque(valor)
        if options == 3:
            valor = int(input('Qual o valor deseja depositar? '))
            usuario.deposito(valor)
        if options == 4:
            print('Tchau!...')
            break


Atm()
