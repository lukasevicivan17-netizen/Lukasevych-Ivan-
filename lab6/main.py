from decorators import abs_decorator
from functions import calculate_negative_balance


# Чіпляємо наш декоратор до функції через собачку @
@abs_decorator
def my_func():
  return calculate_negative_balance()


def main():
  print("=== ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №6 (Варіант 18) ==_\n")

  # Викликаємо задекоровану функцію
  final_result = my_func()

  print(f"\n[РЕЗУЛЬТАТ] Остаточне значення після декоратора abs(): {final_result}")


if __name__ == "__main__":
  main()