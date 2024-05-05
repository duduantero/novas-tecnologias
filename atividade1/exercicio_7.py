total_segundos = int(input("Digite a quantidade de segundos:"))

SEGUNDOS_POR_MINUTO = 60
SEGUNDOS_POR_HORA = 3600
SEGUNDOS_POR_DIA = 86400

dias = total_segundos // SEGUNDOS_POR_DIA
segundos_restantes = total_segundos % SEGUNDOS_POR_DIA

horas = segundos_restantes // SEGUNDOS_POR_HORA
segundos_restantes %= SEGUNDOS_POR_HORA

minutos = segundos_restantes // SEGUNDOS_POR_MINUTO
segundos_restantes %= SEGUNDOS_POR_MINUTO

print(f"{total_segundos} segundos equivalem a:")
print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
