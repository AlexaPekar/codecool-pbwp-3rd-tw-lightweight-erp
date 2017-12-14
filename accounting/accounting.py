import os
import ui
import data_manager
import common
import sys


def start_module():
    while True:
        datas = data_manager.get_table_from_file("accounting/items.csv")
        options = ["Display table", "Add", "Remove", "Update", "Highest profit year", "Average profit in a given year"]
        ui.print_menu("\nAccounting Menu", options, "Main menu")
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
            ui.print_result(which_year_max(datas), "The year having the highest profit:")
        elif option == "6":
            os.system("clear")
            year_list = ui.get_inputs(["Year: "], "Please, add the year to get its average profit!")
            ui.print_result(avg_amount(datas, int(year_list[0])), "The avarage profit of " + year_list[0] + ":")
        elif option == "0":
            os.system("clear")
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    ui.print_table(table, title_list)


def add(table):
    module_headers = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    return common.common_add(table, module_headers)


def remove(table, id_):
    return common.common_remove(table, id_, "accounting/items.csv")


def update(table, id_):
    module_headers = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    return common.common_update(table, id_, "accounting/items.csv", module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "accounting/items.csv")


def which_year_max(table):
    counter_one = 0
    counter_two = 0
    years = []
    for row in table:
        years.append(row[3])
    years = list(set(years))

    for i in range(len(table)):
        if table[i][3] == years[0]:
            if table[i][4] == "in":
                counter_one += int(table[i][5])
            elif table[i][4] == "out":
                counter_one -= int(table[i][5])
        elif table[i][3] == years[1]:
            if table[i][4] == "in":
                counter_two += int(table[i][5])
            elif table[i][4] == "out":
                counter_two -= int(table[i][5])
    if counter_one > counter_two:
        return int(years[0])
    else:
        return int(years[1])


def avg_amount(table, year):
    counter = 0
    profit_changes = []
    for i in range(len(table)):
        if int(table[i][3]) == year:
            if table[i][4] == "in":
                counter += int(table[i][5])
            elif table[i][4] == "out":
                counter -= int(table[i][5])
            profit_changes.append(table[i][4])
    return counter / len(profit_changes)
