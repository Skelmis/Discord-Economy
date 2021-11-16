class DiscordEconomyException(Exception):
    """A base exception for all discord economy exceptions."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message


class MissingDataManager(DiscordEconomyException):
    """Cannot complete this action due to a lack of the DataManager."""
