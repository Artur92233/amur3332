import constants


def calculate_summ(prices: list[float]) -> float:
    """
    Розраховує загальну суму списку цін.
    """
    return sum(prices)


def return_list_of_fruits(items: list[str]) -> list[str]:
    """
    Повертає список, де елемент повторюється лише раз.
    """
    return list(set(items))


def can_you_buy_it(budget: float, banana_price: float) -> bool:
    """
    Перевіряє, чи достатньо бюджету для покупки товару.
    """
    result = budget >= banana_price
    return result
