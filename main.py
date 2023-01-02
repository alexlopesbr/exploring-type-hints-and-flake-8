from constants import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE
from detailed_statistics import DetailedStatistics
from factory_queue import FactoryQueue
from resumed_statistics import ResumedStatistics


priority_queue = FactoryQueue.get_queue(PRIORITY_QUEUE_TYPE)
print(priority_queue.statistics(ResumedStatistics('01-01-23', 10)))

normal_queue = FactoryQueue.get_queue(NORMAL_QUEUE_TYPE)
print(normal_queue.statistics(ResumedStatistics('01-01-23', 10)))
