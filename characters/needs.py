class Needs:
    def __init__(self):
        self.energy = 100.0
        self.hunger = 0.0

    def update(self, elapsed_hours):
        """Update needs based on elapsed simulation time."""

        self.hunger += 5 * elapsed_hours

        self.hunger = max(
            0,
            min(100, self.hunger)
        )