from core import DObject


class Cell:
    """A cell containing coordinates of (x, y)
    """
    def __init__(self, x=0, y=0):
        if not isinstance(x, int):
            raise TypeError("x must be integer")
        if not isinstance(y, int):
            raise TypeError("y must be integer")
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


class AreaCell(Cell):
    def __init__(self, x=0, y=0, objs=[]):
        super().__init__(x, y)
        self.__objs = objs
    
    def get_objects(self):
        return self.__objs

    def set_objects(self, obj_list):
        if any(tuple(not isinstance(x, DObject) for x in obj_list)):
            raise TypeError("obj_list can only contain DObject(s)")
        self.__objs = obj_list


cell = AreaCell()
cell.set_objects([DObject("player", "Player")])
print(cell.get_objects())