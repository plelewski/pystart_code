
with open('transakcje.txt', encoding='utf8', mode='r') as file_to_read:
    with open('przychody.txt', encoding='utf8', mode='w') as file_to_write:
        for line in file_to_read:
            v_date, v_desc, v_value = line.split(';')
            if int(v_value) > 0:
                file_to_write.write(f'{v_date};{v_desc};{v_value}')

v_sum = 0
with open('przychody.txt', encoding='utf8', mode='r') as file:
    for line in file:
        _, _, v_value = line.split(';')
        v_sum += int(v_value)

print(f'Suma przychodów to: {v_sum}')
