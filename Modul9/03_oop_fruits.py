class Fruit:
    def __init__(self, color: str, taste: str, kind: str):
        self.color = color
        self.taste = taste
        self.kind = kind


class Basket:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit: Fruit):
        self.fruits.append(fruit)


# class Report:
#     def __init__(self, basket: Basket):
#         self.basket = basket
#
#     def show_data(self):
#         for fruit in self.basket.fruits:
#             print(f'w koszyku jest jabłko o kolorze: {fruit.color}, smaku: {fruit.taste} i rodzaju: {fruit.kind}')


class ReportKacper:
    def get_report(self, property: str, basket: Basket):
        statistics = {}
        for apple in basket.fruits:
            if property == 'color':
                statistics.update({apple.color: statistics.get(apple.color, 0) + 1})
            elif property == 'taste':
                statistics.update({apple.taste: statistics.get(apple.taste, 0) + 1})
            else:
                statistics.update({apple.kind: statistics.get(apple.kind, 0) + 1})

        return statistics


if __name__ == '__main__':
    fruit1 = Fruit('zielony', 'kwaśny', 'dojrzały')
    fruit2 = Fruit('żółty', 'kwaśny', 'niedojrzały')
    fruit3 = Fruit('czerwony', 'słodki', 'dojrzały')
    fruit4 = Fruit('czerwony', 'kwaśny', 'dojrzały')
    fruit5 = Fruit('czerwony', 'słodki', 'niedojrzały')

    basket1 = Basket()
    basket1.add_fruit(fruit1)
    basket1.add_fruit(fruit2)
    basket1.add_fruit(fruit3)
    basket1.add_fruit(fruit4)
    basket1.add_fruit(fruit5)

    # report1 = Report(basket1)
    # report1.show_data()
    rep = ReportKacper()
    print(rep.get_report('color', basket1))













