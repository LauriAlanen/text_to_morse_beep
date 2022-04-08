import winsound
import os
from time import sleep

debugging = 0

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": "!"}


def encrypt():
    encrypted_msg = []

    print("If you want to quit type !q")
    words = input("Gimme some words so i can do the morse thing...")

    if words == "!q":
        quit()

    else:
        try:
            for letter in words:
                if letter == " ":
                    encrypted_msg.append(MORSE_CODE_DICT[letter])
                else:
                    morse_letter = MORSE_CODE_DICT[letter.capitalize()]
                    encrypted_msg.append(morse_letter)
                encrypted_msg.append("#")

        except KeyError:
            print("Make sure that the input didn't include any special letters.")
            sleep(2)

    beep_rules(encrypted_msg)

def clear():
    os.system('cls')

def beep_rules(encrypted_list):
    str1 = " "

    dot_interval = 65 # This effects how long the beeping and break intervals are.
    dash_interval = dot_interval * 3
    between_letter = dot_interval * 3  # Marked as #
    between_words = dot_interval * 7  # Marked as !
    FREQ = 1000 # This changes the frequency of the beeps in HZ

    encrypted_string = str1.join(encrypted_list)
    if debugging == 1:
        print(encrypted_string)

    for letter in encrypted_string:
        if letter == ".":
            print(letter)
            winsound.Beep(FREQ, dot_interval)
        if letter == "-":
            print(letter)
            winsound.Beep(FREQ, dash_interval)
        if letter == "#":
            print("Between Letter Break")
            sleep(between_letter / 1000)
        if letter == "!":
            print("Between Words Break")
            sleep(dot_interval / 1000)





while True:
    encrypt()
    if debugging == 0:
        clear()
