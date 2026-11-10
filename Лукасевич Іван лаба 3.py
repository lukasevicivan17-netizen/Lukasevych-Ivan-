class Store:
    def __init__(self):
        # Каталог товарів
        self.catalog = [
            {"id": 1, "name": "Mouse", "price": 250.50, "stock": 10},
            {"id": 2, "name": "Keyboard", "price": 700.00, "stock": 5},
            {"id": 3, "name": "Headset", "price": 1200.25, "stock": 3}
        ]
        self.cart = []

    # 1. Переглянути каталог (лямбда для виводу ціни)
    def show_catalog(self):
        print("\n--- КАТАЛОГ ---")
        format_price = lambda p: f"{p:.2f}грн"
        for p in self.catalog:
            print(f"{p['id']}. {p['name']} - {format_price(p['price'])} (Залишок: {p['stock']})")

    # 2. Додати в кошик (лямбда для пошуку)
    def add_to_cart(self, product_id):
        find_product = lambda item_id: next((p for p in self.catalog if p["id"] == item_id), None)
        item = find_product(product_id)

        if item and item["stock"] > 0:
            self.cart.append(item)
            print("Товар додано до кошика!")
        else:
            print("Товар не знайдено або немає в наявності!")

    # 3. Видалити з кошика (лямбда для пошуку)
    def remove_from_cart(self, product_id):
        find_in_cart = lambda item_id: next((p for p in self.cart if p["id"] == item_id), None)
        item = find_in_cart(product_id)

        if item:
            self.cart.remove(item)
            print("Товар видалено з кошика!")
        else:
            print("У кошику немає такого товару з цим ID!")

    # Перегляд кошика та купівля
    def show_cart_and_checkout(self, is_checkout=False):
        if not self.cart:
            print("\nКошик порожній.")
            return

        print("\n--- КОШИК ---")
        total = 0
        for item in self.cart:
            print(f"{item['name']} - {item['price']:.2f}грн")
            total += item['price']

        # Лямбда для виводу загальної суми
        print_total = lambda sum_val: print(f"Всього до сплати: {sum_val:.2f}грн")
        print_total(total)

        if is_checkout:
            # Зменшуємо залишки в каталозі
            for cart_item in self.cart:
                for cat_item in self.catalog:
                    if cat_item["id"] == cart_item["id"]:
                        cat_item["stock"] -= 1
            self.cart.clear()
            print("Замовлення успішно оформлено!")

    # 4. Адмін-панель (перегляд залишків)
    def admin_panel(self):
        password = input("Введіть пароль адміна (admin): ")
        if password == "admin":
            print("\n--- ЗАЛИШКИ НА СКЛАДІ ---")
            for p in self.catalog:
                print(f"ID: {p['id']} | Назва: {p['name']} | Залишок: {p['stock']} шт.")
        else:
            print("Невірний пароль!")


# Головна функція програми
if __name__ == "__main__":
    store = Store()

    while True:
        print("\n1. Каталог | 2. Додати в кошик | 3. Кошик | 4. Видалити | 5. Купити | 6. Адмін | 0. Вихід")
        choice = input("Виберіть дію: ")

        if choice == '1':
            store.show_catalog()
        elif choice == '2':
            store.show_catalog()
            pid = int(input("ID товару: "))
            store.add_to_cart(pid)
        elif choice == '3':
            store.show_cart_and_checkout(False)
        elif choice == '4':
            store.show_cart_and_checkout(False)
            pid = int(input("ID для видалення: "))
            store.remove_from_cart(pid)
        elif choice == '5':
            store.show_cart_and_checkout(True)
        elif choice == '6':
            store.admin_panel()
        elif choice == '0':
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз!")