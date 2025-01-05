# User Data Generator

## Overview
This Python script generates customizable test user data and saves it to a JSON file. It supports dynamic configuration through command-line arguments, allowing you to control the number of users, password complexity, date of birth ranges, and output file name.

---

## Features
- **Random User Data Generation**:
  - Names generated using predefined first and last names.
  - Random email addresses with flexible lengths and domain selection.
  - US-format phone numbers (+1XXXXXXXXXX).
  - Configurable date of birth ranges.
  - Secure passwords with optional special characters.
- **Command-Line Interface (CLI)**:
  - Easily customize the output using CLI arguments.
- **Flexible Output**:
  - Saves data in JSON format for easy integration with other tools.
- **Error Handling**:
  - Ensures compatibility and flexibility with input validation.

---

## Requirements
- Python 3.6 or higher

### Install dependencies
```
pip install -r requirements.txt
```

---

## Usage

### Basic Example:
Generate 10 users with default settings and save them in `users.json`:
```
python3 data_generator.py --user_qty 10
```

### Advanced Example:
Customize parameters:
```
python3 data_generator.py \
  --user_qty 15 \
  --password_length 12 \
  --password_special_characters True \
  --start_year 1980 \
  --end_year 2000 \
  --file test_users.json
```

### Command-Line Arguments:
| Argument                         | Description                                                        | Default Value         |
|----------------------------------|--------------------------------------------------------------------|-----------------------|
| `--user_qty`                     | Number of users to generate.                                       | 1                     |
| `--password_length`              | Length of generated passwords.                                     | 8                     |
| `--password_special_characters`  | Include special characters in passwords (True/False).              | True                  |
| `--start_year`                   | Start year for date of birth range.                                | 1925                  |
| `--end_year`                     | End year for date of birth range.                                  | 2007                  |
| `--file`                         | Output file name.                                                  | users.json            |

---

## Output Example
```json
{
    "users": [
        {
            "name": "John Smith",
            "date_of_birth": "1987-06-15",
            "email": "x8dj2f6z@gmail.com",
            "phone": "+16543219876",
            "password": "aB!7d#pX2@"
        },
        {
            "name": "Alice Johnson",
            "date_of_birth": "1995-12-10",
            "email": "y7fhjks2@yahoo.com",
            "phone": "+17238975643",
            "password": "P@ssw0rd!"
        }
    ]
}
```

---

## Notes
- Ensure the `extra_data.json` file is present and includes `first_names`, `last_names`, and `domains` keys.
- The script validates input parameters and provides meaningful error messages if something goes wrong.
- Supports boolean arguments like `True/False` and `1/0`.

---

## Customization
You can modify the script to include additional fields or change formats. Each data type is generated through separate functions, making it easy to add new features.

---

## Author
Developed by Sergei G.