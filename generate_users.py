import random
import names
import string
from datetime import datetime
import calendar


def save_text_file():
    email, first_name, last_name = _gen_user()
    year, day, month = gen_date()
    _password = _gen_pass()

    with open('users.txt', 'w') as _file:
        _file.write('First name: {} , Last name: {} , Username: {} , Password: {} \n'.format(
            first_name, last_name, email, _password))
        _file.write('Year: {}, Day: {}, Month: {}'.format(year, day, month))
        _file.close()

    return email, first_name, last_name, _password, month, day, year


def _gen_user():
    full_name = names.get_full_name()
    first_name, last_name = full_name.split()
    chunk = full_name[0][0].lower()
    second_chunk = full_name[-1][:3].lower()
    rand_num = '{:03d}'.format(random.randint(0, 10000))
    return chunk + second_chunk + rand_num, first_name, last_name


def _gen_pass():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(15))


def gen_date():
    year = random.randint(1880, 1995)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birhtdate = datetime(year, month, day)
    month_name = calendar.month_name[month]
    return birhtdate.year, birhtdate.day, month_name[0] + month_name[1] + month_name[2]
