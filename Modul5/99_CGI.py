
ft_processes = ['batchDispatcher-CCR-batchDispatcher-3.tra',
                'batchDispatcher-CCR-batchDispatcher-4.tra',
                'TestDataUtility-TDU-testDataUtility-2.tra',
                'blabla-3.tra']

list_of_cur_processes = []


with open('/Users/przemek/check_processes.txt') as file:
    for line in file:
        if '.tra' in line.strip()[-5:-1]:
            dataline = line.strip()
            list_of_cur_processes.append(dataline[dataline.rfind("/")+1:-1])

with open('/Users/przemek/list_of_processes.txt', mode='w') as file:
    for item in list_of_cur_processes:
        file.write(item + "\n")

if len(set(ft_processes) ^ set(list_of_cur_processes)):
    print('Nieprawidłowa ilość procesów FT')
    print(set(ft_processes) ^ set(list_of_cur_processes))
else:
    print('wszystko gra')
