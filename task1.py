def caching_fibonacci():
    # Створюємо порожній словник для зберігання обчислених значень чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Для значень n <= 0 повертаємо 0
        if n <= 0:
            return 0
        # Для n == 1 повертаємо 1
        if n == 1:
            return 1
        # Якщо значення для n вже обчислено та збережено в cache, повертаємо його
        if n in cache:
            return cache[n]
        # Рекурсивно обчислюємо n-те число Фібоначчі, зберігаємо результат у cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))  
    print(fib(15))  
