from collections import deque

class Queue:
  def __init__(self, start=None):
    if start is None:
      self.data = deque()
    else:
      self.data = deque([start])
  
  def __len__(self):
    return len(self.data)
  
  def enqueue(self, value):
    self.data.append(value)
  
  def dequeue(self):
    if len(self) > 0:
      return self.data.popleft()
    else:
      return None
