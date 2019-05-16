class Queue:
  def __init__(self, start=None):
    if start is None:
      self.queue = []
    else:
      self.queue = [start]
  
  def __len__(self):
    return len(self.queue)
  
  def enqueue(self, value):
    self.queue.append(value)
  
  def dequeue(self):
    if len(self) > 0:
      return self.queue.pop(0)
    else:
      return None
