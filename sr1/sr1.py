import math


def calculator():

    """Інтерактивний калькулятор з підтримкою +, -, *, /, //, %, **, !"""

    print("=== Калькулятор ===")

    print("Введіть вираз у форматі: число оператор число (через пробіл) або для знаходження факторіалу: число оператор (через пробіл)")

    print("Введіть 'quit' для виходу, 'history' для історії")


    history = []

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() == "quit":
            break

        if user_input.lower() == "history":
                if not history:
                    print("Історія обчислень порожня.")
                else:
                    print("\n--- Історія обчислень ---")
                    for item in history:
                        print(item)
                continue

        parts = user_input.split()
        if len(parts) < 2 or len(parts) > 3:
            print("Помилка: Некоректний формат! Введіть: число оператор число або для знаходження факторіалу: число оператор")
            continue

        try:
            if len(parts) == 3:
                str_num1, operator, str_num2 = parts
                num1 = float(str_num1)
                num2 = float(str_num2)
            elif len(parts) == 2:
                str_num1, operator = parts
                num1 = float(str_num1)
                if num1 < 0:
                    raise ValueError("Число не може бути від'ємним")
                
        
            result = None

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Помилка: Ділення на нуль неможливе!")
                    continue
                result = num1 / num2
            elif operator == "//":
                if num2 == 0:
                    print("Помилка: Цілочисельне ділення на нуль неможливе!")
                    continue
                result = num1 // num2
            elif operator == "%":
                if num2 == 0:
                    print("Помилка: Ділення на нуль (остача) неможливе!")
                    continue
                result = num1 % num2
            elif operator == "**":
                result = num1**num2
            elif operator == "!":
                result = 1
                if num1 > 0:
                    for num in range(1, int(num1 + 1)):
                        result *= num
            else:
                print(f"Помилка: Непідтримуваний оператор '{operator}'!")
                print("Допустимі оператори: +, -, *, /, //, %, **")
                continue

        
            if len(parts) == 3:
                entry = f"{num1} {operator} {num2} = {result}"
                print(f"Результат: {result}")
            elif len(parts) == 2:
                entry = f"{num1} {operator} = {result}"
                print(f"Результат: {result}")

            history.append(entry)
        except ValueError as e:
            print(f"Дані введено неправильно: {e}")



def triangle():
    while(True):
        print("Дії з трикутником")
        print("Введіть значення для сторін трикутника(три числа через пробіл), для вихоу введіть: quit")
        us_input = input()
        if us_input.lower() == "quit":
            break

        el = us_input.split()
        if len(el) != 3:
            print("Неправельне введення")
            continue
        
        
        try:
            sides = (float(el[0]) , float(el[1]), float(el[2]))
            a, b, c = sides
        except ValueError:
            print("Сторони повинні бути числами!")
            continue
            
          
        if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
            print("Виберіть дію")
            print("Натисність 1 для знаходження периметру, 2 для знадження площі, 3 для знаходження площі і периметру")
            m = input()
            if m == "1":
                print(f"Периметр трикутника: {a + b + c}")
            elif m == "2":
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print(f"Площа трикутника: {area} ")
            elif m == "3":
                print(f"Периметр трикутника: {a + b + c}")
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                print(f"Площа трикутника: {area} ")
            else:
                print("Такої дії немає")
        else: 
            print("Такого трикутника неіснує!")


def my_generator(start, end):
    step = 1 if start <= end else -1
    curr = start
    while (curr <= end if step > 0 else curr >= end):
        yield curr
        curr += step

def iterator():
    print("Демонстрація Ітератора та Генератора")
    while (True):
        print("Введіть початкове та кінцеве число (через пробіл) або 'quit':")
        inp = input()
        if inp.lower() == "quit":
            break
        
        parts = inp.split()
        if len(parts) != 2:
            print("Необхідно ввести мінімум 2 числа!")
            continue
            
        try:
            start, end = int(parts[0]), int(parts[1])
            
            print("Обхід через генератор (yield):")
            for num in my_generator(start, end):
                print(num)
            print()

            print("Ручний обхід через ітератор (iter / next):")
            sample_list = [start, (start + end) // 2, end]
            it = iter(sample_list)
            print("Перший елемент:", next(it))
            print("Другий елемент:", next(it))
            print("Третій елемент:", next(it))
            
        except ValueError:
            print("Введіть коректні цілі числа!")

    
if __name__ == "__main__":
    
    while(True):

        print("Виберіть опцію")
        print( "Для того щоб ввійти в калькулятор натисніть 1, для того, щоб виконувати дії з трикутником натисніть 2, \n для виклику ітератора натисніть 3" )
        print("Для зупинки введіть: exit")
        n = input()

        if n == "1":
            calculator()
        elif n == "2":
            triangle()
        elif n == "3":
            iterator()
        elif n.lower() == "exit":
            break
        else:
            print("Такої операції немає")
