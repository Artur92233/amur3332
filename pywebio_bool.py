import logging
import zoo_constant
from pywebio.input import input as pw_input, NUMBER
from pywebio.output import put_text

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

age_input = pw_input(label='Скількі тобі років?', required=True, type=NUMBER)
logging.info(f'Людина написала скількі її років --> {age_input}')

if age_input < 6:
    price = zoo_constant.discount_little_kids
elif 6 <= age_input <= 12:
    price = zoo_constant.discount_big_kids
elif 13 <= age_input <= 17:
    price = zoo_constant.discount_teenager
elif 18 <= age_input < 60:
    price = zoo_constant.discount_adults
elif age_input >= 60:
    price = zoo_constant.discount_elderly
else:
    price = 'Неправильно введено вік'

put_text(f"Фінальна вартість квитка: {price} грн")
