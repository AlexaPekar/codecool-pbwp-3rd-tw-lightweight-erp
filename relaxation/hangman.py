import random
import sys
import os
import tty
import termios
import pygame
from time import sleep


def read_file(file, list):
    if os.stat(file).st_size == 0:
        print("The " + file + " file is empty!")
        sys.exit()
    else:
        with open(file, "r") as f:
            words = f.read().splitlines()
            for word in words:
                list.append(word)


def start_name():
    print(" *** First game of the team CodeIN, all rights reserved! ***")
    print("First of all, type your fancy name!")
    name = input("Name: ")
    print("\nHello " + name + "!" + "\n" + "Welcome in our hangman game, play carefully and have fun!")


def instructions():
    instructions = """
    Instructions:
        1. You have 6 shots, use them wisely!
        2. You're going to play in your personally chosen wordlist.
        3. You can type a letter without pressing enter.
        4. In some cases you have to use accentuated letters too!
        5. Have FUN!
    """
    print(instructions)


def ascii_result(result):
    art1 = """
 _     __ ____   _    _      _       ____    _____  ______   _
 \ \   / // __ \ | |  | |    | |     / __ \  / ____||  ____|| |
  \ \_/ /| |  | || |  | |    | |    | |  | || (___  | |__   | |
   \   / | |  | || |  | |    | |    | |  | | \___ \ |  __|  | |
    | |  | |__| || |__| |    | |____| |__| | ____) || |____ |_|
    |_|   \____/  \____/     |______|\____/ |_____/ |______|(_)
    """
    art2 = """
 __     __ ____   _    _     __          __ ____   _   _  _
 \ \   / // __ \ | |  | |    \ \        / // __ \ | \ | || |
  \ \_/ /| |  | || |  | |     \ \  /\  / /| |  | ||  \| || |
   \   / | |  | || |  | |      \ \/  \/ / | |  | || . ` || |
    | |  | |__| || |__| |       \  /\  /  | |__| || |\  ||_|
    |_|   \____/  \____/         \/  \/    \____/ |_| \_|(_)
    """
    if result == "won":
        print(art2)
    elif result == "lose":
        print(art1)


def random_word():
    random_num = random.randint(0, len(words) - 1)
    random_word = words[random_num]
    return random_word


def lists_reset(list1, list2, list3):
    list1.clear()
    list2.clear()
    list3.clear()


def listing_wordtolist(list_word_ch, list_hideword):
    get_word = random_word()
    i = 0
    while(i < len(get_word)):
        list_word_ch.append(get_word[i])
        underline = "_"
        replace = list_word_ch[i].replace(list_word_ch[i], underline)
        list_hideword.append(replace)
        i = i + 1


def hiddenlist_display(list_hideword):
    for i in list_hideword:
        print(i, end=" ")


def display_solve(list_word_ch):
    for i in list_word_ch:
        print(i, end="")


def used_letters(list_input_letters):
    str_list = ','.join(list_input_letters)
    print("\nAlready used letters:", str_list)


def hangman_graphic(missed_tries):
    graphic = [
        "\n________    \n",
        "|      |    \n",
        "|           \n",
        "|           \n",
        "|           \n",
        "|             "
    ]

    if missed_tries == 0:
        print("".join(graphic))
    elif missed_tries == 1:
        graphic[2] = "|      O    \n"
        print("".join(graphic))
    elif missed_tries == 2:
        graphic[2] = "|      O    \n"
        graphic[3] = "|     /     \n"
        print("".join(graphic))
    elif missed_tries == 3:
        graphic[2] = "|      O    \n"
        graphic[3] = "|     /|    \n"
        print("".join(graphic))
    elif missed_tries == 4:
        graphic[2] = "|      O    \n"
        graphic[3] = "|     /|\   \n"
        print("".join(graphic))
    elif missed_tries == 5:
        graphic[2] = "|      O    \n"
        graphic[3] = "|     /|\   \n"
        graphic[4] = "|     /     \n"
        print("".join(graphic))
    else:
        graphic[2] = "|      O    \n"
        graphic[3] = "|     /|\   \n"
        graphic[4] = "|     / \   \n"
        print("".join(graphic))
        print("\nIt was: ")
        display_solve(list_word_ch)
        print("\n\nGAME OVER!")
        ascii_result("lose")
        play_sound("relaxation/mortal.wav", 4)


def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def play_sound(sound_file, sleep_sec=0):
    pygame.mixer.pre_init()
    pygame.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    sleep(sleep_sec)


def listing_triedletters(list_hideword, list_word_ch, list_input_letters, used_letters):
    missed_tries = 0
    print("\nI have a word with " + str(len(list_hideword)) + " letters\n")
    hiddenlist_display(list_hideword)
    hangman_graphic(missed_tries)

    while(missed_tries < 6):
        if(list_hideword == list_word_ch):
            ascii_result("won")
            play_sound("relaxation/victory.wav", 14)
            break

        # letter_in = input("\nType a letter: ").upper()
        print("Type a letter: ")
        letter_in = getchar().upper()

        os.system("clear")
        instructions()

        if letter_in.isalpha():
            if(letter_in in list_input_letters):
                print("\nThis letter is already used! Type another one, please.")
            else:
                list_input_letters.append(letter_in)

            used_letters(list_input_letters)

            if letter_in not in list_word_ch:
                missed_tries += 1
            else:
                j = 0
                while (j < len(list_word_ch)):
                    if(list_word_ch[j] == letter_in):
                        list_hideword[j] = list_word_ch[j]
                        j += 1
                    else:
                        j += 1
            hiddenlist_display(list_hideword)
            hangman_graphic(missed_tries)
        else:
            print("Only alphabetic characters please!")


words = []
read_file("relaxation/words.txt", words)


list_word_ch = []  # empty list for random word, character by character
list_hideword = []  # empty list for random word, hidden characters
list_input_letters = []  # empty list for tried letters


def play_whole_game():
    while True:
        start_name()
        instructions()
        listing_wordtolist(list_word_ch, list_hideword)
        listing_triedletters(list_hideword, list_word_ch, list_input_letters, used_letters)

        lists_reset(list_word_ch, list_hideword, list_input_letters)

        replay = input("\nWould you to like play again? (y/n)")
        if replay == "y":
            os.system("clear")
            instructions()
            random_word()
            listing_wordtolist(list_word_ch, list_hideword)
            listing_triedletters(list_hideword, list_word_ch, list_input_letters, used_letters)
        else:
            play_sound("relaxation/byebye.wav", 5)
            print("See you next time!")
            os.system('clear')
            break
