# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    datas = data_manager.get_table_from_file("hr/persons.csv")
    options = ["Display table", "Add", "Remove", "Update"]
    ui.print_menu("Human resources menu", options, "Main menu")
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
        handle_menu()
    else:
        ui.print_error_message("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Name", "Birth date"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    title_list = ["Name", "Birth date"]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("hr/persons.csv", table)
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
    data_manager.write_table_to_file("hr/persons.csv", table)

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
    title_list = ["Name", "Birth date"]
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
        data_manager.write_table_to_file("hr/persons.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
