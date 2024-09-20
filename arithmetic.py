import random, math
import sys

result1, result2 = '', ''
l1_score = 0
l2_score = 0
level1_disc = 'simple operations with numbers 2-9'
level2_disc = 'integral squares of 11-29'
while True:
    try:
        level = int(input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n'''))
        if level > 2:
            print('Incorrect format.')
        elif level == 1:
            for i in range(5):
                L1_task = f"{random.randint(2, 9)} {random.choice('+-*')} {random.randint(2, 9)}"
                print(L1_task)
                while True:
                    try:
                        if int(input()) == eval(L1_task):
                            print('Right!')
                            l1_score += 1
                            break
                        else:
                            print('Wrong!')
                            break

                    except Exception:
                        print('Incorrect format.')
            result1 = f'{l1_score}/5'

            break
        elif level == 2:
            for i in range(5):
                l2_task = random.randint(11, 29)
                print(l2_task)
                while True:
                    try:


                        if int(input()) == (l2_task * l2_task):
                            print('Right!')
                            l2_score += 1
                            break


                        else:
                            print('Wrong!')
                            break

                    except Exception:
                        print('Wrong format! Try again.')
            result2 = f'{l2_score}/5'

    except Exception:
        print('Incorrect format')

    finally:
        if result1:
           save_file = input(f'Your mark is {result1}. Would you like to save the result? Enter yes or no.\n')
           if save_file.lower() == 'yes' or save_file == 'y':
                name = input('What is your name?\n')
                with open('results.txt', 'a') as file:
                    file.write(f'{name}: {result1} in level {level} ({level1_disc})\n')
                    print('The results are saved in "results.txt".')
        if result2:
           save_file = input(f'Your mark is {result2}. Would you like to save the result? Enter yes or no.\n')
           if save_file.lower() == 'yes' or save_file == 'y':
                name = input('What is your name?\n')
                with open('results.txt', 'a') as file:
                    file.write(f'{name}: {result2} in level {level} ({level2_disc})\n')
                print('The results are saved in "results.txt".')