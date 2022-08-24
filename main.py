
from classes.store import Store
from classes.shop import Shop
from classes.request import Request

from config import *


def check_app():

    my_store = Store()

    my_store.add(title='томаты', quantity=10)
    my_store.add(title='томаты', quantity=20)
    my_store.add(title='огурцы', quantity=20)

    my_shop = Shop()

    my_shop.add(title='бананы', quantity=2)
    my_shop.add(title='яблоки', quantity=2)
    my_shop.add(title='сок', quantity=5)

    print(START)
    user_text = input().lower().strip()

    req = Request(user_text)

    error_text = req.check_input_text(req)
    if error_text is not None:
        print(error_text)

    my_store.remove(req.product, int(req.amount))
    my_shop.add(req.product, int(req.amount))
    print(APP_TEXT.format(amount=req.amount, product=req.product, from_storage=req.from_storage, to=req.to))

    print(RESULT_TEXT.format(obj=req.from_storage))
    for title, quantity in my_store.items.items():
        print(quantity, title)

    print(RESULT_TEXT.format(obj=req.to))
    for title, quantity in my_shop.items.items():
        print(quantity, title)


if __name__ == '__main__':
    check_app()

