import datetime
import pytz

#Criando datetime com timezone 
d = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
print(d)