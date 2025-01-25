from MorseCode import CODE
import os
import winsound
from time import sleep

freq = 550  # Hz
dotLength = 60  # milliseconds
dashLength = dotLength * 3
pauseWords = dotLength * 7


def beep(dur):
    """
       makes noise for specific duration.
       :param dur: duration of beep in milliseconds
    """
    winsound.Beep(freq, dur)


def pause(dur):
    """
        pauses audio for dur milliseconds
        :param dur: duration of pause in milliseconds
    """
    sleep(dur / 1000)


def playMorseAudio(morse):
    """
        plays audio conversion of morse string using inbuilt windows module.
        :param morse: morse code string.
    """
    for char in morse:
        if char == '.':
            beep(dotLength)
        elif char == '-':
            beep(dashLength)
        elif char == '/':
            pause(pauseWords)
        else:
            # char is blank space
            pause(dashLength)


def printMenu():
    print(
        "\t███╗░░░███╗░█████╗░██████╗░░██████╗███████╗  ░█████╗░░█████╗░██████╗░███████╗\n"
        "\t████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██╔════╝\n"
        "\t██╔████╔██║██║░░██║██████╔╝╚█████╗░█████╗░░  ██║░░╚═╝██║░░██║██║░░██║█████╗░░\n"
        "\t██║╚██╔╝██║██║░░██║██╔══██╗░╚═══██╗██╔══╝░░  ██║░░██╗██║░░██║██║░░██║██╔══╝░░\n"
        "\t██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗  ╚█████╔╝╚█████╔╝██████╔╝███████╗\n"
        "\t╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝")
    print('---------MENU----------')
    print('1. Text to MorseCode')
    print('2. MorseCode to Text')
    print('3. MorseCode List')
    print('0. Exit')


while True:
    os.system('cls')
    printMenu()
    user_choice = int(input("Please choose one option here: "))

    if user_choice == 1:
        while True:
            user_text = input("Your text: ").upper()
            morse_code = ''
            for c in user_text:
                for character, code in CODE.items():
                    if c == character:
                        morse_code += code
                        morse_code += ' '
            print('Morse Code: ', morse_code)
            playMorseAudio(morse_code)
            while True:
                isContinued = input('Text to MorseCode, Continue? (y/n): ').lower()
                if isContinued in ['y', 'n']:
                    break
                else:
                    print(f'Your input {isContinued} is incorrect')
            if isContinued == 'n':
                break
    elif user_choice == 2:
        while True:
            user_code = input("Your morse code: ").split()
            text = ''
            for code in user_code:
                for character, morse_code in CODE.items():
                    if code == morse_code:
                        text += character
            print('Text: ', text)
            while True:
                isContinued = input('MorseCode to Text, Continue? (y/n): ').lower()
                if isContinued in ['y', 'n']:
                    break
                else:
                    print(f'Your input {isContinued} is incorrect')
            if isContinued == 'n':
                break
    elif user_choice == 3:
        for character, code in CODE.items():
            if character == ' ':
                print("SPACE", " ", code)
                continue
            print(character, " ", code)
    elif user_choice == 0:
        print('Have a good day!')
        break
