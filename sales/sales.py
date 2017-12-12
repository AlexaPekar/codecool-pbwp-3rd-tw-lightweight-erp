# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made
# customer_id: string, id from the crm

# importing everything you need
import os
import ui
import data_manager
import common


def start_module():
    while True:
        datas = data_manager.get_table_from_file("sales/sales.csv")
        options = [
            "Display table",
            "Add",
            "Remove",
            "Update",
            "The id of the item sold for the lowest price",
            "Items are sold between two given dates"]
        ui.print_menu("\nSales menu", options, "Main menu")
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
            ui.print_result(get_lowest_price_item_id(datas), "is the result of the 1st sales extra function.")
        elif option == "6":
            date_list = ui.get_inputs(["Month from: ", "Day from: ", "Year from: ",
                                       "Month to: ", "Day to: ", "Year to: "], "Please add the dates!")
            ui.print_result(
                get_items_sold_between(
                    datas, int(
                        date_list[0]), int(
                        date_list[1]), int(
                        date_list[2]), int(
                        date_list[3]), int(
                            date_list[4]), int(
                                date_list[5])), "")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    module_headers = ["ID", "Title", "Price", "Month", "Day", "Year","Customer ID"]
    return common.common_show_table(table, module_headers)


def add(table):
    module_headers = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    return common.common_add(table, module_headers)


def write_to_file(table):
    return common.common_write_to_file(table, "sales/sales.csv")


def remove(table, id_):
    return common.common_remove(table, id_, "sales/sales.csv")


def update(table, id_):
    module_headers = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    return common.common_update(table, id_, "sales/sales.csv", module_headers)


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
        while j <= (N - 2):
            if lowest_ids[j] < lowest_ids[j + 1]:
                temp = lowest_ids[j + 1]
                lowest_ids[j + 1] = lowest_ids[j]
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
        if date_from < actual_date < date_to:
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


    # your code

    pass

# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    pass


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    # your code

    pass


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    # your code

    pass


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    # your code

    pass


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    # your code

    pass


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    # your code

    pass


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    # your code

    pass


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code

    pass

