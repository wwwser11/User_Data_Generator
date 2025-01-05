import argparse
import json
import random
import string
from datetime import datetime, timedelta


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

def phone_gen ():
    number = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return '+1'+ number

def date_of_birth (start_date, end_date):
    delta = end_date - start_date
    days_diff = delta.days
    random_additional_days_number = random.randint(0, days_diff)
    random_date_of_birth = start_date + timedelta(days=random_additional_days_number)
    return random_date_of_birth.strftime("%m-%d-%Y")

def password_gen (length, special_characters):
    if special_characters:
        char = string.digits + string.ascii_letters
        password = ''.join(random.choices(char, k=length-2)) + str(random.choice(string.digits)) + str(random.choice(string.punctuation))
    else:
        char = string.digits + string.ascii_letters
        password = ''.join(random.choices(char, k=length-1)) + str(random.choice(string.digits))
    return password

def user_data_creator(user_qty=1, password_length=8, password_special_characters=True, start_year=1925, end_year=2007, file_name="users.json"):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 1, 1)

    data = {"users": []}
    for _ in range(user_qty):
        user = {
            'name': name_gen(names_data),
            'date_of_birth': date_of_birth(start_date, end_date),
            'email': email_gen(names_data),
            'phone': phone_gen(),
            'password':password_gen(password_length, password_special_characters)
        }
        data['users'].append(user)

    with open(file_name, "w") as ufile:
        json.dump(data, ufile, indent=4)

    print(f'Test user data has been saved in: {file_name}')

def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ("yes", "true", "t", "1", "y"):
        return True
    elif value.lower() in ("no", "false", "f", "0", "n"):
        return False

# Handle command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test user data and save it to a JSON file.")
    parser.add_argument("--user_qty", type=int, default=1, help="Number of users (default is 1)")
    parser.add_argument("--password_length", type=int, default=8, help="Password length (default is 8)")
    parser.add_argument("--password_special_characters", type=str2bool, default=True, help="Include special characters in password (default is True)")
    parser.add_argument("--start_year", type=int, default=1925, help="Start year for birth dates (default is 1925)")
    parser.add_argument("--end_year", type=int, default=2007, help="End year for birth dates (default is 2007)")
    parser.add_argument("--file", type=str, default="users.json", help="Output file name (default is 'users.json')")

    args = parser.parse_args()

    # Call the function with parsed arguments
    user_data_creator(
        user_qty=args.user_qty,
        password_length=args.password_length,
        password_special_characters=args.password_special_characters,
        start_year=args.start_year,
        end_year=args.end_year,
        file_name=args.file
    )
