import sys
import os
import ui  # User Interface
# Store module
from store import store
# Human Resources module
from hr import hr
# Tool manager module
from inventory import inventory
# Accounting module
from accounting import accounting
# Sales module
from sales import sales
# Customer Relationship Management (CRM) module
from crm import crm
# Data Analyser module
from data_analyser import data_analyser


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        os.system("clear")
        store.start_module()
    elif option == "2":
        os.system("clear")
        hr.start_module()
    elif option == "3":
        os.system("clear")
        inventory.start_module()
    elif option == "4":
        os.system("clear")
        accounting.start_module()
    elif option == "5":
        os.system("clear")
        sales.start_module()
    elif option == "6":
        os.system("clear")
        crm.start_module()
    elif option == "7":
        os.system("clear")
        data_analyser.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Store manager",
               "Human resources manager",
               "Inventory manager",
               "Accounting manager",
               "Sales manager",
               "Customer Relationship Management (CRM)",
               "Data Analyser"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
