import decimal


PRICE = 100


DISCOUNT_FOR_LITTLE_KIDS = 100 % PRICE
discount_little_kids = decimal.Decimal(str(DISCOUNT_FOR_LITTLE_KIDS)).quantize(decimal.Decimal('0.01'))


DISCOUNT_FOR_BIG_KIDS = 50 % PRICE
discount_big_kids = decimal.Decimal(str(DISCOUNT_FOR_BIG_KIDS)).quantize(decimal.Decimal('0.01'))


DISCOUNT_FOR_TEENAGER = 75 % PRICE
discount_teenager = decimal.Decimal(str(DISCOUNT_FOR_TEENAGER)).quantize(decimal.Decimal('0.01'))


DISCOUNT_FOR_ADULTS = 0 % PRICE
discount_adults = decimal.Decimal(str(DISCOUNT_FOR_ADULTS)).quantize(decimal.Decimal('0.01'))


DISCOUNT_FOR_ELDERLY = 70 % PRICE
discount_elderly = decimal.Decimal(str(DISCOUNT_FOR_ELDERLY)).quantize(decimal.Decimal('0.01'))
