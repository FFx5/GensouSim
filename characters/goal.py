class Goal:
    def __init__(
        self,
        name,
        description,
        priority=1,
        preferred_activities=None,
        condition=None,
        repeatable=False
    ):
        self.name = name
        self.description = description
        self.priority = priority
        self.preferred_activities = preferred_activities or []
        self.condition = condition
        self.repeatable = repeatable
        self.completed = False

    def complete(self):
        """Mark the goal as completed."""

        self.completed = True

    def check_completion(self, character, world=None):
        """Check whether the goal's condition has been satisfied."""

        if self.completed:
            return True

        if self.condition is not None and self.condition(character, world):
            self.complete()

        return self.completed
