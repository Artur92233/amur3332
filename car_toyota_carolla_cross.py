corolla_cross = {
    'information': 'Corolla Cross Гібрид',
    'cost,grn': 1658563,
    'engine_displacement_type_hibrid_k_s': 197,
    'massa,': {'min_massa': 1510,
               'max_massa': 1590},
    'max_speed_km_one_hour': 180,
    'interior': ['Кермо оздоблене шкірою', 'Фонова ілюмінація передніх дверей',
                 'Фонова ілюмінація центральної консолі'],
    'parameters_baggage': {
        'volume_of_the_luggage_compartment_l': 390,
        'volume_of_the_luggage_compartment_with_folded_seats_l': 1299

    }
}

corolla_cross['max_massa_trailer_with_brakes_kg'] = 750
# max_masa_trailer = corolla_cross['max_massa_trailer_with_brakes_kg']

name_of_car = corolla_cross['information']
cost_of_car = corolla_cross['cost,grn']
first_interior_of_car = corolla_cross['interior'][0]
car_with_folded_seats = corolla_cross['parameters_baggage']['volume_of_the_luggage_compartment_with_folded_seats_l']
