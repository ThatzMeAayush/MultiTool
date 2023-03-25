import random
import time
import os
import pyautogui as pt

6
while True:

       os.system('cls')

       print('''
                                                                          © Ayush Sahu
 ███▄ ▄███▓ █    ██  ██▓  ▄▄▄█████▓ ██▓▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██    ▓██░▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▒██    ▒██ ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒   ░██▒▒▒█████▓ ░██████▒▒██▒ ░ ░██░  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓    ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░    ░░░ ░ ░   ░ ░   ░       ▒ ░  ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
       ░      ░         ░  ░        ░               ░ ░      ░ ░      ░  ░
                                                                          
''')


       print('''
Hello there fellow user! Here's a list of what you can do in this program ->
1 - Add, Subtract, Multiply or divide 2 numbers.
2 - Add, Subtract, Multiply or divide 3 numbers
3 - Addition of 1+2+3+4...till n.
4 - Print squares of numbers from 1 to n.
5 - Print multiplication table of any number.
6 - Number guessing game.
7 - Roll a dice.
8 - Message spammer.
Or press 9 to quit
''')
       choice_strt = int(input("\n Enter your choice : "))
       if choice_strt == 8:
              break
       elif choice_strt == 1:
              os.system('cls')

              print('Add, Subtract, Multiply or divide 2 numbers')

              no1 = int(input('Enter the first number : '))
              no2 = int(input('Enter the second number : '))
              op = input("Enter the operation, +, -, *, / (gives quotient) or % (gives remainder) : ")
              if op == "+":
                     plus = no1 + no2
                     print("Your answer is {0}.".format(plus))
                     time.sleep(5)
                     continue
              
              elif op == "-":
                     sub = no1 - no2
                     print("Your answer is {0}.".format(sub))
                     time.sleep(5)
                     continue

              elif op == "*":
                     mult = no1 * no2
                     print('Your answer is {0}'.format(mult))
                     time.sleep(5)
                     continue

              elif op == "/":
                     div = no1 / no2
                     print('Your answer is {0}'.format(div))
                     time.sleep(5)
                     continue

              elif op == "%":
                     mod = no1 % no2
                     print('Your answer is {0}'.format(mod))
                     time.sleep(5)
                     continue

       elif choice_strt == 2:

              os.system('cls')

              print('Add, Subtract, Multiply or divide 3 numbers')

              no1 = int(input("Enter the first number: "))

              no2 = int(input('Enter the second number: '))

              no3 = int(input('Enter the third number: '))

              op = input("Enter the operation, +, -, *, / (gives quotient) or % (gives remainder) :")

              if op == "+":
                     plus = no1 + no2
                     plus1 = plus + no3
                     print("Your answer is {0}.".format(plus1))
                     time.sleep(5)
                     continue
              
              elif op == "-":
                     sub = no1 - no2
                     sub1 = sub - no3
                     print("Your answer is {0}.".format(sub1))
                     time.sleep(5)
                     continue

              elif op == "*":
                     mult = no1 * no2
                     mult1 = mult * no3
                     print('Your answer is {0}'.format(mult1))
                     time.sleep(5)
                     continue

              elif op == "/":
                     div = no1 / no2
                     div1 = div / no3
                     print('Your answer is {0}'.format(div1))
                     time.sleep(5)
                     continue

              elif op == "%":
                     mod = no1 % no2
                     mod1 = mod % no3
                     print('Your answer is {0}'.format(mod1))
                     time.sleep(5)
                     continue

       elif choice_strt == 3:

              os.system('cls')

              print('Addition of 1+2+3+4...till n')

              n = int(input("Enter the value of n: "))

              sumConsN = (n*(n+1))/2

              print("The answer is {0}".format(sumConsN))

              time.sleep(5)
              continue

       elif choice_strt == 4:

              os.system('cls')

              print('Print squares of numbers from 1 to n')

              n = int(input("Enter the value of n: "))

              i = 1

              

              while i <= n:
                     
                     isq = i*i

                     print("{0} squared is ".format(i), isq)
                     
                     i += 1
              
              time.sleep(5)
              continue
       
       elif choice_strt == 5:
              
              os.system('cls')

              print('Print multiplication table of any number.')

              n = int(input('Enter the number: '))
              i = 1

              while i<=10:
                     
                     a = i*n
                     print('{} * {} = {}'.format(n,i,a))

       elif choice_strt == 6:

              os.system('cls')

              print('Number guessing game...')

              while True:

                     difficulty = int(input('''Choose the difficulty:
1 - Easy (1-10)
2 - Medium (1-50)
3 - Hard (1-100)
4 - Ultra Hard (1-150)
5 - Extreme (1-200)
6 - Impossible (1-500)
7 - Go back
              
Enter your option: '''))

                     if difficulty == 1:
                            ans = random.randint(1,10)
                            tries = 0
                            while True: 
                                   tries = tries + 1
                                   guess = int(input("Guess the number: "))
                                   if guess == ans:
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          time.sleep(3)
                                          break

                     elif difficulty == 2:
                            ans = random.randint(1,50)
                            tries = 0
                            while True: 
                                   tries = tries + 1
                                   guess = int(input("Guess the number: "))
                                   if guess == ans:
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          time.sleep(3)
                                          break

                     elif difficulty == 3:
                            ans = random.randint(1,100)
                            tries = 0
                            while True: 
                                   tries = tries + 1
                                   guess = int(input("Guess the number: "))
                                   if guess == ans:
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          time.sleep(3)
                                          break

                     elif difficulty == 4:
                            ans = random.randint(1,150)
                            tries = 0
                            while True: 
                                   tries = tries + 1
                                   guess = int(input("Guess the number: "))
                                   if guess == ans:
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          time.sleep(3)
                                          break

                     elif difficulty == 5:
                            ans = random.randint(1,200)
                            tries = 0
                            while True: 
                                   tries = tries + 1
                                   guess = int(input("Guess the number: "))
                                   if guess == ans:
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          time.sleep(3)
                                          break

                     elif difficulty == 6:
                            
                            ans = random.randint(1,500)
                            
                            tries = 0
                            
                            while True: 
                                   
                                   tries = tries + 1
                                   
                                   guess = int(input("Guess the number: "))
                                   
                                   if guess == ans:
                                          
                                          print('The answer was {0}! It took you'.format(ans),tries,"tries to guess it.")
                                          
                                          time.sleep(3)
                                          
                                          break

                     if difficulty == 7:
                            
                            time.sleep(1)
                            
                            break

                     else:
                            
                            print('Invalid input.')
                            
                            time.sleep(2)
                            
                            break

       elif choice_strt == 7:

              os.system('cls')

              print('Roll a dice')

              while True:
              
                     ch = int(input("Press 1 to roll dice or 0 to exit the dice.: "))

                     if ch == 1:
                            dice = random.randint(1,6)

                            print('The dice rolled {0}'.format(dice))

                     elif ch == 0:

                            break

              time.sleep(2)
              
              continue

       elif choice_strt == 8:

              os.system('cls')

              print('Message Spammer')

              limit = input("Enter limit:")
              
              message = input("Enter message:")
              
              i = 0
              
              print('The program wil wait for 7 seconds now, till then open the messaging app...')
              
              time.sleep(7)

              while i <= int(limit):
                     
                     pt.typewrite(message)     

                     pt.press("enter")

                     i+=1

              time.sleep(5)
              continue
       
       elif choice_strt == 9:
              
              time.sleep(2)
              break
       
       else:
              
              print("Invalid input.")

              time.sleep(2)
              continue
