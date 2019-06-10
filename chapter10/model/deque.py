from collections import deque

q = deque(range(5))
q.append(5)
q.appendleft(6)

print(q)
q.pop()
q.popleft()
q.rotate(3)  # 左移
print(q)
q.rotate(-1)
print(q)
