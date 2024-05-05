from entidades.Cliente import Cliente
from entidades.Conta import Conta
from entidades.ContaCorrente import ContaCorrente
from entidades.ContaPoupanca import ContaPoupanca

# Criando instâncias de Cliente
joao = Cliente("João", "Silva", "11111-1")
maria = Cliente("Maria", "Salgado", "22222-222")
pedro = Cliente("Pedro", "Gomes", "33333-3")

# Criando instâncias de Conta
conta_joao = ContaCorrente("123-4", "Corrente", joao, 1000.00, 500.00, True)
conta_maria = ContaCorrente("123-5", "Corrente", maria, 7000.00, 4000.00, False)
conta_pedro = ContaPoupanca("456-7", "Poupança", pedro, 1500.00, 0, "2024-05-05")

# Testando funcionalidades da conta do João
print("Extrato inicial de João:")
transacoes_joao = conta_joao.obter_extrato()
for transacao in transacoes_joao:
    print(transacao)

conta_joao.saldo = 10000.00  # Alterando o saldo via property
print("Saldo após alteração:", conta_joao.saldo)

conta_joao.saca(500.00)
conta_joao.deposita(5.50)
resultado_transf = conta_joao.transfere_para(conta_maria, 2500.00)
print("Resultado da transferência:", "Sucesso" if resultado_transf else "Falha")

# Tentativa de usar cheque especial
print("Tentando usar cheque especial:")
resultado_cheque = conta_joao.utilizar_cheque_especial(200.00)
print("Cheque especial:", "Utilizado" if resultado_cheque else "Não utilizado ou desnecessário")

# Tentativa de fechar a conta do João
resultado_fechamento = conta_joao.fechar_conta()
print("Tentativa de fechar a conta de João:", "Conta fechada" if resultado_fechamento else "Falha ao fechar conta")

# Imprimindo o histórico de transações da conta do João
print("Histórico de transações de João:")
conta_joao._historico.imprime()

# Aplicando juros à conta do Pedro
print("Aplicando juros à conta de Pedro:")
taxa_juros = 0.5  # Supondo uma taxa de juros de 0.5%
conta_pedro.calcular_juros_mensal(taxa_juros)

# Imprimindo o extrato pós-aplicação de juros de Pedro
print("Extrato após aplicação de juros de Pedro:")
transacoes_pedro = conta_pedro.obter_extrato()
for transacao in transacoes_pedro:
    print(transacao)

# Imprimindo o histórico de transações da conta do Pedro
print("Histórico de transações de Pedro:")
conta_pedro._historico.imprime()
