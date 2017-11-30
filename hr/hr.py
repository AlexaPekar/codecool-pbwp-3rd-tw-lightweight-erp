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
    while True:
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
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):

    title_list = ["ID", "Name", "Birth date"]
    ui.print_table(table, title_list)


def add(table):

    title_list = ["Name: ", "Birth date: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table


def remove(table, id_):
    ids = common.id_list(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
        data_manager.write_table_to_file("hr/persons.csv", table)
    else:
        ui.print_error_message("This ID is not in the file!")

    return table


def update(table, id_):

    title_list = ["Name: ", "Birth date: "]
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

    years = []
    oldest = 0
    oldest_persons = []
    table = data_manager.get_table_from_file("hr/persons.csv")

    for line in table:
        years.append(int(line[2]))
    oldest = min(years)
    for line in table:
        if str(oldest) in line:
            oldest_persons.append(line[1])
    return oldest_persons

# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)


def get_persons_closest_to_average(table):

    years = []
    ages = []
    sum_ages = 0
    avg_ages = 0
    difference = []
    result_list = []
    year_now = 2017
    table = data_manager.get_table_from_file("hr/persons.csv")

    for line in table:
        years.append(int(line[2]))
    for year in years:
        age = year_now - year
        ages.append(age)

    for age in ages:
        sum_ages = sum_ages + age
    avg_ages = sum_ages / len(ages)

    closest_year = 0
    tableid = 0

    for i in range(len(table)):
        difference.append(abs(ages[i] - avg_ages))
    min_dif = min(difference)

    for i in range(len(table)):
        if (float(ages[i] - float(avg_ages)) == min_dif):
            result_list.append(table[i][1])
    return result_list
