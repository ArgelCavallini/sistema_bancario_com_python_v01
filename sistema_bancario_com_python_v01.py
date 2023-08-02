class ContaBancaria:
    def __init__(self):
        self.saldo         = 0
        self.extrato       = []
        self.limite_diario = 500
        self.saque_diario  = 0
        self.LIMITE_SAQUES = 3

    def depositarDinheiro(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +{valor}")

            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Digite um valor positivo maior que zero.")

    def sacarDinheiro(self, valor):
        if self.saque_diario >= self.LIMITE_SAQUES:
            print("Você atingiu o limite diário de saques (3 saques).")
        elif valor > 0 and valor <= self.limite_diario:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append(f"Saque: -{valor}")
                self.saque_diario += 1

                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Valor de saque inválido. Digite um valor positivo menor ou igual a R$ 500.")

    def verExtrato(self):
        print("\n================== Extrato ==================")

        if self.extrato:
            for item in self.extrato:
                print(item)
        else:
            print("\nNão foram realizada movimentações.")

        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("\n=============================================")


def iniciarTerminalBancario():
    conta = ContaBancaria()

    while True:
        print("\nEscolha a operação:")
        print("d - Depositar")
        print("s - Sacar")
        print("e - Extrato")
        print("q - Sair")

        menu = input("Digite o número da operação desejada: ")

        if menu == "d":
            valor = float(input("Digite o valor do depósito: "))
            conta.depositarDinheiro(valor)
        elif menu == "s":
            valor = float(input("Digite o valor do saque: "))
            conta.sacarDinheiro(valor)
        elif menu == "e":
            conta.verExtrato()
        elif menu == "q":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    iniciarTerminalBancario()