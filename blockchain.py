import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Создание блока генезиса
        self.new_block(previous_hash=1, proof=100)
        
 
    def new_block(self, proof, previous_hash=None):
        """
        Создание нового блока в блокчейне
 
        :param proof: <int> Доказательства проведенной работы
        :param previous_hash: (Опционально) хеш предыдущего блока
        :return: <dict> Новый блок
        """
 
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
 
        # Перезагрузка текущего списка транзакций
        self.current_transactions = []
 
        self.chain.append(block)
        return block


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
        """
        Создает хэш SHA-256 блока
 
        :param block: <dict> Блок
        :return: <str>
        """
 
        # Мы должны убедиться в том, что словарь упорядочен, иначе у нас будут непоследовательные хеши
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
 
    @property
    def last_block(self):
        # Возвращает последний блок в цепочке
        return self.chain[-1]