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
"""
Starts this module and displays its menu.
User can access default special features from here.
User can go back to main menu from here.

Returns:
    None
"""


def start_module():
    datas = data_manager.get_table_from_file("inventory/inventory.csv")
    inventory_options = ["Display table", "Add", "Remove", "Update"]
    ui.print_menu("Inventory menu", inventory_options, "Main menu")
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
        update(table, id_)
    elif option == "0":
        handle_menu()
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Name", "Manufacturer", "Purchase date", "Durability"]
    ui.print_table(table, title_list)

    
def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """
    title_list = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items: ")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        Table without specified record.
    """

    for i in range(len(table)):
        if table[i][0] == id_[0]:
            table.pop(i)
            break
    data_manager.write_table_to_file("inventory/inventory.csv", table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: Which items have not exceeded their durability yet?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_items(table):

    # your code

    pass


# the question: What are the average durability times for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
