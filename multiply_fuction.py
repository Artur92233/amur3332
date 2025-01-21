def multiply(*args: int) -> int:
    summ = 1
    for number in args:
        summ *= number
    print(f'Сумма {summ}')


multiply(2, 3, 4)
multiply(5, 6)
