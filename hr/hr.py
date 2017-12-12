# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)
import os
import ui
import data_manager
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("hr/persons.csv")
        options = ["Display table", "Add", "Remove", "Update", "Oldest person", "Closest person to the average age"]
        ui.print_menu("\nHuman resources menu", options, "Main menu")
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
            ui.print_result(get_oldest_person(datas), "is the result of the 1st HR extra function.")
        elif option == "6":
            ui.print_result(get_persons_closest_to_average(datas), "is the result of the 2nd HR extra function.")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    title_list = ["ID", "Name", "Birth date"]
    ui.print_table(table, title_list)


def add(table):
    module_headers = ["Name: ", "Birth date: "]
    return common.common_add(table, module_headers)


def remove(table, id_):
    return common.common_remove(table, id_, "hr/persons.csv")


def update(table, id_):
    module_headers = ["Name: ", "Birth date: "]
    return common.common_update(table, id_, "hr/persons.csv", module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "hr/persons.csv")

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
