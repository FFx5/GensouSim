from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


class SimulationClock:
    def __init__(self, mode="live"):
        self.timezone = ZoneInfo("Asia/Tokyo")
        self.mode = mode
        self.manual_time = None

        if self.mode == "manual":
            self.manual_time = datetime.now(self.timezone)

    @property
    def current_time(self):
        """Return the current simulation date and time."""

        if self.mode == "manual":
            return self.manual_time

        return datetime.now(self.timezone)

    def set_manual_time(self, simulation_time):
        """Set the simulation time when using manual mode."""

        self.manual_time = simulation_time

    def advance(self, amount):
        """Advance the simulation time when using manual mode."""

        if self.mode != "manual":
            return

        self.manual_time += amount

    def tick(self):
        """Return the current simulation time for a simulation update."""

        return self.current_time