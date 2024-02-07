class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task):
        if len(self.queue) < 20:
            self.queue.append(task)
        else:
            raise ValueError("Queue is full, cannot add more tasks.")

    def extract_task(self):
        if self.queue_size == 0:
            raise IndexError("Queue is empty, cannot extract task.")
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def clear_queue(self):
        self.queue = []

    def queue_size(self):
        return len(self.queue)


task_queue = TaskQueue()
try:
    for i in range(1, 25):
        task_queue.add_task(f"Task {i}")
except ValueError as ve:
    print(ve)

print(f"Queue size: {task_queue.queue_size()}")

try:
    while not task_queue.is_empty():
        task = task_queue.extract_task()
        print(f"Extracted task: {task}")
except IndexError as ie:
    print(ie)

print(f"Queue size after extraction: {task_queue.queue_size()}")

task_queue.clear_queue()
print(f"Queue size after clearing: {task_queue.queue_size()}")
