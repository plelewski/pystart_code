# kto nie jedzie na wycieczkę

students = {
    ("Adam", "Adamowski"),
    ("Piotr", "Piotrowski"),
    ("Alicja", "Kowalska"),
    ("Ewa", "Wiśniewska")
}

going_to_trip = {
    ("Piotr", "Piotrowski"),
    ("Alicja", "Kowalska"),
}

print(students - going_to_trip)
