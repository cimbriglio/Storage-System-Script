import os
import time
import commands
import curses

def main_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    choices = ["Add Item", "List Item", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()

        for idx, choice in enumerate(choices):
            if idx == current_row:
                stdscr.addstr(idx, 0, f"> {choice}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx, 0, f"  {choice}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(choices) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if choices[current_row] == "Add Item":
                stdscr.clear()
                commands.add_item(stdscr)
            elif choices[current_row] == "List Item":
                stdscr.clear()
                commands.list_item(stdscr)
            elif choices[current_row] == "Exit":
                break

curses.wrapper(main_menu)