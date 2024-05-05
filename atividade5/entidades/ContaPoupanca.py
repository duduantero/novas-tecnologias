from entidades.Conta import Conta

class ContaPoupanca(Conta):
    _total_poupanca = 0

    def __init__(self, numero_agencia, tipo_conta, titular, saldo, limite, aniversario_conta):
        super().__init__(numero_agencia, tipo_conta, titular, saldo, limite)
        self._aniversario_conta = aniversario_conta
        ContaPoupanca._total_poupanca += 1

    @staticmethod
    def get_total_contas():
        return ContaPoupanca._total_poupanca

    def calcular_juros_mensal(self, taxa_juros):
        if self._saldo > 0:  # Aplica juros apenas se houver saldo positivo.
            juros = self._saldo * (taxa_juros / 100)
            self._saldo += juros
            self._historico.registrar_transacao(f"Juros mensais aplicados: {juros}. Saldo atual: {self._saldo}.")
            return True
        return False
