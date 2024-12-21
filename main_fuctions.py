import utils
import constants

summ = utils.calculate_summ(constants.PRICE)
# print(summ)

fruit_list = utils.return_list_of_fruits(constants.FRUITS)
# print(fruit_list)


client_budget = 190.91
can_i_buy_banana = utils.can_you_buy_it(banana_price=constants.PRICE_OF_BANANA, budget=client_budget)
#print(can_i_buy_banana)
