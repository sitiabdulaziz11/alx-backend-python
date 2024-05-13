"""
Imagine you're building a house, and you've
hired different contractors to do various tasks
like plumbing, electrical work, and carpentry.
Now, during the construction process, you want
to test each part of the house to ensure it works
as expected.

For instance, let's say you're testing the electrical system of
the house. You have a switch that turns on the lights in the living
room. However, you don't want to rely on the actual
wiring and light bulbs during testing because that
might introduce unpredictability (e.g., what if the
light bulb blows out?). Instead, you create a mock
switch that behaves exactly like the real one
but doesn't depend on the actual wiring or bulbs.

Here's how it translates to Python code using
the unittest.mock module:
"""

from unittest.mock import MagicMock

class ElectricalSystem:
    def __init__(self):
        self.lights_on = False

    def switch_on(self):
        self.lights_on = True

    def switch_off(self):
        self.lights_on = False

class House:
    def __init__(self, electrical_system):
        self.electrical_system = electrical_system

    def living_room_lights_on(self):
        self.electrical_system.switch_on()

# Now, during testing, you want to isolate the behavior
# of the House class without relying on the actual ElectricalSystem.
# So, you create a mock ElectricalSystem to simulate its behavior.

def test_living_room_lights_on():
    mock_electrical_system = MagicMock(spec=ElectricalSystem)
    house = House(mock_electrical_system)

    house.living_room_lights_on()

    mock_electrical_system.switch_on.assert_called_once()

# Here, we're testing if the living room lights are
# switched on correctly in the House class.
# We're using a mock electrical system to simulate
# the behavior without involving the actual electrical wiring.
# The assert_called_once() method ensures that the switch_on method
# of the mock object is called exactly once.


class Calculator:
    def add(self, a, b):
        return a + b

def mock_add(a, b):
    return 10

calculator = Calculator()
calculator.add = MagicMock(side_effect=mock_add)

assert calculator.add(2, 3) == 10
