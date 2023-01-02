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

    def statistics(self, day:str, agency:int, return_statistic) -> dict:
        statistic = return_statistic(day, agency)

        return statistic.run_statistics(self.customers_served)
