class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.time = 0

    def add_time(self, time_in_h: float):
        self.time += time_in_h

    def get_salary(self) -> float:
        salary = self.rate * self.time
        # resetowanie czasu pracy przed kolejną wypłatą
        self.time = 0
        
        return salary


class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, rate: float):
        super().__init__(first_name, last_name, rate)
        self.bonus = 0

    def add_bonus(self, amount: int):
        self.bonus += amount

    def get_salary(self) -> float:
        # pomnożone przez 2, ponieważ treść zadania nakazywała podwajać ilość godzin
        return super().get_salary() * 2 + self.bonus


def test_get_salary_manager():
    manager = Manager('Jan', 'Kowalski', 100)
    manager.add_time(100)
    manager.add_bonus(888)

    assert manager.get_salary() == 20888


emp = Manager('Jan', 'Kowalski', 100)
emp.add_time(100)
print(emp.get_salary())
emp.add_time(20)
print(emp.get_salary())
