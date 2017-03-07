from enum import Enum


class Category(Enum):
    Football = 1
    Python = 2

    def __str__(self):
        return self.name
