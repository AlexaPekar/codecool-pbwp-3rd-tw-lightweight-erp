# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)
import os
import ui
import data_manager
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("crm/customers.csv")
        options = ["Display table", "Add", "Remove", "Update", "Longest name's ID", "List of subscribed customers"]
        ui.print_menu("\nCRM Menu", options, "Main menu")
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
            given_id = ui.get_inputs(["Please enter an ID to remove the line: "], "")
            remove(datas, given_id)
            write_to_file(datas)
        elif option == "4":
            os.system("clear")
            update_id = ui.get_inputs(["Please enter an ID to update the line: "], "")
            update(datas, update_id)
            write_to_file(datas)
        elif option == "5":
            os.system("clear")
            ui.print_result(get_longest_name_id(datas), "is the result of the 1st CRM extra function")
        elif option == "6":
            os.system("clear")
            ui.print_result(get_subscribed_emails(datas), "\nis the result of the 2nd CRM extra function")
        elif option == "0":
            os.system("clear")
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    module_headers = ["ID", "Name", "E-mail", "Subscribed"]
    return common.common_show_table(table, module_headers)


def add(table):
    module_headers = ["Name: ", "E-mail: ", "Subscribed: "]
    return common.common_add(table, module_headers)


def remove(table, id_):
    return common.common_remove(table, id_, "crm/customers.csv")


def update(table, id_):
    module_headers = ["Name: ", "E-mail: ", "Subscribed: "]
    return common.common_update(table, id_, "crm/customers.csv", module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "crm/customers.csv")


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order


def get_longest_name_id(table):
    names = []
    lenght_names = []
    longest_names = []
    the_name = ""
    the_id = ""
    for i in range(len(table)):
        names.append(table[i][1])
    for name in names:
        lenght_names.append(len(name))
    longest_name_length = max(lenght_names)
    for name in names:
        if len(name) == longest_name_length:
            longest_names.append(name)

    common.collect_ids(longest_names)
    the_name = longest_names[0]

    for line in table:
        if the_name in line:
            the_id = line[0]
    return the_id
# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    subscribed = 1
    subscribed_names = []
    subscribed_emails = []
    subscribed_customers = []

    for line in table:
        if int(line[3]) == subscribed:
            subscribed_names.append(line[1])
            subscribed_emails.append(line[2])
    for i in range(len(subscribed_names)):
        subscribed_name = subscribed_names[i]
        subscribed_email = subscribed_emails[i]
        subscribed_customers.append(subscribed_email + ";" + subscribed_name)
    return subscribed_customers
    pass


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    table = data_manager.get_table_from_file("crm/customers.csv")
    for i in range(len(table)):
        if id == table[i][0]:
            return table[i][1]


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """
    for i in range(len(table)):
        if id == table[i][0]:
            return table[i][1]

