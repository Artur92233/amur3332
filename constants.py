import decimal

discount_for_this_week = 15 / 100
discount = decimal.Decimal(str(discount_for_this_week)).quantize(decimal.Decimal('0.01'))
