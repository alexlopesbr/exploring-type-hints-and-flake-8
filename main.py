from constants import NORMAL_QUEUE_TYPE, PRIORITY_QUEUE_TYPE
from factory_queue import FactoryQueue

normal_queue = FactoryQueue.get_queue(NORMAL_QUEUE_TYPE)
normal_queue.update_queue()
print(normal_queue.call_client(4))

priority_queue = FactoryQueue.get_queue(PRIORITY_QUEUE_TYPE)
priority_queue.update_queue()
print(priority_queue.call_client(1))
