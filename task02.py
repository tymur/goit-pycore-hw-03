import random

def get_numbers_ticket(min_value, max_value, quantity):

    # Перевірка на валідність параметрів
    if min_value < 1 or max_value > 1000 or quantity < 1 or quantity > (max_value - min_value + 1):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    
    # Сортування чисел
    return sorted(numbers)

# Тестування функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
