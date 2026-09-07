class Goal:
    def __init__(self, name, description, priority=1, preferred_activities=None):
        self.name = name
        self.description = description
        self.priority = priority
        self.preferred_activities = preferred_activities or []
        self.completed = False

    def complete(self):
        """Mark the goal as completed."""

        self.completed = True
