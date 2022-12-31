from normal_queue import NormalQueue
from priority_queue import PriorityQueue


normal_queue = NormalQueue()
normal_queue.update_queue()
normal_queue.update_queue()
normal_queue.update_queue()

print(normal_queue.call_client(5))
print(normal_queue.call_client(10))
print(normal_queue.call_client(7))

priority_queue = PriorityQueue()
priority_queue.update_queue()
priority_queue.update_queue()
priority_queue.update_queue()

print(priority_queue.call_client(9))
print(priority_queue.statistics('2022-12-31', 44, 'detailed2'))
