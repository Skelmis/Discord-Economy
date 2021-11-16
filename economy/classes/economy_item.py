from typing import Optional

import attr


# noinspection PyUnresolvedReferences
@attr.s(slots=True)
class EconomyItem:
    """
    A generic Item in your economy.

    Parameters
    ----------
    name: str
        The name of this Item in your economy.

        This needs to be unique
    cost: float
        How much 1 of this Item should cost
    max_ownership: int, optional
        The max amount someone can own of this Item

        Defaults to unlimited
    """

    name: str = attr.ib(validator=attr.validators.instance_of(str))
    cost: float = attr.ib(validator=attr.validators.instance_of(float), converter=float)
    max_ownership: Optional[int] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(int))
    )
