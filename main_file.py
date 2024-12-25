import decimal
import phrases
import costs
import constants
import names_of_dishes

total_cost = 0
name_of_the_client =input('Як я можу до вас звертатись: ')
name_of_the_client = str(name_of_the_client).capitalize()
print(phrases.MSG_WELCOME.format(name=name_of_the_client ))

blinchiki_with_meat_quantity = input(phrases.MSG_PROPOSITION_FIRST
                                     .format(dish=names_of_dishes.blinchiki_wiith_meat,
                                             price=costs.blinchiki_with_meat_price))
blinchiki_with_meat_quantity = int(blinchiki_with_meat_quantity)
blinchiki_with_meat_quantity = costs.blinchiki_with_meat_price * blinchiki_with_meat_quantity
total_cost += blinchiki_with_meat_quantity

okroshka_quantity = input(phrases.MSG_PROPOSITION_FIRST
                          .format(dish= names_of_dishes.okroshka_dish, price=costs.okroshka_price))
okroshka_quantity = int(okroshka_quantity)
okroshka_quantity = costs.okroshka_price * okroshka_quantity
total_cost += okroshka_quantity

discount_sum = total_cost * constants.discount
discount_sum = decimal.Decimal(str(discount_sum)).quantize(decimal.Decimal('0.01'))
total_to_pay = total_cost - discount_sum


print(phrases.DISCOUNT.format(discount= f'{constants.discount * 100}%'))


print('~' * 51)
print('- ' * 26)
print(phrases.MSG_TOTAL.format(total=total_cost))
print(phrases.MSG_DISCOUNT.format(discount= discount_sum))
print(phrases.MSG_TOTAL_TO_PAY.format(pay= total_to_pay))
