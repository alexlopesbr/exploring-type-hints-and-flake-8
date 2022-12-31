from base_queue import BaseQueue

class PriorityQueue(BaseQueue):
    def key_generate(self) -> None:
        self.actual_key = f'PQ-{self.code}'

    def update_queue(self) -> None:
        self.reset_queue()
        self.key_generate()
        self.queue.append(self.actual_key)
    def call_client(self, ticket_window:int) -> str:
        actual_customer:str = self.queue.pop(0)
        self.customers_served.append(actual_customer)
        return f'Cliente atual: {actual_customer} dirija-se ao caixa {ticket_window}'

    def statistics(self, day:str, agency:int, flag:str) -> dict:
        if flag != 'detailed':
            estatistic = {f'{agency}-{day}': len(self.customers_served)}
        else:
            estatistic = {}
            estatistic['day'] = day
            estatistic['agency'] = agency
            estatistic['customers_served'] = self.customers_served
            estatistic['customers_served_count'] = len(self.customers_served)
        return estatistic
