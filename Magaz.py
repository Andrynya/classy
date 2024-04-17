class Store():
    def __init__(self, name, addres):
        self.name = name
        self.addres = addres
        self.items = {}

    def add_items(self, item_name, price):
        self.items[item_name] = price
        print(f"{item_name} добавлен в ассортимент магазина {self.name}.")

    def del_items(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} удалён из ассортимента магазина {self.name}.")

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар {item_name} обновлена")
        else:
            print(f"{item_name} отсутствует в ассортименте магазина {self.name}")


store1 = Store("Первый","Ул. Волорадского, д.37")
store2 = Store("Второй","Ул. Ленина, д.87")
store3 = Store("Третий","Ул. Петровская, д.35")


store1.add_items("Лимонад", 50)
store1.add_items("Хлеб", 20)
store1.add_items("Жвачка", 14)

store2.add_items("Ручка", 50)
store2.add_items("Карандаш", 10)
store2.add_items("Линейка", 15)

store3.add_items("Шапка", 300)
store3.add_items("Шарф", 450)
store3.add_items("Носки", 100)

magaz = store1
magaz.add_items("Пиво", 79)
print(magaz.get_item_price("Пиво"))
magaz.update_item_price("Пиво", 66)
print(magaz.get_item_price("Пиво"))
magaz.del_items("Пиво")
print(magaz.get_item_price("Пиво"))
