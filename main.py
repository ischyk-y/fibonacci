def fibonacci(n):
    if n <= 0:
        return "Число має бути більше нуля"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b


n = int(input("Введіть номер числа Фібоначчі: "))
print(f"Число Фібоначчі під номером {n} дорівнює {fibonacci(n)}")

