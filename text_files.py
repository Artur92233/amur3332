with open('airport-codes_csv.csv', mode='r',encoding='utf-8') as airports:
    airports_data = airports.readlines()
    airports = []
    for row, airport in enumerate(airports_data, start=1):
        if row == 1:
            continue
        airport_clean = airport.strip().split(';')
        airport_country = airport_clean[5]
        if airport[5] == 'UA':
            airports.append(airport[2])



        #result = ', '.join(how_many_people_in_iss)
print(airports)

