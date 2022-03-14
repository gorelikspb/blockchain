class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        
    def new_block(self):
        # Создает новый блок и вносит его в цепь
        pass
    
  
    def new_transaction(self, sender, recipient, amount):
        """
        Направляет новую транзакцию в следующий блок
 
        :param sender: <str> Адрес отправителя
        :param recipient: <str> Адрес получателя
        :param amount: <int> Сумма
        :return: <int> Индекс блока, который будет хранить эту транзакцию
        """
 
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
 
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        # Хеширует блок
        pass
 
    @property
    def last_block(self):
        # Возвращает последний блок в цепочке
        pass