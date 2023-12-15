from datetime import date, datetime, timedelta


class InvalidDateOfEmployment(Exception):
    def __init__(self, hire_date, message='Check the date - sth is wrong'):
        self.hire_date = hire_date
        self.message = message
        super().__init__(f'{self.message}: {hire_date}')


class BaseEmployee:
    def __init__(self, first_name: str, last_name: str, hire_date: datetime):
        today = datetime.now().date()

        if hire_date.date() > today or hire_date.date() < date(today.year - 50, today.month, today.day):
            raise InvalidDateOfEmployment(hd.date())

        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date

    def get_employment_time(self):
        f_today = datetime.now()

        return (f_today - self.hire_date).days

    def __lt__(self, other):
        return self.get_employment_time() > other.get_employment_time()

    def __repr__(self):
        return f'{self.first_name} {self.last_name} pracuje od {self.hire_date}'


class Employee(BaseEmployee):
    def __init__(self, first_name: str, last_name: str, hire_date: datetime, hourly_rate: float, work_hours: int, bonus: float):
        super().__init__(first_name, last_name, hire_date)
        self.hourly_rate = hourly_rate
        self.work_hours = work_hours
        self.bonus = bonus

    def get_salary(self):
        return (self.hourly_rate * self.work_hours) + (self.hourly_rate * self.work_hours) * self.bonus / 100


if __name__ == '__main__':
    fn, ln = input('Podaj imię i nazwisko: ').split(' ')
    hd = datetime.strptime(input('Podaj datę rozpoczęcia pracy w formacie dd.mm.yyyy: '), '%d.%m.%Y')

    # do BaseEmployee
    emp1 = BaseEmployee(fn, ln, hd)
    emp2 = BaseEmployee('Ola', 'Lel', datetime.strptime('01.01.2020', '%d.%m.%Y'))
    emp3 = BaseEmployee('Zuza', 'Lel', datetime(2016, 1, 1, 0, 0, 0))

    emp = [emp1, emp2, emp3]
    # sposób 1
    # emp_sorted = sorted(emp)
    # print('Pracownicy posortowani od najdłużej do najkrócej pracującego:')
    # for i in emp_sorted:
    #     print(f'{i.first_name} {i.last_name} pracuje od {i.hire_date}')

    # sposób 2 w oparciu o __repr__
    emp.sort()
    print(emp)

    # do Employee
    emp3 = Employee('Pati', 'Lel', datetime.strptime('01.01.2016', '%d.%m.%Y'), 100, 160, 10)
    print(f'{emp3.first_name} {emp3.last_name} zarabia {emp3.get_salary()} i pracuje od {emp3.get_employment_time()}')
