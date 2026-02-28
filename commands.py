import random
import curses




def add_item(stdscr):
    while True:
        item = ""
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(3, 0,"Press 'Q' to go back.", curses.A_BOLD | curses.color_pair(2))
        stdscr.addstr(0, 0, "What is the name of the item you would like to add: ", curses.A_BOLD | curses.color_pair(2))
        stdscr.refresh()
        stdscr.attron(curses.color_pair(3))
        curses.echo()
        item = stdscr.getstr(1, 0).decode().strip() 
        curses.noecho()
        stdscr.attroff(curses.color_pair(3))
        item_id_check = False
        if item == "Q":
            stdscr.clear()
            return
        
        while item_id_check == False:
            item_id = random.randint(1000, 9999)
            with open('inventory.csv', 'r') as file:
                item_id_inv = [int(line.split(' - ')[0]) for line in file if line.strip()]
                if item_id not in item_id_inv:
                    item_id_con = item_id
                    item_id_check = True
        if item != "" and item != "Q":
            with open('inventory.csv', 'a') as file:
                print(f"{item_id_con} - {item}", file=file)
                stdscr.addstr(3, 0,"Press any key to go back.", curses.A_BOLD | curses.color_pair(2))
                stdscr.getch()
                stdscr.clear()
                return

        else:
            stdscr.addstr(0, 0,"Please enter acceptible input.", curses.A_BOLD | curses.color_pair(2))
            stdscr.refresh()         

def remove_item(stdscr):
    while True:
        remove_item = ""
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(0, 0, "What is the ID of the item you would like to remove: ", curses.A_BOLD | curses.color_pair(2))
        stdscr.refresh()
        stdscr.attron(curses.color_pair(3))
        curses.echo()
        remove_item = stdscr.getstr(1, 0).decode().strip() 
        curses.noecho()
        stdscr.attroff(curses.color_pair(3))

        if remove_item != "":
            with open("inventory.csv", "r") as f:
                lines = f.readlines()

            filtered_lines = [line for line in lines if remove_item not in line.split()]

            with open("inventory.csv", "w") as f:
                f.writelines(filtered_lines)
                print("Press any key to go back.", curses.A_BOLD | curses.color_pair(2))
                stdscr.getch()
                stdscr.clear()
                return
        else:
            stdscr.addstr(0, 0,"Please enter acceptible input", curses.A_BOLD | curses.color_pair(2))
            stdscr.refresh()

def list_item(stdscr):
    current_row = 0
    while True:
       
        
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()

        with open('inventory.csv', 'r') as file:
            list_all = [line.strip() for line in file]
            list_all.append("Exit")

            stdscr.addstr(0, 0, "ID - Name", curses.A_BOLD | curses.color_pair(2))
            for idx, choice in enumerate(list_all):
                if idx == current_row:
                    idx += 1
                    stdscr.addstr(idx, 0, f"> {choice}", curses.A_REVERSE | curses.A_BOLD | curses.color_pair(2))
                else:
                    idx += 1
                    stdscr.addstr(idx, 0, f"  {choice}", curses.A_BOLD | curses.color_pair(2))
                    

            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > -1:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(list_all) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if list_all[current_row] == "Exit":
                    return
                else:            
                    stdscr.clear()
                    stdscr.addstr(0, 0, f"You selected: {list_all[current_row]}", curses.A_BOLD | curses.color_pair(2))
                    stdscr.addstr(2, 0, "Press any key to go back.", curses.A_BOLD | curses.color_pair(2))
                    stdscr.refresh()
                    stdscr.getch()

def search_item(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    while True:
        stdscr.refresh()
        stdscr.addstr(0, 0, "What is the name of the item you are searching for: ", curses.A_BOLD | curses.color_pair(2))
        stdscr.refresh()
        curses.echo()
        search_item_var = stdscr.getstr(1, 0).decode().strip() 
        curses.noecho()

        if search_item_var != "":
            with open('inventory.csv', "r") as file:
                for line_number, line in enumerate(file):
                    if search_item_var in line:
                        stdscr.clear()
                        stdscr.addstr(f"{line.strip()}")
                        stdscr.addstr(2, 0, "Press any key to go back.", curses.A_BOLD | curses.color_pair(2))
                        stdscr.refresh()
                        stdscr.getch()
                        return
        else:
            stdscr.clear()
            stdscr.addstr(0, 0, "Please enter an acceptible input.", curses.A_BOLD | curses.color_pair(2))
            stdscr.addstr(2, 0, "Press any key to go back.", curses.A_BOLD | curses.color_pair(2))
            stdscr.refresh()
            stdscr.getch()
            stdscr.clear()

def draw_centered(stdscr, text, line_number):
    # Get current window width
    h, w = stdscr.getmaxyx()
    
    # Calculate starting x-coordinate
    x = (w // 2) - (len(text) // 2)
    
    # Print the text at (y, x)
    stdscr.addstr(line_number, x, text)
    stdscr.refresh()
