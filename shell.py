"""
Basic I/OP module.

Uses curses module from stdlib: https://docs.python.org/3/howto/curses.html

Taken from the docs:
Note that the coordinate system used in curses is unusual. Coordinates are always passed in the order y,x,
and the top-left corner of a window is coordinate (0,0). This breaks the normal convention for handling
coordinates where the x coordinate comes first.
"""
import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)

    stdscr.clear()
    stdscr.keypad(True)
    stdscr.addstr("Application started!\n")
    stdscr.addstr("Color output: " + "enabled" if curses.has_colors() else "disabled")
    stdscr.refresh()
    handle_input(stdscr)

    win = curses.newwin(curses.LINES, curses.COLS, 0, curses.COLS // 2)
    win.addstr("Window Opened!", curses.color_pair(1) ^ curses.A_REVERSE)
    win.refresh()
    handle_input(stdscr)


def handle_input(screen):
    user_input = screen.getkey()
    # TODO: Echo input somewhere


if __name__ == "__main__":
    wrapper(main)