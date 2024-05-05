from entidades.Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero_agencia, tipo_conta, titular, saldo, limite, cheque_especial):
        super().__init__(numero_agencia, tipo_conta, titular, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if not self.cheque_especial:
            self._historico.registrar_transacao("Tentativa de usar cheque especial falhou: serviço não habilitado.")
            return False
        elif self.saldo + self._limite >= valor:
            self._historico.registrar_transacao("Uso de cheque especial desnecessário: saldo suficiente.")
            return False
        else:
            self.saldo -= valor
            self._historico.registrar_transacao(f"Cheque especial utilizado para cobrir: {valor}. Saldo atual: {self.saldo}.")
            return True
