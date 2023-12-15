import subprocess


answer = input('Podaj domenę do wysłania ping\'a: ')
response = subprocess.run(["ping", "-c", "1", answer], capture_output=True)
# subprocess.run(["ls", "-l"])
print(response.stdout.decode('utf8'))
print(response)

if response.returncode == 0:
    print('Domena odpowiedziała')
else:
    print('Coś nie bangla')
