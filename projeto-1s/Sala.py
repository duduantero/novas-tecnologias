class Sala:
    def __init__(self, nome):
        self.nome = nome
        self.reservas = []

    def __str__(self):
        return self.nome

    def adicionar_reserva(self, reserva):
        self.reservas.append(reserva)

    def remover_reserva(self, reserva):
        self.reservas.
        (reserva)

    def esta_disponivel(self, data):
        for reserva in self.reservas:
            if reserva.data == data:
                return False
        return True
