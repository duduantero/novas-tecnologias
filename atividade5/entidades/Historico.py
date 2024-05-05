import datetime

class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.datetime.now()
        self.transacoes = []

    def registrar_transacao(self, descricao):
        data_hora_atual = datetime.datetime.now()
        self.transacoes.append(f"{data_hora_atual} - {descricao}")

    def obter_transacoes(self):
        return list(self.transacoes)

    def imprime(self):
        print(f"A data de abertura: {self.data_da_abertura}")
        print("Transações:")
        for transacao in self.transacoes:
            print("-", transacao)
