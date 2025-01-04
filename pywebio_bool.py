import logging
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
    price = 'Безкоштовно'
elif 6 <= age_input <= 12:
    price = '50 грн (знижка 50%)'
elif 13 <= age_input <= 17:
    price = '75 грн (знижка 25%)'
elif 18 <= age_input < 60:
    price = '100 грн (повна вартість)'
elif age_input >= 60:
    price = '70 грн (знижка 30%)'
else:
    price = 'Неправильно введено вік'

put_text(f"Фінальна вартість квитка: {price}")
