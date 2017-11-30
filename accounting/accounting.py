# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
        datas = data_manager.get_table_from_file("accounting/items.csv")
        options = ["Display table", "Add", "Remove", "Update"]
        ui.print_menu("\nAccounting Menu", options, "Main menu")
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
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):

    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)


def add(table):

    title_list = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


def remove(table, id_):

    ids = common.id_list(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
        data_manager.write_table_to_file("accounting/items.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")
    return table


def update(table, id_):

    title_list = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
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
        data_manager.write_table_to_file("accounting/items.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")
    return table
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
