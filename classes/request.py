

class Request:

    def __init__(self, storage_list: str):
        self.storage_list = storage_list.split()

        self.from_storage = self.storage_list[5]
        self.to = self.storage_list[7]
        self.amount: int = self.storage_list[2]
        self.product = self.storage_list[3]

    def check_input_text(self, input_text):
        if input_text.from_storage is None or input_text.from_storage != 'склад':
            return 'Неверно указано, откуда брать товар. Рекомендуется указать "склад"'
        if input_text.to is None or input_text.to != 'магазин':
            return 'Неверно указано, куда везти товар. Рекомендуется указать "магазин"'
        if input_text.amount is None:
            return 'Неверно указано количество товара. Пожалуйста, перепроверьте.'
        if input_text.product is None:
            return 'Неверно указан тип товара. Пожалуйста, перепроверьте.'


        #Курьер забирает 3 томаты из склад в магазин