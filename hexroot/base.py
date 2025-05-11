class BaseBot:
    def __init__(self, name):
        self.name = name

    def start(self):
        raise NotImplementedError("Start method must be implemented by subclasses.")
