def print_table(table, title_list):
    table.insert(0, title_list)
    maxlength = []
    for column in range(len(table[0])):
        length = 0
        for row in range(len(table)):
            if len(str(table[row][column])) > length:
                length = len(str(table[row][column]))
        maxlength.append(length)

    for row_i in range(len(table)):
        row = table[row_i]
        print()
        for cell_j in range(len(row)):
            cell = row[cell_j]
            width = maxlength[cell_j]
            print(" | " + cell.center(width) + " | ", end='')



def print_result(result, label):
    print(result, label)


def print_menu(title, list_options, exit_message):
    print(title)
    for i in range(0, len(list_options)):
        print("    (" + str(i + 1) + ") " + list_options[i])
    print("    (0) " + exit_message)


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for label in list_labels:
        user_input = input(label)
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    print(message)
