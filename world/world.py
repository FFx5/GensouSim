from simulation.clock import SimulationClock


class World:
    def __init__(self, clock_mode="live"):
        self.clock = SimulationClock(mode=clock_mode)
        self.locations = {}
        self.characters = {}

    @property
    def current_time(self):
        """Return the current Gensokyo date and time."""
        return self.clock.current_time

    def add_location(self, name):
        self.locations[name] = {
            "name": name,
            "connections": set()
        }

    def connect_locations(self, first_location, second_location):
        """Create a two-way connection between two existing locations."""

        self.locations[first_location]["connections"].add(second_location)
        self.locations[second_location]["connections"].add(first_location)

    def add_character(self, character):
        self.characters[character.name] = character

    def tick(self):
        """Update the simulation."""

        current_time = self.clock.tick()

        for character in self.characters.values():
            activity_changed = character.update(current_time, self)

            if activity_changed:
                print(
                    f"[{current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
                    f"{character.name} is now "
                    f"{character.activity.lower()} "
                    f"at {character.location}."
                )
