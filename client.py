class ChaseLevDeque:
    """
    Chase-Lev Work-Stealing Deque.
    Owner worker accesses bottom without contention; idle workers steal from top.
    """
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.bottom = 0
        self.top = 0

    def push_bottom(self, task):
        b = self.bottom
        self.buffer[b % self.capacity] = task
        self.bottom = b + 1

    def pop_bottom(self):
        b = self.bottom - 1
        self.bottom = b
        t = self.top
        if b < t:
            self.bottom = t
            return None
        task = self.buffer[b % self.capacity]
        if b > t:
            return task
        self.bottom = t + 1
        self.top = t + 1
        return task

    def steal(self):
        t = self.top
        b = self.bottom
        if t >= b:
            return None
        task = self.buffer[t % self.capacity]
        self.top = t + 1
        return task
