from base_queue import BaseQueue


class NormalQueue(BaseQueue):
    def key_generate(self) -> None:
        self.actual_key = f'NQ-{self.code}'

    def call_client(self, ticket_window:int) -> str:
        actual_customer:str = self.queue.pop(0)
        self.customers_served.append(actual_customer)
        return f'Cliente atual: {actual_customer} dirija-se ao caixa {ticket_window}'
