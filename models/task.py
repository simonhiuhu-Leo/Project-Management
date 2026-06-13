class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete_task(self):
        self.completed = True

    def to_dict(self):
        return {
            "name": self.name,
            "completed": self.completed
        }