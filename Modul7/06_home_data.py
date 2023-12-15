from datetime import datetime

today = datetime.today()
print(today.strftime('%d/%m/%y %H:%M:%S'))
print(today.strftime('%d-%m-%Y %H:%M:%S'))
