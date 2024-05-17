from SistemaReservas import SistemaReservas


def main():
    sistema = SistemaReservas()

    # Adicionar salas
    sistema.adicionar_sala("Sala 1")
    sistema.adicionar_sala("Sala 2")

    # Visualizar salas
    print("Salas disponíveis:")
    sistema.visualizar_salas()

    # Verificar disponibilidade
    print("\nVerificando disponibilidade:")
    sistema.visualizar_disponibilidade("Sala 1", "2024-06-01")

    # Fazer uma reserva
    print("\nFazendo uma reserva:")
    sistema.fazer_reserva("Sala 1", "Alice", "2024-06-01")

    # Verificar disponibilidade novamente
    print("\nVerificando disponibilidade novamente:")
    sistema.visualizar_disponibilidade("Sala 1", "2024-06-01")

    # Cancelar uma reserva
    print("\nCancelando uma reserva:")
    sistema.cancelar_reserva("Sala 1", "Alice", "2024-06-01")

    # Verificar disponibilidade novamente
    print("\nVerificando disponibilidade novamente:")
    sistema.visualizar_disponibilidade("Sala 1", "2024-06-01")


if __name__ == "__main__":
    main()
