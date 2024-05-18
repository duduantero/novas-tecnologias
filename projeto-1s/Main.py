from SistemaReservas import SistemaReservas


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar sala")
    print("2. Visualizar salas")
    print("3. Verificar disponibilidade")
    print("4. Fazer uma reserva")
    print("5. Cancelar uma reserva")
    print("6. Sair")


def main():
    sistema = SistemaReservas()

    # Adicionar algumas salas iniciais
    sistema.adicionar_sala("R 01 A")
    sistema.adicionar_sala("R 01 B")
    sistema.adicionar_sala("M109")
    sistema.adicionar_sala("M110")

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome_sala = input("Informe o nome da sala: ")
            sistema.adicionar_sala(nome_sala)
        elif escolha == '2':
            print("Salas disponíveis:")
            sistema.visualizar_salas()
        elif escolha == '3':
            nome_sala = input("Informe a sala: ")
            data = input("Informe a data (YYYY-MM-DD): ")
            sistema.visualizar_disponibilidade(nome_sala, data)
        elif escolha == '4':
            nome_sala = input("Informe a sala: ")
            usuario = input("Informe o nome do usuário: ")
            data = input("Informe a data (YYYY-MM-DD): ")
            sistema.fazer_reserva(nome_sala, usuario, data)
        elif escolha == '5':
            nome_sala = input("Informe a sala: ")
            usuario = input("Informe o nome do usuário: ")
            data = input("Informe a data (YYYY-MM-DD): ")
            sistema.cancelar_reserva(nome_sala, usuario, data)
        elif escolha == '6':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
