import sys
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from simulation.clock import SimulationClock


clock = SimulationClock(mode="manual")

print("Starting time:")
print(clock.current_time.strftime("%Y-%m-%d %H:%M:%S JST"))

print()

clock.advance(timedelta(hours=1))

print("After advancing one hour:")
print(clock.current_time.strftime("%Y-%m-%d %H:%M:%S JST"))

print()

clock.advance(timedelta(days=1, hours=2, minutes=30))

print("After advancing another 1 day, 2 hours, and 30 minutes:")
print(clock.current_time.strftime("%Y-%m-%d %H:%M:%S JST"))