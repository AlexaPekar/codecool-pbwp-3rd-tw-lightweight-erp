# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
        datas = data_manager.get_table_from_file("crm/customers.csv")
        options = ["Display table", "Add", "Remove", "Update"]
        ui.print_menu("CRM Menu", options, "Main menu")
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
    
    title_list = ["ID", "Name", "E-mail", "Subscribed"]
    ui.print_table(table, title_list)


def add(table):

    title_list = ["Name: ", "E-mail: ", "Subscribed: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


def remove(table, id_):

    ids = common.id_list(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
        data_manager.write_table_to_file("crm/customers.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")
    return table


def update(table, id_):

    title_list = ["Name: ", "E-mail: ", "Subscribed: "]
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
        data_manager.write_table_to_file("crm/customers.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order


def get_longest_name_id(table):

    with open("crm/customers.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
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
    
    common.asc_sort(longest_names)
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

    table = data_manager.get_table_from_file("crm/customers.csv")

    for line in table:
        if int(line[3]) == subscribed:
            subscribed_names.append(line[1])
            subscribed_emails.append(line[2])
    for i in range(len(subscribed_names)):
        subscribed_name = subscribed_names[i]
        subscribed_email = subscribed_emails[i]
        subscribed_customers.append(subscribed_name + ";" + subscribed_email)
    return subscribed_customers