from typing import Union

from constants import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE
from normal_queue import NormalQueue
from priority_queue import PriorityQueue


class FactoryQueue:
    @staticmethod
    def get_queue(queue_type) -> Union[NormalQueue, PriorityQueue]:
        if queue_type == NORMAL_QUEUE_TYPE:
            return NormalQueue()
        elif queue_type == PRIORITY_QUEUE_TYPE:
            return PriorityQueue()
        else:
            raise NotImplementedError('Type of queue is not supported')
