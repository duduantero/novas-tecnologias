from Sala import Sala
from Reserva import Reserva

class SistemaReservas:
    def __init__(self):
        self.salas = {}

    def adicionar_sala(self, nome):
        if nome not in self.salas:
            self.salas[nome] = Sala(nome)
        else:
            print(f"Sala {nome} já existe.")

    def visualizar_salas(self):
        for sala in self.salas.values():
            print(sala)

    def visualizar_disponibilidade(self, nome_sala, data):
        if nome_sala in self.salas:
            sala = self.salas[nome_sala]
            if sala.esta_disponivel(data):
                print(f"A sala {nome_sala} está disponível na data {data}.")
            else:
                print(f"A sala {nome_sala} não está disponível na data {data}.")
        else:
            print(f"Sala {nome_sala} não encontrada.")

    def fazer_reserva(self, nome_sala, usuario, data):
        if nome_sala in self.salas:
            sala = self.salas[nome_sala]
            if sala.esta_disponivel(data):
                reserva = Reserva(sala, usuario, data)
                sala.adicionar_reserva(reserva)
                print("Reserva realizada com sucesso!")
            else:
                print(f"A sala {nome_sala} não está disponível na data {data}.")
        else:
            print(f"Sala {nome_sala} não encontrada.")

    def cancelar_reserva(self, nome_sala, usuario, data):
        if nome_sala in self.salas:
            sala = self.salas[nome_sala]
            for reserva in sala.reservas:
                if reserva.usuario == usuario and reserva.data == data:
                    sala.remover_reserva(reserva)
                    print("Reserva cancelada com sucesso!")
                    return
            print("Reserva não encontrada.")
        else:
            print(f"Sala {nome_sala} não encontrada.")
