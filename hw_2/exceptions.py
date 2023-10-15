"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class ValidationError(Exception):
    pass

class LowFuelError(ValidationError):
    pass

class NotEnoughFuel(ValidationError):
    pass

class CargoOverload(ValidationError):
    pass