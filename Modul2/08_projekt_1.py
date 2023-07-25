from math import ceil

how_many_walls = int(input('Ile ścian do pomalowania: '))
default_height = 2.75
meters_to_paint = 0
paint_productivity = 13

print('Domyślna wysokość to 2.75m - za chwilę będzie można to zmienić.')

for wall in range(0, how_many_walls):
    width_wall = float(input(f'Szerokość ściany numer {wall+1}: '))
    height_wall = input(f'Wysokość ściany numer {wall+1} (enter przyjmuje wartość domyśną lub poprzednią): ')
    if height_wall == '':
        height_wall = default_height
    meters_to_paint += width_wall * float(height_wall)
    default_height = height_wall


print(f'Powierzchnia do pomalowania wynosi: {meters_to_paint:.2f}')
how_many_layers = int(input('Ile warstw farby chcesz położyć: '))

print(f'Potrzebujesz {ceil(meters_to_paint * how_many_layers / paint_productivity)} litrów farby')
