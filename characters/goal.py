class Goal:
    def __init__(self, name, description, priority=1):
        self.name = name
        self.description = description
        self.priority = priority
        self.completed = False

    def complete(self):
        """Mark the goal as completed."""

        self.completed = True
