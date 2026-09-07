import random

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

    def move_character(self, character):
        """Move a character to a random connected location."""

        if character.location not in self.locations:
            return False

        connections = list(
            self.locations[character.location]["connections"]
        )

        if not connections:
            return False

        previous_location = character.location
        character.location = random.choice(connections)

        print(
            f"[{self.current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
            f"{character.name} traveled from "
            f"{previous_location} to {character.location}."
        )

        return True

    def tick(self):
        """Update the simulation."""

        current_time = self.clock.tick()

        for character in self.characters.values():
            activity_completed = (
                character.activity_end_time is not None
                and current_time >= character.activity_end_time
            )

            if activity_completed and character.activity in {
                "Wandering",
                "Exploring"
            }:
                self.move_character(character)

            activity_changed = character.update(current_time)

            if activity_changed:
                print(
                    f"[{current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
                    f"{character.name} is now "
                    f"{character.activity.lower()} "
                    f"at {character.location}."
                )
