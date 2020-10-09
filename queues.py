from collections import deque  # because it is not efficient that's why we use deque
queue = deque([])  # create deque obj
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
print(queue)
if not queue:
    print("empty")
