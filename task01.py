from datetime import datetime

def get_days_from_today(date):

    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (input_date - today).days
        return delta
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

# Введення дати користувачем
try:
    user_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
    result = get_days_from_today(user_date)
    print(f"Кількість днів між сьогоднішньою датою і {user_date}: {result} днів")
except ValueError as e:
    print(f"Помилка: {e}")
