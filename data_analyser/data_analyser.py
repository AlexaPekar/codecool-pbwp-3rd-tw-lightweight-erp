import os
import ui
import common
from sales import sales
from crm import crm


def start_module():
    while True:
        options = ["Get the last buyer name", "Get the last buyer ID", "Get the buyer's name spent the most and the amount of money spent", "Get the buyer's ID spent the most and the amount of money spent", "Get the most frequent buyers' names", "Get the most frequent buyers' IDs", "Get the name of the customers who did not buy anything"]
        ui.print_menu("\nData analyser menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            os.system("clear")
            ui.print_result(get_the_last_buyer_name(), "Name of the last buyer:")
        elif option == "2":
            os.system("clear")
            ui.print_result(get_the_last_buyer_id(), "ID of the last buyer:")
        elif option == "3":
            os.system("clear")
            ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), "Name of the buyer spent the most and the amount of money spent:")
        elif option == "4":
            os.system("clear")
            ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent(), "ID of the buyer spent the most and the amount of money spent:")
        elif option == "5":
            os.system("clear")
            number_of_buyers = ui.get_inputs(["Please, enter the number of buyers to display: "], "")
            ui.print_result(get_the_most_frequent_buyers_names(int(number_of_buyers[0])), "Name(s) of the most frequent buyer(s):")
        elif option == "6":
            os.system("clear")
            number_of_buyers = ui.get_inputs(["Please, enter the number of buyers to display: "], "")
            ui.print_result(get_the_most_frequent_buyers_ids(int(number_of_buyers[0])), "ID(s) of the most frequent buyer(s):")
        elif option == "7":
            os.system("clear")
            ui.print_result(get_names_no_sale_belongs_to(), "Name(s) of person(s) who did not buy anything:")
        elif option == "0":
            os.system("clear")
            break
        else:
            ui.print_error_message("There is no such option.")


def get_the_last_buyer_name():
    result = get_the_last_buyer_id()
    name = crm.get_name_by_id(result)
    return name


def get_the_last_buyer_id():
    sale_id = sales.get_item_id_sold_last()
    customer_id = sales.get_customer_id_by_sale_id(sale_id)
    return customer_id
        

def get_the_buyer_name_spent_most_and_the_money_spent():
    result_tuple = get_the_buyer_id_spent_most_and_the_money_spent()
    name = crm.get_name_by_id(result_tuple[0])
    result_list = list(result_tuple)
    result_list[0] = name
    return tuple(result_list)
    

def get_the_buyer_id_spent_most_and_the_money_spent():
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
    result = get_the_most_frequent_buyers_ids(num)
    for i in range(len(result)):
        result[i] = list(result[i])
        name = crm.get_name_by_id(result[i][0])
        result[i][0] = name
        result[i] = tuple(result[i])
    return result


def get_the_most_frequent_buyers_ids(num=1):
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


def get_names_no_sale_belongs_to():
    get_all_sales_for_customer = sales.get_all_sales_ids_for_customer_ids()
    content_of_table = common.get_crm_table()
    have_bought = True
    list_of_buyers_ids = []
    not_buyers_id = []
    not_buyers = []
    for key, value in get_all_sales_for_customer.items():
        if get_all_sales_for_customer[key] != []:
            have_bought = True
            list_of_buyers_ids.append(key)
        else:
            have_bought = False
            not_buyers.append(key)

    for i in range(len(content_of_table)):
        if content_of_table[i][0] not in list_of_buyers_ids:
            not_buyers_id.append(content_of_table[i][0])
    for id in not_buyers_id:
        not_buyers.append(crm.get_name_by_id(id))
    return not_buyers

