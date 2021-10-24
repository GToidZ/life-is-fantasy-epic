from abc import ABC, abstractmethod
from cogs.core import DObject


class PlayerObject(DObject):
    def __init__(self, name):
        super().__init__("player", name, False)

    def interact(self):
        pass

class NPCObject(DObject, ABC):
    def __init__(self, uid, name):
        super().__init__(f"npc[{uid}]", name, False)
        self.__uid = uid

    def get_uid(self):
        return self.__uid

    def interact(self):
        self.interactions()

    @abstractmethod
    def interactions(self): pass

class QuesterNPC(NPCObject):
    def __init__(self, uid, name):
        super().__init__(uid, name)

    def interactions(self):
        pass
