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

#2 Phone number
pattern = r'^(?:\+?380|\b380)\d{9}$'

# Примеры телефонных номеров для проверки
phone_numbers = ["+380123456789", "380987654321", "014785236", "+380j00000000"]

for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        print(f"{phone_number} - Right")
    else:
        print(f"{phone_number} - Not right")


