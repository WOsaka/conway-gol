from enum import Enum

class FieldStatus(Enum):
    DEAD = 0
    COPY = 1
    ALIVE = 2

    def __str__(self):
        return self.name