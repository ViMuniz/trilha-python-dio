from datetime import timedelta, datetime, date, time

tipo_carro = 'M' #P, M, G
tempo_pequeno = 30
tempo_medio = 8956
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else: 
    data_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")


#Manipulção apenas de data
print(date.today() - timedelta(days=5))

#Manipulação de data e hora
resultado = datetime(2000,4,1, 10,20,30) - timedelta(hours=10)
print(resultado.time())

print(datetime.now().date())