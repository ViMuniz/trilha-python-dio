from datetime import date, datetime, time # da função datatime enviar os valores para date, datetime e time

#Framework date mostra apenas os dias
data = date(2025, 5, 1)
print(data)
print(date.today()) #Dia, mês e ano atual

#Framework datetime informa data e tempo
data_tempo = datetime(1999, 7, 7, 10, 27, 43)
print(data_tempo)

data_tempo0 = datetime(765, 3, 14)
print(data_tempo0)

print(datetime.today())

#Framework time informa o tempo apenas
tempo = time(17,32,9)
print(tempo)