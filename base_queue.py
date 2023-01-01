import abc

from constants import MAX_QUEUE_SIZE


class BaseQueue(metaclass=abc.ABCMeta):
    code:int = 0
    queue:list = []
    customers_served:list = []
    actual_key:str = ''

    def reset_queue(self) -> None:
        self.code += 1 if self.code < MAX_QUEUE_SIZE else 0

    def insert_customer(self) -> None:
        self.queue.append(self.actual_key)

    def update_queue(self):
        self.reset_queue()
        self.key_generate()
        self.insert_customer()

    @abc.abstractmethod
    def key_generate(self):
        ...

    @abc.abstractmethod
    def call_client(self, ticket_window:int):
        ...
