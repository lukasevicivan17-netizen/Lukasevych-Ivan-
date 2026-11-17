# 200 інгредієнтів та 50 зілля
INGREDIENTS = [f"Трава_{i}" for i in range(1, 201)]
POTIONS = {f"Зілля_{i}": i * 15 for i in range(1, 51)}

# Простий базовий рецепт для тесту крафту
RECIPES = {(INGREDIENTS[0], INGREDIENTS[1]): list(POTIONS.keys())[0]}