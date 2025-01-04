import logging
import decimal
from pywebio.input import input as pw_input
from pywebio.input import textarea
from pywebio.output import put_text, put_error, put_success, put_warning, put_html


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)


name_input = pw_input(label='Як тебе звати?', required=True)
logging.info(f'Людина написала як ії звати --> {name_input}')
put_text(name_input)


correct_count = 0


first_answer = pw_input(label='Яка планета є найбільшою у Сонячній системі', required=True)
ANSWER_1 = 'Юпітер'
logging.debug(f'Відповідь на перше питання --> {first_answer}')
is_correct_first_question = ANSWER_1 == first_answer
if is_correct_first_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


second_answer = pw_input(label='Скільки континентів на Землі?', required=True)
ANSWER_2 = '7'
logging.debug(f'Відповідь на друге питання --> {second_answer}')
is_correct_second_question = ANSWER_2 == second_answer
if is_correct_second_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


third_answer = pw_input(label='Як називається столиця Франції?', required=True)
ANSWER_3 = 'Париж'
logging.debug(f'Відповідь на третє питання --> {third_answer}')
is_correct_third_question = ANSWER_3 == third_answer
if is_correct_third_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


fourth_answer = pw_input(label='Який метал є основним у виробництві алюмінієвої фольги?', required=True)
ANSWER_4 = 'Алюміній'
logging.debug(f'Відповідь на четверте питання --> {fourth_answer}')
is_correct_fourth_question = ANSWER_4 == fourth_answer
if is_correct_fourth_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


fifth_answer = pw_input(label='Скільки кольорів у веселці?', required=True)
ANSWER_5 = '7'
logging.debug(f'Відповідь на п`яте питання --> {fifth_answer}')
is_correct_fifth_question = ANSWER_5 == fifth_answer
if is_correct_fifth_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


sixth_answer = pw_input(label='Хто такий Тарас Шевченко?', required=True)
ANSWER_6 = 'Письменник'
logging.debug(f'Відповідь на шосте питання --> {sixth_answer}')
is_correct_sixth_question = ANSWER_6 == sixth_answer
if is_correct_sixth_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


seventh_answer = pw_input(label='Скільки буде 2+2?', required=True)
ANSWER_7 = '4'
logging.debug(f'Відповідь на сьоме питання --> {seventh_answer}')
is_correct_seventh_question = ANSWER_7 == seventh_answer
if is_correct_seventh_question:
    put_success('Правильна відповідь')
    correct_count += 1
else:
    put_error('Неправильна відповідь')


put_text(f'{name_input}, ви набрали {correct_count} з 7 балів.')

score_percentage = (correct_count / 7 * 100)
score_percentage = decimal.Decimal(str(score_percentage)).quantize(decimal.Decimal('0.01'))
put_text(f'Відсоток правильних відповідей: {score_percentage}%')

logging.info(
    f'Користувач {name_input} завершив вікторину з результатом: {correct_count}/ 7 баллів та {score_percentage}%')
