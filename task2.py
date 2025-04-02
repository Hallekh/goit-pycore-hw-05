import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз шукає числа з опціональним мінусом, що містять десяткову крапку, і перед якими та після яких є пробіл.
    pattern = r'(?<=\s)(-?\d+\.\d+)(?=\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group(0))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальну суму чисел (доходу) з тексту,
    використовуючи задану функцію-генератор для пошуку дійсних чисел.
    """
    return sum(func(text))

if __name__ == "__main__":
    text = ("Загальний дохід працівника складається з декількох частин: "
            " 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
