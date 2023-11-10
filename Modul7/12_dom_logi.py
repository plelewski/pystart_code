from datetime import datetime

v_logs = {}

with open('logi2.txt', encoding='utf8', mode='r') as file:
    for line in file:
        v_datetime, v_username, v_operation = line.strip().split(';')

        if v_operation == 'login' and (v_logs.get(v_username) is None or v_logs[v_username][1] > 0):
            v_logs[v_username] = [v_datetime, 0]
        else:
            v_diff = datetime.strptime(v_datetime,'%Y-%m-%d %H:%M:%S') - datetime.strptime(v_logs[v_username][0], '%Y-%m-%d %H:%M:%S')
            v_logs[v_username] = ['', v_logs[v_username][1] + v_diff.total_seconds()]

for name, num_of_sec in v_logs.items():
    print(f'{name} przepracował {float(num_of_sec[1])/60:.2f} minut')
