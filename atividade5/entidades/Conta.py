from entidades.Historico import Historico

class Conta:
    __slots__ = ['_numero_agencia', '_tipo_conta', '_saldo', '_limite', '_titular', '_historico']

    def __init__(self, numero_agencia, tipo_conta, titular, saldo=0, limite=0):
        self._numero_agencia = numero_agencia
        self._tipo_conta = tipo_conta
        self._saldo = saldo
        self._limite = limite
        self._titular = titular
        self._historico = Historico()  # Supõe-se que a classe Historico já esteja definida.

    def consultar_saldo(self):
        self._historico.registrar_transacao("Consulta de saldo.")
        return self._saldo

    def saca(self, valor):
        if self._saldo + self._limite < valor:
            self._historico.registrar_transacao("Tentativa de saque falhou.")
            return False
        self._saldo -= valor
        self._historico.registrar_transacao(f"Saque de {valor}. Saldo atual: {self._saldo}.")
        return True

    def deposita(self, valor):
        self._saldo += valor
        self._historico.registrar_transacao(f"Depósito de {valor}. Saldo atual: {self._saldo}.")
        return True

    def transfere_para(self, destino, valor):
        if self.saca(valor):
            destino.deposita(valor)
            self._historico.registrar_transacao(f"Transferência de {valor} para conta do titular {destino._titular}.")
            return True
        return False

    def obter_extrato(self):
        return self._historico.obter_transacoes()

    def alterar_titular(self, novo_titular):
        self._titular = novo_titular
        self._historico.registrar_transacao(f"Titular alterado para {novo_titular}.")
        return True

    def fechar_conta(self):
        if self._saldo > 0:
            self._historico.registrar_transacao("Conta não pode ser fechada, saldo maior que zero.")
            return False
        self._historico.registrar_transacao("Conta fechada com sucesso.")
        # Implementar transferência de saldo restante, se necessário.
        return True

