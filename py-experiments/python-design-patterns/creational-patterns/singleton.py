# What the Gang of Four’s original Singleton Pattern
# might look like in Python.


class Logger1:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


# Straightforward implementation of the Singleton Pattern


class Logger2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the object")
            cls._instance = super().__new__(cls)
            # Put any initialization here.
        return cls._instance
