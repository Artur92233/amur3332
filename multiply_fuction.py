import decimal
def multiply(*args: int | float) -> int | float:
    summ = 1
    for number in args:
        summ *= number
        summ_decimal = decimal.Decimal(str(summ)).quantize(decimal.Decimal('0.01'))
    print(f'Сумма {summ_decimal}')
    return summ_decimal


multiply(2, 3, 4)
multiply(5, 6)
