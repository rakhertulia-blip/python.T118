# ==========================================
# Задание 1. Пропуск на мероприятие ЕКЕВ
# ==========================================

def entry_message(group):
    if group == "Т118":
        return "Т118: вход разрешён"
    return "Обратитесь к куратору"

# Сохраняем ссылку на функцию в переменной (без вызова!)
check_entry = entry_message

# Проверочные вызовы через новое имя:
print(check_entry("Т118"))  # Т118: вход разрешён
print(check_entry("Т119"))  # Обратитесь к куратору
print(check_entry("т118"))  # Обратитесь к куратору
print(check_entry(""))      # Обратитесь к куратору

# Вывод типов в консоль:
print("Тип check_entry:", type(check_entry))
print("Тип результата вызова:", type(check_entry("Т118")))

# ==========================================
# Задание 2. Учебные тарифы поездки в Казахстане
# ==========================================

def standard_fare(km):
    return 500 + 100 * km

def student_fare(km):
    return 300 + 70 * km

def trip_cost(km, tariff):
    return tariff(km)  # Вызов переданного тарифа находится в этой строке

# Проверочные вызовы из таблицы:
print(trip_cost(10, standard_fare))  # 1500
print(trip_cost(10, student_fare))   # 1000
print(trip_cost(0, standard_fare))   # 500
print(trip_cost(0, student_fare))    # 300

# Дополнительные проверки для 1 км:
print(trip_cost(1, standard_fare))   # 600
print(trip_cost(1, student_fare))


# ==========================================
# Задание 3. Фабрика скидок для ярмарки
# ==========================================

def make_discount(amount):
    def discount(price):
        if price - amount < 0:
            return 0
        return price - amount
    return discount

discount_100 = make_discount(100)
discount_300 = make_discount(300)

# Основные проверки из таблицы:
print(discount_100(250))  # 150
print(discount_300(250))  # 0
print(discount_100(100))  # 0
print(discount_100(0))    # 0
print(discount_300(500))  # 200
print(discount_100(500))  # 400

# Самостоятельные проверки:
discount_0 = make_discount(0)
print(discount_0(500))    # 500 (Ожидается: 500)

# Граничные цены для discount_100 (на 1 тенге ниже и выше скидки 100):
print(discount_100(99))   # 0 (Ожидается 0, так как 99 - 100 < 0)
print(discount_100(101))  # 1 (Ожидается 1, так как 101 - 100 = 1)

# ==========================================
# Задание 4. Один тест функции
# ==========================================

def check_case(function, value, expected):
    actual = function(value)
    return actual == expected

# Правильная функция:
def ekeb_price(price):
    if price >= 1000:
        return price - 100
    return price

print(check_case(ekeb_price, 999, 999))   # True
print(check_case(ekeb_price, 1000, 900))  # True
print(check_case(ekeb_price, 1001, 901))  # True

# Ошибочная функция:
def wrong_price(price):
    return price - 100

print(check_case(wrong_price, 999, 999))   # False (Ошибку нашли!)
print(check_case(wrong_price, 1000, 900))  # True
print(check_case(wrong_price, 1001, 901))  # True

# Дополнительные проверки из задания:
print(check_case(ekeb_price, 0, 0))          # True (Проверка ekeb_price при цене 0)
print(check_case(discount_100, 250, 150))    # True (Проверка discount_100 для цены 250 и expected=150)

