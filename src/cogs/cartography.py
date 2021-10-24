from typing import List
from cogs.core import DObject


# Abstract cell classess
class Cell:
    """
    A cell containing coordinates of (x, y),
    color for terminal to print and,
    an identifier on terminal.
    """
    def __init__(self, x=0, y=0, color="white", identifier="#"):
        
        if not isinstance(y, int):
            raise TypeError("y must be integer")
        self.x = x
        self.y = y
        self.color = color
        self.identifier = identifier

    def __repr__(self):
        return f"({self.x}, {self.y})"

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def color(self):
        return self.__color

    @property
    def identifier(self):
        return self.__identifier
    
    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be integer")
        self.__x = val

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be integer")
        self.__y = val

    @color.setter
    def color(self, color):
        self.__color = color

    @identifier.setter
    def identifier(self, identifier):
        if len(identifier) != 1:
            raise ValueError("identifier should be 1 character long")
        self.__identifier = identifier


class AreaCell(Cell):
    def __init__(self, x=0, y=0, objs=[]):
        super().__init__(x, y)
        self.__objs = objs
    
    @property
    def objects(self):
        return self.__objs

    @objects.setter
    def objects(self, obj_list):
        if not isinstance(obj_list, List):
            raise TypeError("obj_list must be List")
        if any(tuple(not isinstance(x, DObject) for x in obj_list)):
            raise TypeError("obj_list can only contain DObject(s)")
        self.__objs = obj_list


class Wall:
    def __init__(self, x=0, y=0, length=1, direction="east"):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction
        self.__wallcells = []

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def length(self):
        return self.__length

    @property
    def direction(self):
        return self.__direction

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be integer")
        self.__x = val

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be integer")
        self.__y = val

    @length.setter
    def length(self, val):
        if not isinstance(val, int):
            raise TypeError("length must be integer")
        self.__length = val

    @direction.setter
    def direction(self, direction):
        if not any((direction == "north",
                    direction == "south",
                    direction == "east",
                    direction == "west")):
            raise ValueError("direction can only be either north, south, east or west")
        self.__direction = direction

    def make_wall(self):
        self.__wallcells.clear()
        if self.direction == "east":
            for i in range(self.length):
                self.__wallcells.append(Cell(self.x + i, self.y))
        elif self.direction == "west":
            for i in range(self.length):
                self.__wallcells.append(Cell(self.x - i, self.y))
        elif self.direction == "north":
            for i in range(self.length):
                self.__wallcells.append(Cell(self.x, self.y - i))
        elif self.direction == "south":
            for i in range(self.length):
                self.__wallcells.append(Cell(self.x, self.y + i))
        return self.__wallcells