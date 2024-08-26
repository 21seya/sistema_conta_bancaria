import datetime

d = datetime.datetime.now()

#formato de data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

data_string = "20/07/2024 19:30"
d = datetime.datetime.strptime(data_string,"%d/%m/%Y %H:%M")
print(d)