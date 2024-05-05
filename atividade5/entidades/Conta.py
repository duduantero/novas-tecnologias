from entidades.Historico import Historico


class Conta:

    __slots__=['_numero', '_titular','_tipo_conta', '_saldo','_limite', '_historico']

    _total_contas = 0


    def __init__(self, numero, cliente, tipo_conta, saldo, limite):
       self._numero = numero
       self._titular = cliente
       self._tipo_conta=tipo_conta
       self._saldo = saldo
       self._limite = limite
       self._historico = Historico()
       Conta._total_contas +=1

    @property
    def saldo(self):
        self._historico._transacoes.append(f"Consultou o saldo de {self._saldo}.")
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._historico._transacoes.append(f"Alterou o saldo de {self._saldo} para {valor}.")
        self._saldo = valor

    def get_numero(self):
        self._historico._transacoes.append(f"Consultou o número da conta {self._numero}.")
        return self._numero

    def deposita(self,valor):
        self._historico._transacoes.append(f"Depositou o valor de {valor}.")
        self.saldo = self.saldo + valor

    def saca(self,valor):
        if(self.saldo<valor):
            return False
        else:
            self.saldo = self.saldo - valor
            self._historico._transacoes.append(f"Retirou o valor {valor}, o saldo agora é {self._saldo}.")
            return True
    

    def extrato(self):
        self._historico._transacoes.append("Imprimiu extrato.")
        return f"numero: {self.get_numero()} \n saldo: {self.saldo}"

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou==False):
            return False
        else:
            destino.deposita(valor)
            self._historico._transacoes.append(f"Transferiu o valor {valor} para a conta {destino._titular._nome}.")
            return True
        
    def fecha_conta(self):
        if(self.saldo==0):
            self._historico._transacoes.append("Fechou a Conta.")
            return True
        else:
            return False

    @staticmethod
    def get_total_contas():
        return Conta._total_contas
