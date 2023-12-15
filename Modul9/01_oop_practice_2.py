class Car:
    def __init__(self, name: str, price: int, max_speed: int):
        self.name = name
        self.price = price
        self.max_speed = max_speed

    def get_car(self):
        print(f'{self.name} koszuje {self.price} i zasuwa z prędkością {self.max_speed}')


if __name__ == '__main__':
    cars = []
    for _ in range(2):
        cars.append(
            Car(input('Podaj nazwę auta: '),
                int(input('Podaj cenę auta: ')),
                int(input('Podaj max prędkość: '))
                )
        )

    cars[0].get_car()
# lub można od razu pokazać
    for car in cars:
        print(f'{car.name} koszuje {car.price} i zasuwa z prędkością {car.max_speed}')