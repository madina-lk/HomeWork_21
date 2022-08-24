from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items_d):
        self._items = items_d

    @property
    def capacity(self):
        return self._capacity

    def get_free_space(self, title: str) -> int:
        return self.capacity - self.items.get(title, 0)

    @property
    def get_unique_items_count(self):
        return len(self.items)

    @abstractmethod
    def add(self, title, quantity):
        pass

    @abstractmethod
    def remove(self, title, quantity):
        pass

