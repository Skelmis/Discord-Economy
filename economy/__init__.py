from economy.abc import Cache, PersistentStorage
from economy.classes import EconomyItem, Item
from economy.exceptions import DiscordEconomyException, MissingDataManager

__version__ = "0.0.1a1"
__all__ = (
    "__version__",
    "VersionInfo",
    "EconomyItem",
    "Cache",
    "PersistentStorage",
    "Item",
    "DiscordEconomyException",
    "MissingDataManager",
)

import sys
import logging
from collections import namedtuple

logging.getLogger(__name__).addHandler(logging.NullHandler())
VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel="alpha", serial=0)


if sys.version_info[1] < 8:
    raise RuntimeError("This package requires python 3.8 or higher.")
