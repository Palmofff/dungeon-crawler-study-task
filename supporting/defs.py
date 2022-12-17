from time import *
def print_slow(string):
    for letter in string:
        print(letter, end='', flush=True)
        sleep(0.04)
    print("")
def input_slow(string):
    for letter in string:
        print(letter, end='', flush=True)
        sleep(0.04)
    print("", end="")
    
