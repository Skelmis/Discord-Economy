from typing import List, Optional

import attr

from economy import EconomyItem, Item, MissingDataManager
from economy.data_storage import DataManager


@attr.s
class Person:
    """
    Represents a Person in your economy
    """

    data_manager: Optional[DataManager] = attr.ib(default=None)

    @property
    async def items(self) -> List[Item]:
        """
        Returns
        -------
        List[EconomyItem]
            All the Item's this person has

        Raises
        ------
        MissingDataManager
            This class is missing the data manager instance
        """
        if not self.data_manager:
            raise MissingDataManager

        return []
