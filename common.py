import random
import string
import ui
import data_manager


def generate_random(table):
    generated = ''
    a = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    b = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    c = ''.join(random.choice(symbols) for i in range(2))
    d = ''.join(random.choice(string.digits) for i in range(2))
    generated = a + d + b + c
    return generated


def collect_ids(table):
    ids = []
    for row in table:
        ids.append(row[0])
    return ids


def sort_list_in_asc(list):

    N = len(list)
    iteration = 1
    while iteration < N:
        j = 0
        while j <= (N - 2):
            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp
                j += 1
            else:
                j += 1
        iteration += 1


def common_update(table, id_, file_name, header_list):
    new_items = []
    ids = collect_ids(table)
    if id_[0] in ids:
        new_items.append(id_[0])
        new_elements = ui.get_inputs(header_list, "Please add the items")
        for item in new_elements:
            new_items.append(item)
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table[i] = new_items
    else:
        ui.print_error_message("There is no such option.")
    return table


def common_add(table, header_list):
    random_id = generate_random(table)
    inputs = ui.get_inputs(header_list, "Please add the items")
    inputs.insert(0, random_id)
    table.append(inputs)
    return table


def common_show_table(table, header_list):
    return ui.print_table(table, header_list)


def common_remove(table, id_, file_name):
    ids = collect_ids(table)
    if id_[0] in ids:
        for i in range(len(table)):
            if table[i][0] == id_[0]:
                table.pop(i)
                break
    else:
        ui.print_error_message("There is no such option.")
    return table


def common_write_to_file(table, file_name):
    return data_manager.write_table_to_file(file_name, table)


def get_crm_table():
    table = data_manager.get_table_from_file("crm/customers.csv")
    return table


def get_sales_table():
    table = data_manager.get_table_from_file("sales/sales.csv")
    return table