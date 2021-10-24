from abc import ABC, abstractmethod


class DObject(ABC):
    def __init__(self, id, name, interactable=False):
        self.id = id
        self.name = name
        self.interactable = interactable

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def interactable(self):
        return self.__interactable

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @interactable.setter
    def interactable(self, i):
        if not isinstance(i, bool):
            raise TypeError("interactable must be bool")
        self.__interactable = i

    @abstractmethod
    def interact(self): pass
