import random
from data import INGREDIENTS, POTIONS, RECIPES
from inventory import Inventory


def main():
  inv = Inventory()
  gold = 50
  day = 1

  while day <= 5 and gold < 500:
    print(f"\n--- День {day} | Золото: {gold} ---")

    # Щоденний бонус: +5 інгредієнтів
    for _ in range(5):
      inv.add_item("ing", random.choice(INGREDIENTS), 1)

    print("Ваші інгредієнти:", inv.ingredients)

    # Приклад крафту першого рецепта автоматично
    pair = list(RECIPES.keys())[0]
    inv.craft(pair[0], pair[1], RECIPES[pair])

    # Продаж зілля в кінці дня
    earned = sum(POTIONS[p] * count for p, count in inv.potions.items())
    gold += earned
    inv.potions.clear()
    print(f"Продано зілля на {earned монет. Загалом золота: {gold}")

    day += 1

  # Кінцівка гри
  if gold >= 500:
    print("\n🎉 ВИГРАШ! Ви заробили 500 золота!")
  else:
    print("\n💀 ПРОГРАШ! Час вийшов, а ціль не досягнута.")


if __name__ == "__main__":
  main()
