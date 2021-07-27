from enum import Enum


class ActionType(Enum):
    """
    List of access defined in the application
    """

    @staticmethod
    def list():
        """get the all the option as list

        """
        return list(map(lambda c: c.name + ': ' + str(c.value), ActionType))

    Read = 1
    Write = 2
    Update = 3
    Delete = 4
