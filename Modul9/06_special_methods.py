class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100

    def __str__(self):
        return f'{self.value} mm'

    def __add__(self, other):
        return LengthUnit(self.value + other.value)

    def __sub__(self, other):
        return LengthUnit(self.value - other.value)

    def __eq__(self, other):
        return self.value == other.value


if __name__ == '__main__':
    lu1 = LengthUnit(100)
    lu2 = LengthUnit(50)

    print(lu1)
    print(lu1 + lu2)
    print(lu1 - lu2)
    print(lu1 == lu2)
