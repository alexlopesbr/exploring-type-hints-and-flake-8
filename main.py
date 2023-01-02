from constants import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE
from detailed_statistics import DetailedStatistics
from factory_queue import FactoryQueue
from resumed_statistics import ResumedStatistics

normal_queue = FactoryQueue.get_queue(NORMAL_QUEUE_TYPE)
normal_queue.update_queue()
print(normal_queue.call_client(4))

priority_queue = FactoryQueue.get_queue(PRIORITY_QUEUE_TYPE)
priority_queue.update_queue()
print(priority_queue.call_client(1))

normal_queue = FactoryQueue.get_queue(PRIORITY_QUEUE_TYPE)
print(normal_queue.statistics(ResumedStatistics(120, '01/01/23')))
