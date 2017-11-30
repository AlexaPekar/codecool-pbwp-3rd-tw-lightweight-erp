# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("inventory/inventory.csv")
        options = ["Display table", "Add", "Remove", "Update", "Available items", "Average durability by manufacturers"]
        ui.print_menu("\nInventory menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            show_table(datas)
        elif option == "2":
            add(datas)
        elif option == "3":
            given_id = ui.get_inputs(["Please enter an ID to remove the line: "], "")
            remove(datas, given_id)
        elif option == "4":
            update_id = ui.get_inputs(["Please enter an ID to update the line: "], "")
            update(datas, update_id)
        elif option == "5":
            ui.print_result(get_available_items(datas), "is the result of 1st inventory extra function.")
        elif option == "6":
            ui.print_result(get_average_durability_by_manufacturers(datas), "is the result of 2nd inventory extra function.")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(table, title_list)

    
def add(table):
    title_list = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table


def remove(table, id_):
    ids = common.id_list(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
        data_manager.write_table_to_file("inventory/inventory.csv", table)
    else:
        ui.print_error_message("There is no such option.")
    return table


def update(table, id_):
    title_list = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    new_items = []
    ids = common.id_list(table)
    if id_[0] in ids:
        new_items.append(id_[0])
        new_elements = ui.get_inputs(title_list, "Please add the items")
        for item in new_elements:
            new_items.append(item)
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table[i] = new_items
        data_manager.write_table_to_file("inventory/inventory.csv", table)
    else:
        ui.print_error_message("There is no such option.")
    return table


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