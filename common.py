# implement commonly used functions here

import random
import string


# generate and return a unique and random string
# other expectations:
# - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation.

    Args:
        table: list containing keys. Generated string should be different then all of them

    Returns:
        Random and unique string
    """

    generated = ''
    a = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    b = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    symbols = ["!","@","#","$","%","^","&","*","(",")","?"]
    c = ''.join(random.choice(symbols) for i in range(2))
    d = ''.join(random.choice(string.digits) for i in range(2))
    generated = a+d+b+c
    return generated


def id_list(table):
    ids = []
    for row in table:
        ids.append(row[0])
    return ids
