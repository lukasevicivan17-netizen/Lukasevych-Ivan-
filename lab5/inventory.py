class Inventory:

  def __init__(self):
    self.ingredients = {}  # макс 25 слотів, стак 25
    self.potions = {}  # макс 10 слотів, стак 10

  def add_item(self, type_item, name, count=1):
    try:
      storage = self.ingredients if type_item == "ing" else self.potions
      max_slots = 25 if type_item == "ing" else 10
      max_stack = 25 if type_item == "ing" else 10

      if name not in storage:
        if len(storage) >= max_slots:
          raise ValueError("Немає вільних слотів!")
        storage[name] = 0

      if storage[name] + count > max_stack:
        raise ValueError("Перевищено ліміт стаку в слоті!")

      storage[name] += count
    except ValueError as e:
      print(f"[Помилка інвентарю]: {e}")

  def craft(self, ing1, ing2, result_potion):
    try:
      if (
          self.ingredients.get(ing1, 0) < 1
          or self.ingredients.get(ing2, 0) < 1
      ):
        raise ValueError("Недостатньо інгредієнтів для крафту!")

      # Витрачаємо інгредієнти
      self.ingredients[ing1] -= 1
      self.ingredients[ing2] -= 1
      if self.ingredients[ing1] == 0:
        del self.ingredients[ing1]
      if self.ingredients[ing2] == 0:
        del self.ingredients[ing2]

      # Додаємо зілля
      self.add_item("potion", result_potion, 1)
      print(f"[Успіх] Зварено: {result_potion}")
    except ValueError as e:
      print(f"[Помилка крафту]: {e}")