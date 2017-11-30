# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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
        datas = data_manager.get_table_from_file("sales/sales.csv")
        options = ["Display table", "Add", "Remove", "Update"]
        ui.print_menu("\nSales menu", options, "Main menu")
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
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)

def add(table):
    title_list = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    random_id = common.generate_random(table)
    inputs = ui.get_inputs(title_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    data_manager.write_table_to_file("sales/sales.csv", table)
    return table


def remove(table, id_):
    ids = common.id_list(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
        data_manager.write_table_to_file("sales/sales.csv", table)
    else:
        ui.print_error_message("There is no such option.")
    return table


def update(table, id_):
    title_list = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
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
        data_manager.write_table_to_file("sales/sales.csv", table)
    else:
        ui.print_error_message("There is no such option.")
    return table


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    prices = []
    lowest_ids = []
    for row in table:
        prices.append(int(row[2]))
    for row in table:
        if int(row[2]) == min(prices):
            lowest_ids.append(row[0])
            
    N = len(lowest_ids)
    iteration = 1
    while iteration < N:
        j = 0
        while j <= (N-2):
            if lowest_ids[j] < lowest_ids[j+1]:
                temp = lowest_ids[j+1]
                lowest_ids[j+1] = lowest_ids[j]
                lowest_ids[j] = temp
                j += 1
            else:
                j += 1
        iteration += 1
    return str(lowest_ids[0])


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    date_from = (year_from, month_from, day_from)
    date_to = (year_to, month_to, day_to)
    between_dates = []
    filtered_table = []
    for i in range(len(table)):
        actual_month = int(table[i][3])
        actual_day = int(table[i][4])
        actual_year = int(table[i][5])
        actual_date = (actual_year, actual_month, actual_day)
        if (date_from) < (actual_date) < (date_to):
            between_dates.append(list(actual_date))
    for i in range(len(table)):        
        for date in between_dates:
            table[i][5] = int(table[i][5])
            table[i][3] = int(table[i][3])
            table[i][4] = int(table[i][4])
            table[i][2] = int(table[i][2])
            if date[0] == table[i][5] and date[1] == table[i][3] and date[2] == table[i][4]:
                filtered_table.append(table[i])
    return filtered_table