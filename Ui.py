'''
An example of the user interface
'''

import random
import time

if __name__ == '__main__':
    while True:
        print("What ingredient do you want included?: ", end=" ")
        inp = input()

        # if user inputs ingredient
        if inp.isalpha():
            # write word to recipes.txt
            f = open("recipes.txt", "w")
            f.write(inp)
            f.close()

            time.sleep(10.0)

            # read recipe from text file
            f = open("recipes.txt", "r")
            line = f.read()
            print(line)

