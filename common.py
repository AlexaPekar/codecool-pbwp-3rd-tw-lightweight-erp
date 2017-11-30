# implement commonly used functions here

import random
import string
import ui


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)

def generate_random(table):
    generated = ''
    a = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    b = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
    c = ''.join(random.choice(symbols) for i in range(2))
    d = ''.join(random.choice(string.digits) for i in range(2))
    generated = a + d + b + c
    return generated


def id_list(table):
    ids = []
    for row in table:
        ids.append(row[0])
    return ids


def asc_order(list):

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
