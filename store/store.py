# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number
import os
import ui
import data_manager
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("store/games.csv")
        options = [
            "Display table",
            "Add",
            "Remove",
            "Update",
            "Available games by manufacturer",
            "Average amount of games by manufacturer"]
        ui.print_menu("\nStore menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            show_table(datas)
        elif option == "2":
            add(datas)
            write_to_file(datas)
        elif option == "3":
            given_id = ui.get_inputs(["Please enter an ID to remove the line: "], "")
            remove(datas, given_id)
            write_to_file(datas)
        elif option == "4":
            update_id = ui.get_inputs(["Please enter an ID to update the line: "], "")
            update(datas, update_id)
            write_to_file(datas)
        elif option == "5":
            ui.print_result(get_counts_by_manufacturers(datas), "is the result of the 1st store extra function.")
        elif option == "6":
            manufacturer = ui.get_inputs(["Please choose a manufacturer to get the average amount of games: "], "")
            ui.print_result(
                get_average_by_manufacturer(
                    datas,
                    manufacturer[0]),
                "is the result of the 2nd store extra function.")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    title_list = ["ID", "Title", "Manufacturer", "Price", "In stock"]
    ui.print_table(table, title_list)


def add(table):
    module_headers = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    return common.common_add(table, module_headers)


def remove(table, id_):
    return common.common_remove(table, id_, "store/games.csv")


def update(table, id_):
    module_headers = ["Title: ", "Manufacturer: ", "Price: ", "In stock: "]
    return common.common_update(table, id_, "inventory/inventory.csv", module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "store/games.csv")


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    manufacturers = []
    manufacturer_dict = {}
    for row in table:
        manufacturers.append(row[2])
    for manufacturer in manufacturers:
        if manufacturer in manufacturer_dict:
            manufacturer_dict[manufacturer] += 1
        else:
            manufacturer_dict[manufacturer] = 1
    return manufacturer_dict


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    manufacturers = []
    in_stocks = []
    total = 0
    try:
        for i in range(len(table)):
            if manufacturer == table[i][2]:
                in_stocks.append(int(table[i][4]))
        for in_stock in in_stocks:
            total += in_stock
        return total / len(in_stocks)
    except BaseException:
        ui.print_error_message("There's no such manufacturer in table!")
