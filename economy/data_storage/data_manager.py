from economy import Cache, PersistentStorage


class DataManager:
    def __init__(
        self, *, cache: Cache = None, persistent_storage: PersistentStorage = None
    ):
        self.cache: Cache = cache  # or DefaultCache
        self.persistent_storage: PersistentStorage = (
            persistent_storage  # or default storage
        )
