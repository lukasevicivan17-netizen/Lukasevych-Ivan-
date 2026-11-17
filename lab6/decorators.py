def abs_decorator(func):
  """Декоратор для варіанта 18: повертає абсолютне значення результату (abs)"""

  def wrapper(*args, **kwargs):
    # Викликаємо оригінальну функцію
    result = func(*args, **kwargs)
    print(f"[ДЕКОРАТОР] Отримано результат до обробки: {result}")

    # Застосовуємо abs() і повертаємо результат
    return abs(result)

  return wrapper
