import os


os.add_dll_directory(os.getcwd())

import unicurses as uc
from cogs.core import *
from cogs.cartography import *

def insert_cells_from_list(cell_list: List[Cell]):
    uc.init_pair(1, uc.COLOR_CYAN, uc.use_default_colors())
    uc.attron(uc.COLOR_PAIR(1))
    for cell in cell_list:
        uc.mvaddstr(cell.y, cell.x, cell.identifier)
    uc.attron(uc.COLOR_PAIR(1))
    uc.move(0, 0)

def insert_cells(*cells: Cell):
    for cell in cells:
        uc.mvaddstr(cell.y, cell.x, cell.identifier)
    uc.move(0, 0)

def make_rectangle(x, y, width, height):
    top = Wall(x, y, width, "east").make_wall()
    bottom = Wall(x, height - 1, width, "east").make_wall()
    left = Wall(x, y, height, "south").make_wall()
    right = Wall(width - 1, y, height, "south").make_wall()
    insert_cells_from_list(top)
    insert_cells_from_list(bottom)
    insert_cells_from_list(left)
    insert_cells_from_list(right)

def main():
    stdscr = uc.initscr()
    uc.curs_set(0)
    uc.start_color()
    while True:
        key = uc.getch()
        if key == 27:
            uc.nodelay(stdscr, True)
            n = uc.getch()
            if n == -1:
                break
            uc.nodelay(stdscr, False)
    uc.endwin()
    return 0

if __name__ == "__main__":
    main()