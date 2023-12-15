import argparse
from os import walk
from pathlib import Path


parser = argparse.ArgumentParser(
    prog='File finder',
    description='It can find any files',
    epilog='Pek Lel'
)

parser.add_argument('--dir', type=str)
parser.add_argument('--extension', type=str, default='jpg')

arguments = parser.parse_args()

for path, _, files in walk(arguments.dir):
    for photo in files:
        source = Path(f'{path}/{photo}')
        if source.suffix == '.jpg':
            print(source.absolute())
