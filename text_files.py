with open('airport-codes_csv.csv', mode='r',encoding='utf-8') as airports:
    airports_data = airports.readlines()
    airports = []
    for row, airport in enumerate(airports_data, start=1):
        if row == 1:
            continue
        airport_clean = airport.strip().split(';')
        airport_country = airport_clean[5]
        if airport_country == 'UA':
            airports.append(airport_clean[2])



result = ', '.join(airports)
print(result)
