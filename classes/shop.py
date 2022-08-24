
from classes.storage import Storage


class Shop(Storage):
    def __init__(self):
        """
        Конструктор класса Shop
        """
        self._items = {}
        self._capacity = 20

    def _check_item(self, title: str):
        """
        Проверка наличия товара в items
        :param title:
        :return:
        """
        return title in self.items

    def add(self, title: str, quantity: int):
        """
        Метод увеличивает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        if self.get_free_space(title=title) >= quantity and self.get_unique_items_count < 5:
            self.items[title] = self.items.get(title, 0) + quantity
        else:
            return "Недостаточно места для добавления товара"

    def remove(self, title: str, quantity: int):
        """
        Метод уменьшает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        if self._check_item(title) is None:
            return "Товар с таким названием не найден"

        current_qnt = self.items.get(title)
        if current_qnt - quantity < 0:
            return "Превышен лимит для отгрузки товара в магазин"

        self.items[title] = current_qnt - quantity
