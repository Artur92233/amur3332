
import decimal
from datetime import datetime

total_cost = 0
# fist_item
item_one_title = input('Введіть назву першого товару: ')

item_one_quantity = input('Введіть бажаєму кількість першого товару: ')
item_one_quantity = int(item_one_quantity)

item_one_price = input('Введіть ціну першого товару: ')
item_one_price = decimal.Decimal(str(item_one_price)).quantize(decimal.Decimal('0.01'))

item_one_total = item_one_price * item_one_quantity
total_cost += item_one_total

# second_item
item_two_title = input('Введіть назву другого товару: ')

item_two_quantity = input('Введіть бажаєму кількість другого товару: ')
item_two_quantity = int(item_two_quantity)

item_two_price = input('Введіть ціну другого товару: ')
item_two_price = decimal.Decimal(str(item_two_price)).quantize(decimal.Decimal('0.01'))

item_two_total = item_two_price * item_two_quantity
total_cost += item_two_total

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'
printing_second_template = '{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}'
printing_third_template = '\t\t{}\t\t'
# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\tкількість\t\t\tціна\t\t\tвартість')
print(printing_template.format(item_one_title, item_one_quantity, item_one_price, item_one_total))
print(printing_template.format(item_two_title, item_two_quantity, item_two_price, item_two_total))
print('~' * 80)
print(printing_second_template.format(
    "ВСЬОГО".ljust(5),
    item_one_quantity + item_one_quantity,
    item_one_price + item_two_price,
    item_two_total + item_one_total,
)
)

print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')
