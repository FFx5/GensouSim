import random
from datetime import timedelta

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
            "connections": {}
        }

    def connect_locations(self, first_location, second_location, travel_time=15):
        """Create a two-way connection with a travel time in minutes."""

        duration = timedelta(minutes=travel_time)

        self.locations[first_location]["connections"][second_location] = duration
        self.locations[second_location]["connections"][first_location] = duration

    def add_character(self, character):
        self.characters[character.name] = character

    def move_character(self, character):
        """Begin travel to a random connected location."""

        if character.location not in self.locations:
            return False

        connections = self.locations[character.location]["connections"]

        if not connections:
            return False

        destination = random.choice(list(connections.keys()))
        travel_time = connections[destination]

        character.travel_destination = destination
        character.travel_end_time = self.current_time + travel_time
        character.activity = "Traveling"
        character.activity_start_time = self.current_time
        character.activity_end_time = character.travel_end_time

        print(
            f"[{self.current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
            f"{character.name} began traveling from "
            f"{character.location} to {destination}."
        )

        return True

    def complete_travel(self, character):
        """Complete a character's current journey."""

        if character.travel_destination is None:
            return False

        previous_location = character.location
        character.location = character.travel_destination
        character.travel_destination = None
        character.travel_end_time = None
        character.activity = "Idle"
        character.activity_start_time = self.current_time
        character.activity_end_time = None

        print(
            f"[{self.current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
            f"{character.name} arrived at {character.location} "
            f"from {previous_location}."
        )

        return True

    def tick(self):
        """Update the simulation."""

        current_time = self.clock.tick()

        for character in self.characters.values():
            if (
                character.activity == "Traveling"
                and character.travel_end_time is not None
                and current_time >= character.travel_end_time
            ):
                self.complete_travel(character)

            activity_completed = (
                character.activity_end_time is not None
                and current_time >= character.activity_end_time
            )

            if (
                activity_completed
                and character.activity in {"Wandering", "Exploring"}
            ):
                if not self.move_character(character):
                    character.activity_end_time = current_time

            activity_changed = character.update(current_time)

            if activity_changed:
                print(
                    f"[{current_time.strftime('%Y-%m-%d %H:%M:%S JST')}] "
                    f"{character.name} is now "
                    f"{character.activity.lower()} "
                    f"at {character.location}."
                )
