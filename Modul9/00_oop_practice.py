from math import pi

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_circuit(self):
        return self.radius ** 2

    def get_field(self):
        return round(2 * pi * self.radius,2)


# python -m pytest nazwa_skryptu.py
def test_circle_calc():
    cir = Circle(5)
    c = cir.get_circuit()
    f = cir.get_field()

    assert c == 25
    assert 31.4 < f < 31.5


if __name__ == '__main__':
    cir1 = Circle(5)
    print(cir1.get_circuit())
    print(cir1.get_field())
