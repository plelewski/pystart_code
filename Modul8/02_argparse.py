import argparse


parser = argparse.ArgumentParser(
    prog='Image bulk resizer',
    description='It can resize images',
    epilog='Pek Lel'
)

parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('--width', type=int, default=300)
parser.add_argument('--height', type=int, default=300)
parser.add_argument('-a', action='store_true')  # if exists then True else value is False


arguments = parser.parse_args()
print(arguments)
