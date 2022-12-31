class BaseQueue:
    code:int = 0
    queue:list = []
    customers_served:list = []
    actual_key:str = ''

    def reset_queue(self) -> None:
        self.code += 1 if self.code < 100 else 0
