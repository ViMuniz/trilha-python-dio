# Fuso horarios
import pytz
from datetime import datetime, timedelta, timezone

# Direcionando o fuso horario de acordo com a localização do cliente
data = datetime.now(pytz.timezone("Europe/London"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data)
print(data2)

# Usando timezone base do python - É PIOR QUE O PYTZ
data_londres = datetime.now(timezone(timedelta(hours=1)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))
print(data_londres)
print(data_sao_paulo)