class Task:
    def __init__(self, description):
        self.description = description

    def execute(self):
        raise NotImplementedError("Execute method must be implemented by subclasses.")
