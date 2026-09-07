import inspect


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

    def _condition_satisfied(self, character, world=None):
        """Return whether the goal's condition is satisfied."""

        if self.condition is None:
            return False

        signature = inspect.signature(self.condition)

        try:
            signature.bind(character, world)
        except TypeError:
            return self.condition(character)

        return self.condition(character, world)

    def check_completion(self, character, world=None):
        """Check whether the goal's condition has been satisfied."""

        if self.completed:
            if self.repeatable and not self._condition_satisfied(character, world):
                self.completed = False

            return False

        if self._condition_satisfied(character, world):
            self.complete()
            return True

        return False
