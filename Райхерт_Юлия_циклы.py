# Вариант 13 — Райхерт Юлия

# 1. Числа от 1 до N
n = int(input("Введите N: "))

for i in range(1, n + 1):
    print(i)

# 2. НОД
a = int(input("Введите A: "))
b = int(input("Введите B: "))

while b != 0:
    a, b = b, a % b

print("НОД =", a)

# 3. Совершенное число
n = int(input("Введите число для проверки: "))

sum_divisors = 0

for i in range(1, n):
    if n % i == 0:
        sum_divisors += i

if sum_divisors == n:
    print("Число совершенное")
else:
    print("Число не является совершенным")