# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)
import os
import ui
import data_manager
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("inventory/inventory.csv")
        options = ["Display table", "Add", "Remove", "Update", "Available items", "Average durability by manufacturers"]
        ui.print_menu("\nInventory menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            os.system("clear")
            show_table(datas)
        elif option == "2":
            os.system("clear")
            add(datas)
            write_to_file(datas)
        elif option == "3":
            os.system("clear")
            given_id = ui.get_inputs(["Please, enter an ID to remove the line: "], "")
            remove(datas, given_id)
            write_to_file(datas)
        elif option == "4":
            os.system("clear")
            update_id = ui.get_inputs(["Please, enter an ID to update the line: "], "")
            update(datas, update_id)
            write_to_file(datas)
        elif option == "5":
            os.system("clear")
            ui.print_result(get_available_items(datas), "The available  items:")
        elif option == "6":
            os.system("clear")
            ui.print_result(get_average_durability_by_manufacturers(datas),
                            "The average durability by manufacturers:")
        elif option == "0":
            os.system("clear")
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    module_headers = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    return common.common_show_table(table, module_headers)


def add(table):
    module_headers = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    return common.common_add(table, module_headers)


def remove(table, id_):
    return common.common_remove(table, id_, "inventory/inventory.csv")


def update(table, id_):
    module_headers = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    return common.common_update(table, id_, "inventory/inventory.csv", module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "inventory/inventory.csv")


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):
    available_items = []
    for i in range(len(table)):
        if int(table[i][3]) + int(table[i][4]) >= 2017:
            table[i][3] = int(table[i][3])
            table[i][4] = int(table[i][4])
            available_items.append(table[i])
    return available_items

# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists


def get_average_durability_by_manufacturers(table):
    company_counter = {}
    sum_dict = {}
    avg_dict = {}

    for row in table:
        if row[2] in company_counter:
            company_counter[row[2]] += 1
        else:
            company_counter[row[2]] = 1

    for row in table:
        if row[2] in sum_dict:
            sum_dict[row[2]] += int(row[4])
        else:
            sum_dict[row[2]] = int(row[4])

    for key, value in company_counter.items():
        avg_dict[key] = sum_dict[key] / value
    return avg_dict
