

class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title: str, quantity: int):
        if self.get_free_space(title=title) >= quantity:
            self.items[title] = self.items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int):
        if self.items.get(title, 0) - quantity > 0:
            self.items[title] = self.items.get(title, 0) - quantity






my_store = Store()
my_shop = Shop()

my_store.add(title='Сушеные питоны', quantity=10)
my_store.add(title='Сушеные питоны', quantity=20)
my_store.add(title='Сушеные питоны', quantity=20)
my_store.add(title='Сушеные питоны', quantity=20)
my_store.add(title='Сушеные питоны', quantity=50)
my_store.add(title='Свежие питоны', quantity=5)
my_store.add(title='Сырые питоны', quantity=6)

my_shop.add(title='Сушеные питоны', quantity=10)
my_shop.add(title='Сушеные питоны', quantity=3)
my_shop.add(title='Сушеные питоны', quantity=2)
my_shop.add(title='Сушеные питоны', quantity=2)
my_shop.add(title='Сушеные питоны', quantity=5)
my_shop.add(title='Свежие питоны', quantity=5)
my_shop.add(title='Сырые питоны', quantity=2)

my_req = Request()

print(my_store.items)
print(my_shop.items)
# print(my_store.get_unique_items_count())
# print(my_store.get_free_space())