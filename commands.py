import random
import curses




def add_item(stdscr):
    while True:
        item = ""
        curses.curs_set(0)
        stdscr.clear()
        stdscr.refresh()
        stdscr.addstr(0, 0, "What is the name of the item: ")
        stdscr.refresh()
        curses.echo()
        item = stdscr.getstr(1, 0).decode().strip() 
        curses.noecho() 
        item_id_check = False

        while item_id_check == False:
            item_id = random.randint(1000, 9999)
            with open('inventory.csv', 'r') as file:
                item_id_inv = [int(line.split(' - ')[0]) for line in file if line.strip()]
                if item_id not in item_id_inv:
                    item_id_con = item_id
                    item_id_check = True
        if item != "":
            with open('inventory.csv', 'a') as file:
                print(f"{item_id_con} - {item}", file=file)
                print("Press any key to go back.")
                stdscr.getch()
                stdscr.clear()
                return
                
        else:
            stdscr.addstr(0, 0,"Please enter acceptible input.")
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

            stdscr.addstr(0, 0, "ID - Name")
            for idx, choice in enumerate(list_all):
                if idx == current_row:
                    idx += 1
                    stdscr.addstr(idx, 0, f"> {choice}", curses.A_REVERSE)
                else:
                    idx += 1
                    stdscr.addstr(idx, 0, f"  {choice}")
                    

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
                    stdscr.addstr(0, 0, f"You selected: {list_all[current_row]}")
                    stdscr.addstr(2, 0, "Press any key to go back.")
                    stdscr.refresh()
                    stdscr.getch()