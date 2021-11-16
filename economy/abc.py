from typing import runtime_checkable, Protocol


@runtime_checkable
class PersistentStorage(Protocol):
    """The ABC for persistent storage"""


@runtime_checkable
class Cache(Protocol):
    """The ABC for caches"""
