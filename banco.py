class BancoSimulado:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saque = 500.0
        self.max_saques = 3

    def depositar(self, valor):
        if valor >= 100.0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Depósito mínimo permitido é de R$100,00.")

    def sacar(self, valor):
        if self.saques_realizados >= self.max_saques:
            print("Limite de saques diários atingido.")
            return
        if valor > self.limite_saque:
            print(f"Limite de saque por transação é de R${self.limite_saque:.2f}.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        self.saldo -= valor
        self.saques_realizados += 1
        self.extrato.append(f"Saque: -R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def ver_extrato(self):
        print("\nExtrato:")
        for transacao in self.extrato:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


def menu_banco():
    banco = BancoSimulado()
    
    while True:
        print("\n--- Sistema Bancário Simulado ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == '1':
            valor = float(input("Digite o valor para depositar: R$"))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para sacar: R$"))
            banco.sacar(valor)
        elif opcao == '3':
            banco.ver_extrato()
        elif opcao == '4':
            print("Saindo do sistema bancário. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu_banco()
