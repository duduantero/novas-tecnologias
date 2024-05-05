from banco.Conta import Conta

class ContaPoupanca(Conta):

    _total_poupanca=0

    def __init__(self, numero, cliente, tipo_conta, saldo, limite, aniversario_conta):
        super().__init__(numero, cliente, tipo_conta, saldo, limite)
        self._aniversario_conta =aniversario_conta
        ContaPoupanca._total_poupanca +=1

    @staticmethod
    def get_total_contas():
        return ContaPoupanca._total_poupanca
