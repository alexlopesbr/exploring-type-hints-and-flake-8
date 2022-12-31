class NormalQueue:
    code:int = 0
    queue:list = []
    customers_served:list = []
    actual_key:str = ''

    def key_generate(self) -> None:
        self.actual_key = f'NQ-{self.code}'

    def reset_queue(self) -> None:
        self.code += 1 if self.code < 100 else 0

    def update_queue(self) -> None:
        self.reset_queue()
        self.key_generate()
        self.queue.append(self.actual_key)

    def call_client(self, ticket_window:int) -> str:
        actual_customer:str = self.queue.pop(0)
        self.customers_served.append(actual_customer)
        return f'Cliente atual: {actual_customer} dirija-se ao caixa {ticket_window}'
