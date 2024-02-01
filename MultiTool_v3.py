import random
import time
import os
import pyautogui as pt
import msvcrt
import tkinter as tk
from colorama import Fore

while True:

    os.system('cls')

    print(Fore.RED + '''                                                         
                        
                            ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
                            ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                            ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
                            ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
                            ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗    - v3
                            ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝    - © Ayush Sahu
                                                                                                    
                                          
''')

    try:
        userName = open("username.txt", "rt")
        userNameRiyal = userName.readline()
        print(Fore.GREEN +
              '''             
                               _______________________________________________________________________________
                              |                                                                               |
                              |  [ 1 ] Calculator                             [ 2 ] Addition of 1+2+3+4...+n  |
                              |                                                                               |
                              |  [ 3 ] Squares from 1 to n                    [ 4 ] Table of 'n'              |
                              |                                                                               |
                              |  [ 5 ] Guess the number                       [ 6 ] Roll a dice               |
                              |                                                                               |
                              |  [ 7 ] Spammer                                [ 8 ] Check if Leap year        |
                              |                                                                               |
                              |  [ 9 ] Check no. of vowel & consonant                                         |
                              |                                                                               |
                              |                                                                               |
                              |                                   [ q ] QUIT                                  |
                              |_______________________________________________________________________________|
  
          Hello {0}! Press any of the keys stated above to proceed...            
                      '''.format(userNameRiyal)
              )
    except:
        userName = open("username.txt", "at")
        userNameA = input(Fore.LIGHTGREEN_EX + "\n\nHello user! What's your Name/Username??  ")
        userName.write(userNameA)
        print('Press any key to continue...')
        msvcrt.getch()


    def getKey():
        key = msvcrt.getch()
        return key.decode('utf-8')

    def checkKey():
        while True:
            key = getKey()
            if key.isdigit():
                return int(key)
            else:
                return key
    choice_start = checkKey()

    if choice_start == 1:
        os.system('cls')
        print('**Calculator opened... If you cant see it please check the TASKBAR...**')

        calculation = ""

        def addToCalc(symbol):

            global calculation
            calculation += str(symbol)
            text_result.delete(1.0 , "end")
            text_result.insert(1.0, calculation)

        def evalCalc():
            global calculation
            try:
                calculation = str(eval(calculation))
                text_result.delete(1.0, 'end')
                text_result.insert(1.0, calculation)

            except:
                clearField()
                text_result.insert(1.0, 'Error')

        def clearField():
            global calculation
            calculation = ''
            text_result.delete(1.0, 'end')

        root = tk.Tk()
        root.geometry('400x375')
        text_result = tk.Text(root, height = 2, width = 16, font = ('Arial', 24))
        text_result.grid(columnspan = 5)
        btn_1 = tk.Button(root, text = '1', command = lambda: addToCalc(1), width = 5, font = ('Arial', 14))
        btn_1.grid(row = 2, column = 1 )

        btn_2 = tk.Button(root, text = '2', command = lambda: addToCalc(2), width = 5, font = ('Arial', 14))
        btn_2.grid(row = 2, column = 2 )

        btn_3 = tk.Button(root, text = '3', command = lambda: addToCalc(3), width = 5, font = ('Arial', 14))
        btn_3.grid(row = 2, column = 3 )

        btn_4 = tk.Button(root, text = '4', command = lambda: addToCalc(4), width = 5, font = ('Arial', 14))
        btn_4.grid(row = 3, column = 1 )

        btn_5 = tk.Button(root, text = '5', command = lambda: addToCalc(5), width = 5, font = ('Arial', 14))
        btn_5.grid(row = 3, column = 2 )

        btn_6 = tk.Button(root, text = '6', command = lambda: addToCalc(6), width = 5, font = ('Arial', 14))
        btn_6.grid(row = 3, column = 3 )

        btn_7 = tk.Button(root, text = '7', command = lambda: addToCalc(7), width = 5, font = ('Arial', 14))
        btn_7.grid(row = 4, column = 1 )

        btn_8 = tk.Button(root, text = '8', command = lambda: addToCalc(8), width = 5, font = ('Arial', 14))
        btn_8.grid(row = 4, column = 2 )

        btn_9 = tk.Button(root, text = '9', command = lambda: addToCalc(9), width = 5, font = ('Arial', 14))
        btn_9.grid(row = 4, column = 3 )

        btn_0 = tk.Button(root, text = '0', command = lambda: addToCalc(0), width = 5, font = ('Arial', 14))
        btn_0.grid(row = 5, column = 2 )

        btn_plus = tk.Button(root, text = '+', command = lambda: addToCalc('+'), width = 5, font = ('Arial', 14))
        btn_plus.grid(row = 2, column = 4 )

        btn_subt = tk.Button(root, text = '-', command = lambda: addToCalc('-'), width = 5, font = ('Arial', 14))
        btn_subt.grid(row = 3, column = 4 )

        btn_mult = tk.Button(root, text = 'x', command = lambda: addToCalc('*'), width = 5, font = ('Arial', 14))
        btn_mult.grid(row = 4, column = 4 )

        btn_div = tk.Button(root, text = '÷', command = lambda: addToCalc('/'), width = 5, font = ('Arial', 14))
        btn_div.grid(row = 5, column = 4 )

        btn_openp = tk.Button(root, text = '(', command = lambda: addToCalc('('), width = 5, font = ('Arial', 14))
        btn_openp.grid(row = 5, column = 1 )

        btn_closep = tk.Button(root, text = ')', command = lambda: addToCalc(')'), width = 5, font = ('Arial', 14))
        btn_closep.grid(row = 5, column = 3 )

        btn_equal = tk.Button(root, text = '=', command = evalCalc, width = 11, font = ('Arial', 14))
        btn_equal.grid(row = 6, column = 3, columnspan = 2 )

        btn_clear = tk.Button(root, text = 'C', command = clearField, width = 11, font = ('Arial', 14))
        btn_clear.grid(row = 6, column = 1, columnspan = 2 )

        root.mainloop()

    elif choice_start == 2:

        os.system('cls')

        print('Addition of 1+2+3+4...till n')

        n = int(input("Enter the value of n: "))

        sumConsN = (n * (n + 1)) / 2

        print("The answer is {0}".format(sumConsN))

        print('\n\nPress any key to continue:')
        msvcrt.getch()
        continue

    elif choice_start == 3:

        os.system('cls')

        print(Fore.CYAN + '''

                                                ██████╗ ██╗    ██╗███████╗
                                                ██╔══██╗██║    ██║██╔════╝
                                                ██║  ██║██║ █╗ ██║███████╗
                                                ██║  ██║██║███╗██║╚════██║
                                                ██████╔╝╚███╔███╔╝███████║
                                                ╚═════╝  ╚══╝╚══╝ ╚══════╝      (*Dealing with squares*)
                          
                          

              
              ''')
        print(Fore.YELLOW + 'Available options:' + Fore.RED + '\n\t(' + Fore.MAGENTA + '1' + Fore.RED + ')' + Fore.LIGHTGREEN_EX + ' Square any number' + Fore.RED + '\n\t(' + Fore.MAGENTA + '2' + Fore.RED + ')' + Fore.LIGHTGREEN_EX + ' Find Sq Root of any number' + Fore.RED + '\n\t(' + Fore.MAGENTA + '3' + Fore.RED + ')' + Fore.LIGHTGREEN_EX + ' Print Squares from 1 to n' + Fore.RED + '\n\t(' + Fore.MAGENTA + 'Q/q' + Fore.RED + ')' + Fore.LIGHTGREEN_EX + 'Go back')
        dws_ch = getKey()
        if dws_ch == 1:
            os.system('cls')
            sq = int(input('Enter the number:'))
            print('The answer is ', sq*sq)
            time.sleep(6.9)
    elif choice_start == 4:

        os.system('cls')

        print(Fore.CYAN + 'Print multiplication table of any number.')

        n = int(input(Fore.LIGHTBLUE_EX + 'Enter the number: '))
        i = 1

        while i <= 10:
            a = i * n
            print('{} * {} = {}'.format(n, i, a))
            i += 1

    elif choice_start == 5:

        os.system('cls')

        print()

        while True:

            print(Fore.LIGHTBLUE_EX + '''Choose the difficulty:
1 - Easy (1-10)
2 - Medium (1-25)
3 - Hard (1-75)
4 - Ultra Hard (1-150)
5 - Extreme (1-200)
6 - Impossible (1-500)
7 - Go back

Enter your option: ''' + Fore.RESET)

            while True:
                try:
                    difficulty = int(msvcrt.getch())
                    break

                except:
                    print(Fore.MAGENTA + 'Error : Please enter a number...' + Fore.RESET)
                    time.sleep(2)
                    continue

            if difficulty == 1:
                ans = random.randint(1, 10)
                tries = 0
                while True:
                    tries = tries + 1
                    guess = int(input(Fore.CYAN + "Guess the number: " + Fore.RESET))
                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")
                        print(Fore.MAGENTA + 'Press any key to continue...' + Fore.RESET)
                        msvcrt.getch()
                    break


            elif difficulty == 2:
                ans = random.randint(1, 25)
                tries = 0
                while True:
                    tries = tries + 1
                    guess = int(input(Fore.CYAN + "Guess the number: "))
                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")
                        print(Fore.MAGENTA + 'Press any key to continue...')
                        msvcrt.getch()
                        break

            elif difficulty == 3:
                ans = random.randint(1, 75)
                tries = 0
                while True:
                    tries = tries + 1
                    guess = int(input(Fore.CYAN + "Guess the number: "))
                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")
                        print(Fore.MAGENTA + 'Press any key to continue...')
                        msvcrt.getch()
                        break

            elif difficulty == 4:
                ans = random.randint(1, 150)
                tries = 0
                while True:
                    tries = tries + 1
                    guess = int(input(Fore.CYAN + "Guess the number: "))
                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")
                        print(Fore.MAGENTA + 'Press any key to continue...')
                        msvcrt.getch()
                        break

            elif difficulty == 5:
                ans = random.randint(1, 200)
                tries = 0
                while True:
                    tries = tries + 1
                    guess = int(input(Fore.CYAN + "Guess the number: "))
                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")
                        print(Fore.MAGENTA + 'Press any key to continue...')
                        msvcrt.getch()
                        break

            elif difficulty == 6:

                ans = random.randint(1, 500)

                tries = 0

                while True:

                    tries = tries + 1

                    guess = int(input(Fore.CYAN + "Guess the number: "))

                    if guess == ans:
                        print(Fore.YELLOW + 'The answer was {0}! It took you'.format(ans), tries, "tries to guess it.")

                        print(Fore.MAGENTA + 'Press any key to continue...')
                        msvcrt.getch()
                        break

            if difficulty == 7:
                break

            else:
                print(Fore.CYAN + 'Invalid Input')
                time.sleep(2)
                break

    elif choice_start == 6:

        os.system('cls')

        print(Fore.LIGHTBLUE_EX + 'Roll a dice...')

        while True:

            ch = getKey()

            if ch == '\r':
                dice = random.randint(1, 6)

                print(Fore.CYAN + 'The dice rolled {0}'.format(dice))

            elif ch == 'Q' or ch == 'q':
                break

        continue

    elif choice_start == 7:

        os.system('cls')

        print(Fore.GREEN + 'Message Spammer')

        limit = int(input(Fore.LIGHTRED_EX + "Enter limit:"))

        message = input(Fore.LIGHTRED_EX + "Enter message:")

        i = 0

        print(Fore.LIGHTCYAN_EX + 'The program wil wait for 10 seconds now, till then open the messaging app...')

        time.sleep(10)
        os.system('cls')
        print(Fore.LIGHTYELLOW_EX + 'Spamming...')
        while i <= int(limit):
            pt.typewrite(message)
            time.sleep(0.2)
            pt.press("enter")

            i += 1

        print(Fore.CYAN + 'Spamming done. Press any key to continue...')
        msvcrt.getch()
        continue

    elif choice_start == 8:

        os.system('cls')
        time.sleep(0.5)
        while True:
            year = int(input(Fore.CYAN + 'Enter the year or enter 0 to exit: '))

            if year == 0:
                break

            if ((year % 400 == 0) or
                (year % 100 != 0) and
                (year % 4 == 0)):
                    print(Fore.YELLOW + "Given Year is a leap Year")
                    time.sleep(1)
                    continue

            else:
                print(Fore.YELLOW + "Given Year is not a leap Year")
                time.sleep(1)
                continue


    elif choice_start == 9:

        os.system('cls')
        string = input(Fore.LIGHTGREEN_EX + "Enter your Word/Sentence: ")
        vowels = ['a', 'e', 'e', 'i', 'o', 'A', 'E', 'I', 'O', 'U']
        vowels_count = 0
        cons_count = 0
        for char in string:
            if char.isalpha():
                if char in vowels:
                    vowels_count += 1

                else:
                    cons_count += 1

        print(Fore.YELLOW + f'Number of Vowels: {vowels_count}')
        print(Fore.YELLOW + f'Number of consonants: {cons_count}')
        print(Fore.CYAN + '\n\nPress any key to continue...')
        msvcrt.getch()

        os.system('cls')
        time.sleep(0.5)
        continue

    elif choice_start == 'Q' or choice_start == 'q':

        time.sleep(0.5)
        break

    else:

        os.system('cls')
        print(Fore.GREEN + "Invalid input.")

        time.sleep(2)
        continue
