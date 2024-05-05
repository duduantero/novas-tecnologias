class Conta:
    
    def __init__(self,numero,cliente,saldo,limite):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
    
    def extrato(self):
        return self._saldo
    
    def depositar(self,valor):
        self.saldo += valor   

    def sacar(self,valor):
        if(self.saldo<valor):
            return False
        else: 
            self.saldo-+ valor
            return True
    def trasfere_para(self,destino,valor):
        retirou = self.sacar()
        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            return True
            
    def fecha_conta(self):
        if(self._saldo == 0):
            return True