from datetime import datetime

data_hora_atual = datetime.now()

data_hora_str = '2024-07-01 19:35'

mascara_ptbr = '%d/%m/%Y'

mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str,mascara_en))