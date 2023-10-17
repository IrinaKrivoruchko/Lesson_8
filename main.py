import re
#1 Home number
# pattern = r'^\d{9}$'
#
# # Примеры телефонных номеров для проверки
# home_numbers = ["123456789", "987654321", "12345ABC", "1234567890"]
#
# for home_number in home_numbers:
#     if re.match(pattern, home_number):
#         print(f"{home_number} - Right")
#     else:
#         print(f"{home_number} - Not right")

#2 Phone number
# pattern = r'^(?:\+?380|\b380)\d{9}$'
#
# # Примеры телефонных номеров для проверки
# phone_numbers = ["+380123456789", "380987654321", "014785236", "+380j00000000"]
#
# for phone_number in phone_numbers:
#     if re.match(pattern, phone_number):
#         print(f"{phone_number} - Right")
#     else:
#         print(f"{phone_number} - Not right")

#3 email
# pattern = r'^[a-zA-Z0-9._%+-]{3,30}@[a-zA-Z0-9.-]{2,10}\.[a-zA-Z]{2,5}$'
#
# # Примеры email-адресов для проверки
# emails = ["Kryvoruchko@gmail.com", "Kryvoruchko_Iryna@domain.co.uk", "a@b.c", "invalid.email@qwertyuiopl.asdfghjkl"]
#
# for email in emails:
#     if re.match(pattern, email):
#         print(f"{email} - Right")
#     else:
#         print(f"{email} - Not right")

#4
pattern = r'^[а-яА-Яa-zA-ZіІїЇєЄґҐ]{2,20}\s[а-яА-Яa-zA-ZіІїЇєЄґҐ]{2,20}\s[а-яА-Яa-zA-ZіІїЇєЄґҐ]{2,20}$'

# Примеры ФИО для проверки
full_names = ["Криворучко Ірина Валеріївна", "Иванов Иван Иванович", "Иванов Иван", "John", "qwertyuioplkjhgfdsazxcvbnm"]

for full_name in full_names:
    if re.match(pattern, full_name):
        print(f"{full_name} - Right")
    else:
        print(f"{full_name} - Not right")

