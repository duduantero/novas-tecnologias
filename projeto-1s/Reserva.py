class Reserva:
    def __init__(self, sala, usuario, data):
        self.sala = sala
        self.usuario = usuario
        self.data = data

    def __str__(self):
        return f"Reserva feita por {self.usuario} na sala {self.sala} para a data {self.data}"
