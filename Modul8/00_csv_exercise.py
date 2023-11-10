import csv

with open('cars.csv', mode='w', newline='') as csvfile:
    v_fieldnames = ['Name', 'time_to_100', 'speed_record']
    writer = csv.DictWriter(csvfile, fieldnames=v_fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerow({'Name': 'Venom F5', 'time_to_100': 2.6, 'speed_record': 484})
    writer.writerow({'Name': 'SSC Tuara', 'time_to_100': 2.5, 'speed_record': 460})
    writer.writerow({'Name': 'Agera RS', 'time_to_100': 3.1, 'speed_record': 457})

with open('cars.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        print(row['Name'])
