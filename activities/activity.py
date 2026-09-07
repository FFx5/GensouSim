import random
from datetime import timedelta


class Activity:
    def __init__(
        self,
        name,
        minimum_duration,
        maximum_duration,
        energy_change_per_hour,
        hunger_change_per_hour,
        energy_preference,
        hunger_preference,
        allowed_locations=None
    ):
        self.name = name
        self.minimum_duration = minimum_duration
        self.maximum_duration = maximum_duration
        self.energy_change_per_hour = energy_change_per_hour
        self.hunger_change_per_hour = hunger_change_per_hour
        self.energy_preference = energy_preference
        self.hunger_preference = hunger_preference
        self.allowed_locations = allowed_locations

    def get_duration(self):
        """Return a random duration within the activity's duration range."""

        duration_minutes = random.randint(
            self.minimum_duration,
            self.maximum_duration
        )

        return timedelta(minutes=duration_minutes)

    def is_available_at(self, location):
        """Return whether the activity can be performed at the given location."""

        if self.allowed_locations is None:
            return True

        return location in self.allowed_locations

    def get_energy_multiplier(self, energy):
        """Return an activity preference multiplier based on current energy."""

        if self.name == "Resting":
            return 0.5 + ((100 - energy) / 100) * 4.5

        if energy <= 20:
            return self.energy_preference["low"]

        if energy <= 50:
            return self.energy_preference["medium"]

        return self.energy_preference["high"]

    def get_hunger_multiplier(self, hunger):
        """Return an activity preference multiplier based on current hunger."""

        if hunger <= 20:
            return self.hunger_preference["low"]

        if hunger <= 50:
            progress = (hunger - 20) / 30

            return (
                self.hunger_preference["low"]
                + (
                    self.hunger_preference["medium"]
                    - self.hunger_preference["low"]
                ) * progress
            )

        progress = (hunger - 50) / 50

        return (
            self.hunger_preference["medium"]
            + (
                self.hunger_preference["high"]
                - self.hunger_preference["medium"]
            ) * progress
        )


ACTIVITIES = {
    "Maintaining the shrine": Activity(
        "Maintaining the shrine",
        30,
        90,
        -4,
        0,
        {
            "low": 0.25,
            "medium": 0.75,
            "high": 1.0
        },
        {
            "low": 1.0,
            "medium": 0.9,
            "high": 0.7
        },
        ["Hakurei Shrine"]
    ),
    "Resting": Activity(
        "Resting",
        15,
        60,
        2,
        0,
        {
            "low": 5.0,
            "medium": 2.0,
            "high": 0.5
        },
        {
            "low": 1.0,
            "medium": 0.9,
            "high": 0.75
        }
    ),
    "Wandering": Activity(
        "Wandering",
        20,
        120,
        -3,
        0,
        {
            "low": 0.25,
            "medium": 0.75,
            "high": 1.0
        },
        {
            "low": 1.0,
            "medium": 1.0,
            "high": 1.25
        }
    ),
    "Exploring": Activity(
        "Exploring",
        60,
        240,
        0,
        -5,
        {
            "low": 0.1,
            "medium": 0.75,
            "high": 1.0
        },
        {
            "low": 1.0,
            "medium": 0.9,
            "high": 0.75
        }
    ),
    "Studying magic": Activity(
        "Studying magic",
        30,
        180,
        0,
        -3,
        {
            "low": 0.25,
            "medium": 0.75,
            "high": 1.0
        },
        {
            "low": 1.0,
            "medium": 0.8,
            "high": 0.5
        },
        ["Forest of Magic"]
    ),
    "Eating": Activity(
        "Eating",
        15,
        30,
        0,
        -20,
        {
            "low": 1.0,
            "medium": 1.0,
            "high": 1.0
        },
        {
            "low": 0.25,
            "medium": 1.0,
            "high": 4.0
        }
    )
}