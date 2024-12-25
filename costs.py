import decimal

blinchiki_with_meat_cost = 119.00
blinchiki_with_meat_price = decimal.Decimal(str(blinchiki_with_meat_cost)).quantize(decimal.Decimal('0.01'))

okroshka_cost = 89.99
okroshka_price = decimal.Decimal(str(okroshka_cost)).quantize(decimal.Decimal('0.01'))

borsh_cost = 99.99
borsh_price = decimal.Decimal(str(borsh_cost)).quantize(decimal.Decimal('0.01'))

chocolate_ice_cream_cost = 49.99
chocolate_ice_cream_price = decimal.Decimal(str(chocolate_ice_cream_cost)).quantize(decimal.Decimal('0.01'))

sushi_cost = 170.99
sushi_price = decimal.Decimal(str(sushi_cost)).quantize(decimal.Decimal('0.01'))
