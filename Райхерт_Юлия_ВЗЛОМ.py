print("================================")
print("     СИСТЕМА БЕЗОПАСНОСТИ")
print("================================")


while True:
    print("\n1 — Начать игру")
    print("0 — Выйти")

    choice = input("Выберите действие: ")

    if choice == "0":
        print("Выход из программы.")
        break

    elif choice == "1":

        # ==============================
        # УРОВЕНЬ 1 — КОД ДОСТУПА
        # ==============================

        print("\n================================")
        print("      УРОВЕНЬ 1: КОД ДОСТУПА")
        print("================================")

        secret = 37
        success = False

        for attempt in range(1, 4):
            print("\nПопытка", attempt, "/ 3")

            while True:
                try:
                    number = int(input("Введите число от 1 до 999999: "))

                    if 1 <= number <= 999999:
                        break
                    else:
                        print("Ошибка! Введите число от 1 до 999999.")

                except ValueError:
                    print("Ошибка! Нужно ввести целое число.")

            if number == secret:
                print("КОД ВЕРНЫЙ!")
                print("УРОВЕНЬ 1 ПРОЙДЕН!")
                success = True
                break

            elif number < secret:
                print("Загаданное число больше.")

            else:
                print("Загаданное число меньше.")

        if not success:
            print("\nТРЕВОГА!")
            print("Система заблокирована. Попытки исчерпаны.")
            continue


        # ==============================
        # УРОВЕНЬ 2 — ПЕРЕХВАТ СООБЩЕНИЯ
        # ==============================

        print("\n================================")
        print("   УРОВЕНЬ 2: ПЕРЕХВАТ СООБЩЕНИЯ")
        print("================================")

        numbers = [7, 14, 5, 10, 21, 8, 28, 3, 35, 11]
        total = 0

        print("Перехваченное сообщение:")

        for number in numbers:
            print(number, end=" ")

            if number % 7 == 0:
                total = total + number

        print("\n")

        print("Найдите сумму чисел, которые делятся на 7 без остатка.")

        while True:
            try:
                answer = int(input("Введите сумму: "))

                if answer >= 0:
                    break
                else:
                    print("Введите неотрицательное число.")

            except ValueError:
                print("Ошибка! Введите целое число.")

        if answer == total:
            print("СУММА ВЕРНА!")
            print("УРОВЕНЬ 2 ПРОЙДЕН!")

        else:
            print("Неверный ответ.")
            print("Правильная сумма:", total)
            print("ТРЕВОГА! Система заблокирована.")
            continue


        # ==============================
        # УРОВЕНЬ 3 — ПОСЛЕДНИЙ ЗАМОК
        # ==============================

        print("\n================================")
        print("       УРОВЕНЬ 3: ПОСЛЕДНИЙ ЗАМОК")
        print("================================")

        while True:
            try:
                number = int(input("Введите положительное число: "))

                if number > 0:
                    break
                else:
                    print("Число должно быть положительным.")

            except ValueError:
                print("Ошибка! Введите целое число.")

        # Сохраняем число для анализа
        temp = number

        count = 0
        digit_sum = 0
        even_count = 0
        odd_count = 0
        maximum = 0
        minimum = 9

        # Анализ цифр через while
        while temp > 0:
            digit = temp % 10

            count = count + 1
            digit_sum = digit_sum + digit

            if digit % 2 == 0:
                even_count = even_count + 1
            else:
                odd_count = odd_count + 1

            if digit > maximum:
                maximum = digit

            if digit < minimum:
                minimum = digit

            temp = temp // 10

        print("\nРЕЗУЛЬТАТ АНАЛИЗА:")
        print("Количество цифр:", count)
        print("Сумма цифр:", digit_sum)
        print("Чётных цифр:", even_count)
        print("Нечётных цифр:", odd_count)
        print("Наибольшая цифра:", maximum)
        print("Наименьшая цифра:", minimum)

        print("\nУРОВЕНЬ 3 ПРОЙДЕН!")

        # ==============================
        # ФИНАЛ
        # ==============================

        print("\n================================")
        print("        СЕЙФ ВЗЛОМАН!")
        print("================================")
        print("Поздравляем, агент.")
        print("Доступ к системе получен.")

    else:
        print("Ошибка! Выберите 1 или 0.")