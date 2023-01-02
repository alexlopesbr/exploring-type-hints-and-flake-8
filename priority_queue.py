from typing import Dict, List, Union

from base_queue import BaseQueue
from constants import PRIORITY_QUEUE_CODE
from detailed_statistics import DetailedStatistics
from resumed_statistics import ResumedStatistics

Classes = Union[DetailedStatistics, ResumedStatistics]

class PriorityQueue(BaseQueue):
    def key_generate(self) -> None:
        self.actual_key = f'{PRIORITY_QUEUE_CODE}-{self.code}'

    def call_client(self, ticket_window:int) -> str:
        actual_customer:str = self.queue.pop(0)
        self.customers_served.append(actual_customer)
        return f'Cliente atual: {actual_customer} dirija-se ao caixa {ticket_window}'

    def statistics(self, return_statistic:Classes) -> dict:
        return return_statistic.run_statistics(self.customers_served)
