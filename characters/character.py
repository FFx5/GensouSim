import random

from activities.activity import ACTIVITIES
from characters.needs import Needs


class Character:
    def __init__(self, name, location=None, activity_preferences=None):
        self.name = name
        self.location = location
        self.activity = "Idle"
        self.activity_preferences = activity_preferences or {}
        self.activity_start_time = None
        self.activity_end_time = None
        self.needs = Needs()
        self.last_needs_update = None
        self.last_activity_weights = {}

    def choose_activity(self, current_time):
        """Choose an activity based on preferences and current needs."""

        activities = list(self.activity_preferences.keys())
        base_weights = list(self.activity_preferences.values())

        adjusted_weights = []

        for activity_name, base_weight in zip(
            activities,
            base_weights
        ):
            activity_definition = ACTIVITIES[activity_name]

            energy_multiplier = (
                activity_definition.get_energy_multiplier(
                    self.needs.energy
                )
            )

            hunger_multiplier = (
                activity_definition.get_hunger_multiplier(
                    self.needs.hunger
                )
            )

            adjusted_weight = (
                base_weight
                * energy_multiplier
                * hunger_multiplier
            )

            adjusted_weights.append(adjusted_weight)

        if self.needs.energy <= 0:
            self.activity = "Resting"
        else:
            self.activity = random.choices(
                activities,
                weights=adjusted_weights,
                k=1
            )[0]

        activity_definition = ACTIVITIES[self.activity]

        self.activity_start_time = current_time
        self.activity_end_time = (
            current_time + activity_definition.get_duration()
        )

        self.last_activity_weights = self.get_activity_weights()

    def get_activity_weights(self):
        """Return the current adjusted selection weight for each activity."""

        weights = {}

        for activity_name, base_weight in self.activity_preferences.items():
            activity_definition = ACTIVITIES[activity_name]

            energy_multiplier = (
                activity_definition.get_energy_multiplier(
                    self.needs.energy
                )
            )

            hunger_multiplier = (
                activity_definition.get_hunger_multiplier(
                    self.needs.hunger
                )
            )

            weights[activity_name] = (
                base_weight
                * energy_multiplier
                * hunger_multiplier
            )

        return weights

    def should_reconsider_activity(self):
        """Return whether the character should reconsider their current activity."""

        current_weights = self.get_activity_weights()

        current_weight = current_weights.get(self.activity, 0)

        if current_weight <= 0:
            return True

        best_activity = max(
            current_weights,
            key=current_weights.get
        )

        best_weight = current_weights[best_activity]

        if best_activity == self.activity:
            return False

        return best_weight >= current_weight * 1.5

    def update_needs(self, current_time):
        """Update the character's needs based on elapsed simulation time."""

        if self.last_needs_update is None:
            self.last_needs_update = current_time
            return

        elapsed_seconds = (
            current_time - self.last_needs_update
        ).total_seconds()

        elapsed_hours = elapsed_seconds / 3600

        if self.activity in ACTIVITIES:
            activity_definition = ACTIVITIES[self.activity]

            energy_change = (
                activity_definition.energy_change_per_hour
                * elapsed_hours
            )

            self.needs.energy += energy_change

            self.needs.energy = max(
                0,
                min(100, self.needs.energy)
            )

            hunger_change = (
                activity_definition.hunger_change_per_hour
                * elapsed_hours
            )

            self.needs.hunger += hunger_change

            self.needs.hunger = max(
                0,
                min(100, self.needs.hunger)
            )

        self.needs.update(elapsed_hours)

        self.last_needs_update = current_time

    def update(self, current_time):
        """Update the character's state for the current simulation time."""

        self.update_needs(current_time)

        activity_changed = False

        if (
            self.activity_end_time is None
            or current_time >= self.activity_end_time
            or self.should_reconsider_activity()
        ):
            self.choose_activity(current_time)
            activity_changed = True

        return activity_changed