import re

def normalize_phone(phone_number):

    # Видалення всіх символів, крім цифр і '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())
    
    # Перевірка чи номер містить міжнародний код
    if not cleaned_number.startswith("+"):
        if cleaned_number.startswith("380"):
            cleaned_number = "+" + cleaned_number
        else:
            cleaned_number = "+38" + cleaned_number
    
    return cleaned_number

# Введення номера користувачем
user_number = input("Введіть номер телефону у будь-якому форматі: ")
normalized_number = normalize_phone(user_number)
print(f"Нормалізований номер телефону: {normalized_number}")
