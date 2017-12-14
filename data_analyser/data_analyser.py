# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        options = ["Get the last buyer name", "Get the last buyer ID", "Get the buyer's name spent the most and the amount of money spent", "Get the buyer's ID spent the most and the amount of money spent", "Get the most frequent buyers' names", "Get the most frequent buyers' IDs"]
        ui.print_menu("\nData analyser menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            ui.print_result(get_the_last_buyer_name(), "Name of the last buyer:")
        elif option == "2":
            ui.print_result(get_the_last_buyer_id(), "ID of the last buyer:")
        elif option == "3":
            ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), "Name of the buyer spent the most and the amount of money spent:")
        elif option == "4":
            ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(), "ID of the buyer spent the most and the amount of money spent:")
        elif option == "5":
            number_of_buyers = ui.get_inputs(["Please enter the number of buyers to display: "], "")
            ui.print_result(get_the_most_frequent_buyers_names(int(number_of_buyers[0])), "Name(s) of the most frequent buyer(s):")
        elif option == "6":
            number_of_buyers = ui.get_inputs(["Please enter the number of buyers to display: "], "")
            ui.print_result(get_the_most_frequent_buyers_ids(int(number_of_buyers[0])), "ID(s) of the most frequent buyer(s):")
        elif option == "0":
            break
        else:
            ui.print_error_message("There is no such option.")


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """
    result = get_the_last_buyer_id()
    name = crm.get_name_by_id(result)
    return name


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """
    sale_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(sale_id)
    return customer_id
        

def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """
    result_tuple = get_the_buyer_id_spent_most_and_the_money_spent()
    name = crm.get_name_by_id(result_tuple[0])
    result_list = list(result_tuple)
    result_list[0] = name
    return tuple(result_list)
    

def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """
    result = []
    money_spent_by_customers = []
    ids_dict = sales.get_all_sales_ids_for_customer_ids()
    for key, value in ids_dict.items():
        ids_dict[key] = sales.get_the_sum_of_prices(ids_dict[key])
        money_spent_by_customers.append(ids_dict[key])
        max_money_spent = max(money_spent_by_customers)
    for key, value in ids_dict.items():
        if max_money_spent == ids_dict[key]:
            result.append(key)
            result.append(max_money_spent)
    return tuple(result)


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """
    result = get_the_most_frequent_buyers_ids(num)
    for i in range(len(result)):
        result[i] = list(result[i])
        name = crm.get_name_by_id(result[i][0])
        result[i][0] = name
        result[i] = tuple(result[i])
    return result


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """
    result = []
    all_customers = []
    number_of_sales = []
    customer_sales = sales.get_num_of_sales_per_customer_ids()
    for i in sorted(customer_sales, key=customer_sales.get, reverse=True):
        all_customers.append(tuple([i, customer_sales[i]]))
    if num > len(all_customers):
        num = len(all_customers)
    for i in range(0, num):
        result.append(all_customers[i])
    return result
