import datetime

class Historico:

    def __init__(self):
        self._data_da_abertura = datetime.datetime.now()
        self._transacoes = []

    def imprime(self):
        print(f"A data de abertura: {self._data_da_abertura}")
        print("Transações:")
        for t in self._transacoes:
            print("-", t)
