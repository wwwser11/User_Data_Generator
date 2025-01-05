import json
import random
import string
from math import radians

with open('extra_data.json') as file:
    names_data = json.load(file)



def name_gen (names_dict):
    first_name = random.choice(names_dict['first_names'])
    second_name = random.choice(names_dict['last_names'])
    full_name = first_name + ' ' + second_name
    return full_name


def email_gen (extra_data):
    all_letters = string.ascii_lowercase
    email_length = random.randint(1, 10)
    name = ''.join(random.choices(all_letters + string.digits, k=email_length))
    domain = str(random.choice(extra_data['domains']))
    return name+'@'+domain

print(name_gen(names_data), email_gen(names_data))