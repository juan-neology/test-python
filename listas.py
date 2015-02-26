__author__ = 'juan'
from collections import deque


queue = deque(["uno", "dos", "tres"])
queue.append("cuatro")
queue.append("cinco")


print (queue)
queue.popleft()
print (queue)

