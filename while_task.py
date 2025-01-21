def break_if_number_zero(summ: int) -> int:
    while True:
        number = int(input('Введіть число: '))
        summ += number
        if number == 0:
            print(f'Сума чисел: {summ}')
            return


break_if_number_zero(summ=0)
