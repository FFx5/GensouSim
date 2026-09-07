import random
from datetime import timedelta

from activities.activity import ACTIVITIES
from characters.goal import Goal
from characters.needs import Needs
from characters.relationship import Relationship


class Character:
    def __init__(self, name, location=None, activity_preferences=None, goals=None):
        self.name = name
        self.location = location
        self.activity = "Idle"
        self.activity_preferences = activity_preferences or {}
        self.goals = goals or []
        self.relationships = {}
        self.activity_start_time = None
        self.activity_end_time = None
        self.last_completed_activity = None
        self.activity_completed_this_tick = None
        self.travel_destination = None
        self.travel_end_time = None
        self.needs = Needs()
        self.last_needs_update = None
        self.last_activity_weights = {}

    def add_goal(self, goal):
        """Add the character's goal."""

        if not isinstance(goal, Goal):
            raise TypeError("goal must be a Goal instance")

        self.goals.append(goal)

    def add_relationship(self, character, value=0):
        """Set a relationship with another character."""

        if isinstance(value, Relationship):
            self.relationships[character.name] = value
        else:
            self.relationships[character.name] = Relationship(affinity=value)

    def get_relationship(self, character):
        """Return the relationship with another character."""

        return self.relationships.get(character.name, Relationship())

    def get_active_goals(self):
        """Return the character's goals that are not yet completed."""

        return [goal for goal in self.goals if not goal.completed]

    def get_goals_for_evaluation(self):
        """Return goals that should be checked for completion or reactivation."""

        return [
            goal
            for goal in self.goals
            if not goal.completed or goal.repeatable
        ]

    def choose_activity(self, current_time):
        """Choose an available activity based on preferences, needs, and goals."""

        weights = self.get_activity_weights()

        available_activities = {
            activity_name: weight
            for activity_name, weight in weights.items()
            if weight > 0
        }

        if self.needs.energy <= 0 and "Resting" in ACTIVITIES:
            self.activity = "Resting"
        else:
            activities = list(available_activities.keys())
            adjusted_weights = list(available_activities.values())

            if not activities:
                self.activity = "Idle"
                self.activity_start_time = current_time
                self.activity_end_time = None
                self.last_activity_weights = weights
                return

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

        self.last_activity_weights = weights

    def get_activity_weights(self):
        """Return current adjusted weights for activities available here."""

        weights = {}

        for activity_name, base_weight in self.activity_preferences.items():
            activity_definition = ACTIVITIES[activity_name]

            if not activity_definition.is_available_at(self.location):
                weights[activity_name] = 0
                continue

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

            goal_multiplier = 1

            for goal in self.get_active_goals():
                if activity_name in goal.preferred_activities:
                    goal_multiplier += goal.priority

            weights[activity_name] = (
                base_weight
                * energy_multiplier
                * hunger_multiplier
                * goal_multiplier
            )

        return weights

    def should_reconsider_activity(self, current_time):
        """Return whether the character should reconsider their current activity."""

        if self.activity_start_time is None:
            return False

        minimum_activity_time = timedelta(minutes=30)

        if current_time - self.activity_start_time < minimum_activity_time:
            return False

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
        self.activity_completed_this_tick = None

        if self.activity == "Traveling":
            return False

        activity_changed = False
        activity_completed = (
            self.activity_end_time is not None
            and current_time >= self.activity_end_time
        )

        if (
            self.activity_end_time is None
            or activity_completed
            or self.should_reconsider_activity(current_time)
        ):
            previous_activity = self.activity

            if activity_completed:
                self.last_completed_activity = previous_activity
                self.activity_completed_this_tick = previous_activity

            self.choose_activity(current_time)
            activity_changed = self.activity != previous_activity

        return activity_changed
