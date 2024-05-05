from atividade5.entidades.Conta import Conta
from atividade5.entidades.Cliente import Cliente

joao = Cliente("João", "Silva", "11111-1")
maria = Cliente("Maria", "Salgado", "22222-222")
conta_joao = Conta("123-4", joao,"Corrente", 1000.00, 500.00)
conta_maria = Conta("123-5", maria,"Corrente", 7000.00, 4000.00)

conta_joao.extrato()
conta_joao.saldo = 10000.00
print(conta_joao.saldo)
conta_joao.saca(500.00)
conta_joao.deposita(5.50)
conta_joao.transfere_para(conta_maria, 2500.00)
conta_joao.fecha_conta()

conta_joao._historico.imprime()

