import tkinter as tk


def add_person():
    persons = set()
    with open('dane_klientow2.txt', encoding='utf8', mode='r') as file:
        for line in file:
            first_name, last_name = line.strip().split(' ')
            persons.add(
                (first_name, last_name)
            )

    print(persons)

    with open('dane_klientow2.txt', encoding='utf8', mode='a') as file:
        if (first_name_entry.get(),last_name_entry.get()) not in persons:
            file.write(f'{first_name_entry.get()} {last_name_entry.get()}\n')


window = tk.Tk()
window.title('Dodaj osobę')

first_name_label = tk.Label(window, text='Jak masz na imię')
first_name_label.pack()
first_name_entry = tk.Entry()
first_name_entry.pack()

last_name_label = tk.Label(window, text='Jak masz na nazwisko')
last_name_label.pack()
last_name_entry = tk.Entry()
last_name_entry.pack()

button = tk.Button(text='Dodaj', command=add_person)
button.pack()

window.mainloop()
