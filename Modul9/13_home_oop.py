from json import load, dump


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class JsonFile:
    def __init__(self, filename: str):
        self.filename = filename
        self.persons = []

    def get_data(self):
        try:
            with open(self.filename, 'r') as file:
                self.persons = load(file)
        except FileNotFoundError:
            self.persons = []

    def add_element(self, person: Person):
        self.get_data()
        self.persons.append({
            'first_name': person.first_name,
            'last_name': person.last_name
        })

        with open(self.filename, 'w') as file:
            dump(self.persons, file)


if __name__ == '__main__':
    el1 = Person('Jacek', 'Placek')

    df = JsonFile('data.json')
    df.add_element(el1)
