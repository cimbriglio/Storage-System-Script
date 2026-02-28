import os
import time
import commands
import curses

def main_menu(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    choices = ["Add Item","Remove Item", "List Item", "Search Item","Exit"]
    current_row = 0
    stdscr.bkgd(' ', curses.color_pair(1))

    while True:

        if curses.has_colors():
            curses.start_color()
            # Define color pair 1: Yellow foreground on Red background
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
            # Define color pair 2: Green foreground on Green background (useful for a block highlight effect)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_CYAN)
            
            stdscr.bkgd(' ', curses.color_pair(1))

        h, w = stdscr.getmaxyx()
        

        
        with open('inventory.csv', 'r+') as file:
            inventory_content = file.read()
            file.seek(0)
            file.write("\n".join(line for line in inventory_content.splitlines() if line.strip()))
        stdscr.clear()

        for idx, choice in enumerate(choices):
            text = f"> {choice}" if idx == current_row else f"  {choice}"
            x = w // 2 - len(text) // 2          # horizontal center
            y = h // 2 - len(choices) // 2 + idx # vertical center block

            if idx == current_row:
                stdscr.addstr(y, x, text, curses.A_REVERSE | curses.A_BOLD | curses.color_pair(2))
            else:
                stdscr.addstr(y, x, text, curses.A_BOLD | curses.color_pair(2))

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(choices) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if choices[current_row] == "Add Item":
                stdscr.clear()
                time.sleep(0.25)
                commands.add_item(stdscr)
            elif choices[current_row] == "Remove Item":
                stdscr.clear()
                time.sleep(0.25)
                commands.remove_item(stdscr)
            elif choices[current_row] == "List Item":
                stdscr.clear()
                time.sleep(0.25)
                commands.list_item(stdscr)
            elif choices[current_row] == "Search Item":
                stdscr.clear()
                time.sleep(0.25)
                commands.search_item(stdscr)
            elif choices[current_row] == "Exit":
                break

curses.wrapper(main_menu)