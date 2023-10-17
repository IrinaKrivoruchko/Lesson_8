import re
#1 Home number
pattern = r'^\d{9}$'

# Примеры телефонных номеров для проверки
home_numbers = ["123456789", "987654321", "12345ABC", "1234567890"]

for home_number in home_numbers:
    if re.match(pattern, home_number):
        print(f"{home_number} - Right")
    else:
        print(f"{home_number} - Not right")
