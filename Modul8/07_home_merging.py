from os import walk
from pathlib import Path


with open('scalone.txt', mode='w') as output:
    for path, _, files in walk('/Users/przemek/Przemek'):
        for file in files:
            source = Path(f'{path}/{file}')
            if source.suffix == '.txt':
                with open(source, mode='r') as source:
                    output.write('\n'.join(source.readlines()))
                    output.write('\n')
