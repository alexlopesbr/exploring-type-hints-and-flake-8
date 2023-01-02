from typing import Dict, Union, List

from base_queue import BaseQueue
from constants import PRIORITY_QUEUE_CODE


class PriorityQueue(BaseQueue):
    def key_generate(self) -> None:
        self.actual_key = f'{PRIORITY_QUEUE_CODE}-{self.code}'

    def call_client(self, ticket_window:int) -> str:
        actual_customer:str = self.queue.pop(0)
        self.customers_served.append(actual_customer)
        return f'Cliente atual: {actual_customer} dirija-se ao caixa {ticket_window}'

    def statistics(self, day:str, agency:int, flag:str) -> dict:
        estatistic:Dict[str, Union[List[str], str, int]] = {}

        if flag != 'detailed':
            estatistic[f'{agency}-{day}'] = len(self.customers_served)
        else:
            estatistic['day'] = day
            estatistic['agency'] = agency
            estatistic['customers_served'] = self.customers_served
            estatistic['customers_served_count'] = len(self.customers_served)
        return estatistic
