import csv
import json


with open('schedule.csv', 'w', newline='') as fh:
    information = [
        'name',
        'surname',

        'departure point',
        'destination point',

        'departure time',
        'arrival time',

        'cost ticket'
    ]

    writer_ifo = csv.DictWriter(fh, fieldnames=information)

    writer_ifo.writeheader()
    writer_ifo.writerow({

        'name': 'Joni',
        'surname': "Poll",

        'departure point': 'Kiev',
        'destination point': 'Odessa',

        'departure time': "14:00",
        'arrival time': "5 hours",

        'cost ticket': '1200 UAH'

    })

    writer_ifo.writerow({

        'name': 'Gustav',
        'surname': "Anderson",

        'departure point': 'Odessa',
        'destination point': 'Ternopil',

        'departure time': "12:00",
        'arrival time': "7 hours",

        'cost ticket': '1800 UAH'

    })

    writer_ifo.writerow({

        'name': 'Jason',
        'surname': "Statham",

        'departure point': 'Ternopil',
        'destination point': 'Kiev',

        'departure time': "10:00",
        'arrival time': "12 hours",

        'cost ticket': '2500 UAH'

    })


def reader_csv():
    with open('schedule.csv', newline='') as information_list:
        reader = csv.DictReader(information_list)
        list_with_csv = []

        for row in reader:
            list_with_csv.append(row)
            print(

                f"Name: {row['name']}, "
                f"Surname: {row['surname']},\n"

                f"Departure point: {row['departure point']}, "
                f"Destination point: {row['destination point']},\n"

                f"Departure time: {row['departure time']}, "
                f"Arrival time: {row['arrival time']}, "

                f"Cost ticket: {row['cost ticket']},\n "

            )

            def save_info_in_jason():
                with open('schedule.json', 'w') as inf:
                    json.dump(list_with_csv, inf, indent=4, sort_keys=True)

            # save_info_in_jason()
        return save_info_in_jason


reader_csv()
