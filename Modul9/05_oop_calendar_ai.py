#### wersja 1 ####

# class Spotkanie:
#     def __init__(self, data, godzina):
#         self.data = data
#         self.godzina = godzina
#
# class Kalendarz:
#     def __init__(self):
#         self.spotkania = {}
#
#     def dodaj_spotkanie(self, spotkanie):
#         if spotkanie.data in self.spotkania:
#             if spotkanie.godzina in self.spotkania[spotkanie.data]:
#                 print("W tym czasie jest już inne spotkanie!")
#             else:
#                 self.spotkania[spotkanie.data][spotkanie.godzina] = spotkanie
#         else:
#             self.spotkania[spotkanie.data] = {spotkanie.godzina: spotkanie}
#
#     def pokaz_spotkania(self):
#         for data, godziny in self.spotkania.items():
#             for godzina, spotkanie in godziny.items():
#                 print(f"{data} o {godzina}:00 - Spotkanie")
#
#
# kalendarz = Kalendarz()
#
# spotkanie1 = Spotkanie("2023-11-21", 10)
# spotkanie2 = Spotkanie("2023-11-21", 12)
# spotkanie3 = Spotkanie("2023-11-22", 11)
#
# kalendarz.dodaj_spotkanie(spotkanie1)
# kalendarz.dodaj_spotkanie(spotkanie2)
# kalendarz.dodaj_spotkanie(spotkanie3)
#
# kalendarz.pokaz_spotkania()

#### wersja 2 ####
# import json
#
# class Spotkanie:
#     def __init__(self, data, godzina):
#         self.data = data
#         self.godzina = godzina
#
# class Kalendarz:
#     def __init__(self):
#         self.spotkania = {}
#
#     def dodaj_spotkanie(self, spotkanie):
#         if spotkanie.data in self.spotkania:
#             if spotkanie.godzina in self.spotkania[spotkanie.data]:
#                 print("W tym czasie jest już inne spotkanie!")
#             else:
#                 self.spotkania[spotkanie.data][spotkanie.godzina] = spotkanie
#         else:
#             self.spotkania[spotkanie.data] = {spotkanie.godzina: spotkanie}
#
#     def zapisz_do_pliku(self, nazwa_pliku):
#         with open(nazwa_pliku, 'w') as plik:
#             json.dump(self.spotkania, plik, indent=4)
#
#     def wczytaj_z_pliku(self, nazwa_pliku):
#         with open(nazwa_pliku, 'r') as plik:
#             self.spotkania = json.load(plik)
#
#     def pokaz_spotkania(self):
#         for data, godziny in self.spotkania.items():
#             for godzina, spotkanie in godziny.items():
#                 print(f"{data} o {godzina}:00 - Spotkanie")
#
# # Przykładowe użycie
# kalendarz = Kalendarz()
#
# spotkanie1 = Spotkanie("2023-11-21", 10)
# spotkanie2 = Spotkanie("2023-11-21", 12)
# spotkanie3 = Spotkanie("2023-11-22", 11)
#
# kalendarz.dodaj_spotkanie(spotkanie1)
# kalendarz.dodaj_spotkanie(spotkanie2)
# kalendarz.dodaj_spotkanie(spotkanie3)
#
# kalendarz.zapisz_do_pliku('meetings.json')  # Zapis do pliku
#
# # Wczytanie spotkań z pliku
# kalendarz2 = Kalendarz()
# kalendarz2.wczytaj_z_pliku('meetings.json')
#
# kalendarz2.pokaz_spotkania()

#### wersja3 ###
import json

class Spotkanie:
    def __init__(self, data, godzina):
        self.data = data
        self.godzina = godzina

    def serializuj(self):
        return {'data': self.data, 'godzina': self.godzina}

    @classmethod
    def deserializuj(cls, serialized):
        return cls(serialized['data'], serialized['godzina'])

class Kalendarz:
    def __init__(self):
        self.spotkania = {}

    def dodaj_spotkanie(self, spotkanie):
        if spotkanie.data in self.spotkania:
            if spotkanie.godzina in self.spotkania[spotkanie.data]:
                print("W tym czasie jest już inne spotkanie!")
            else:
                self.spotkania[spotkanie.data][spotkanie.godzina] = spotkanie.serializuj()
        else:
            self.spotkania[spotkanie.data] = {spotkanie.godzina: spotkanie.serializuj()}

    def zapisz_do_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'w') as plik:
            json.dump(self.spotkania, plik, indent=4)

    def wczytaj_z_pliku(self, nazwa_pliku):
        with open(nazwa_pliku, 'r') as plik:
            self.spotkania = json.load(plik, object_hook=self.deserialize_hook)

    def deserialize_hook(self, obj):
        if 'data' in obj and 'godzina' in obj:
            return {obj['data']: {obj['godzina']: Spotkanie.deserializuj(obj)}}
        return obj

    def pokaz_spotkania(self):
        for data, godziny in self.spotkania.items():
            for godzina, spotkanie in godziny.items():
                print(f"{data} o {godzina}:00 - Spotkanie")

# Przykładowe użycie
kalendarz = Kalendarz()

spotkanie1 = Spotkanie("2023-11-21", 10)
spotkanie2 = Spotkanie("2023-11-21", 12)
spotkanie3 = Spotkanie("2023-11-22", 11)

kalendarz.dodaj_spotkanie(spotkanie1)
kalendarz.dodaj_spotkanie(spotkanie2)
kalendarz.dodaj_spotkanie(spotkanie3)

kalendarz.zapisz_do_pliku('meetings_ai.json')  # Zapis do pliku

# Wczytanie spotkań z pliku
kalendarz2 = Kalendarz()
kalendarz2.wczytaj_z_pliku('meetings.json')

kalendarz2.pokaz_spotkania()
