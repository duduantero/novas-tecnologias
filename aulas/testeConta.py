from banco.Conta import Conta
from banco.Cliente import Cliente



joao =  Cliente("João","Silva",1234-5)
contaJoao = Conta(1234,joao,1000.0,500.0)

contaJoao.saldo = 2000


print(contaJoao.extrato())
