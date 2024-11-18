from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    today = datetime.today().date()
    week_later = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження у об'єкт datetime.date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        # Зміна року на поточний
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження цього року вже минув, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевірка, чи день народження у проміжку наступного тижня
        if today <= birthday_this_year <= week_later:
            # Якщо день народження на вихідний, переносимо на понеділок
            if birthday_this_year.weekday() in (5, 6):  # Субота (5) або неділя (6)
                next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                congratulation_date = next_monday
            else:
                congratulation_date = birthday_this_year
            
            # Додавання до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Тестовий список користувачів
users = [
    {"name": "John Doe", "birthday": "1985.11.23"},
    {"name": "Jane Smith", "birthday": "1990.11.27"},
    {"name": "Alice Johnson", "birthday": "1992.11.28"},
    {"name": "Bob Brown", "birthday": "1988.10.29"}
]

# Виклик функції
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
