import os
import ui
import data_manager
import common
import sys
import webbrowser
from relaxation import game_2048_play
from relaxation import hangman


def start_module():
    while True:
        datas = data_manager.get_table_from_file("accounting/items.csv")
        options = ["Listen relaxing music", "Play 2048 game", "Watch memes", "Play HangMan game"]
        ui.print_menu("\nRelaxation Menu", options, "Main menu")
        inputs = ui.get_inputs(["Please, choose an option: "], "")
        option = inputs[0]
        if option == "1":
            os.system("clear")
            play_relax_music()
        elif option == "2":
            os.system("clear")
            play_2048_game()
        elif option == "3":
            os.system("clear")
            open_memes()
        elif option == "4":
            os.system("clear")
            play_hangman_game()
        elif option == "0":
            os.system("clear")
            break
        else:
            ui.print_error_message("There is no such option.")


def play_relax_music():
    webbrowser.open("https://www.youtube.com/watch?v=vx6EPrL_HlI&list=PLQkQfzsIUwRYx6DUfckrwbHMelJZs8wmg")


def play_2048_game():
    game_2048_play.play_whole_game()


def play_hangman_game():
    hangman.play_whole_game()


def open_memes():
    webbrowser.open("https://9gag.com/tag/programming?ref=search")
