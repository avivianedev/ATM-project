'''
ATM project
Faça um programa de caixa eletrônico com as opções: 
(1) consulta saldo, 
(2) saque, 
(3) depósito e 
(4) sair. 
O saldo inicial é sempre de R$ 0,00. 
A cada saque ou depósito atualize o valor do saldo e apresente-o na tela.
'''

class Conta:
    
    def __init__(self, nome,saldo = 0 ):        
        self.saldo = saldo
        self.nome = nome

    def consulta_saldo(self):
        print(f'Olá {self.nome} seu saldo é: {self.saldo:.2f}') 

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def deposito(self,valor):
        self.saldo += valor



