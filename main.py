############################################   -== INFORMATION ==-   ############################################

#### THE PROGRAM WAS CREATED AND PUBLISHED BY:
#### https://github.com/viktorsynek
#### https://www.linkedin.com/in/viktor-synek/

#############################################   -== PROGRAM ==-   ###############################################

#IMPORT LIBRARIES
import time

def factorial(num):
    result = 1
    # EXAMPLE: 5! = 2 * 3 * 4 * 5 = 120
    for i in range(2, num + 1):
        result *= i
    print(result)

def another():
    # IF USER INPUTS "N" THE PROGRAM STOPS
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()
    
def start():
    print("Give me a number, I'll give the factorial of it: ")
    time.sleep(1)
    try:
        # THE USER GIVES A NUMBER
        n = int(input("Input: "))
        time.sleep(1)
        factorial(n)
        another()
    # HANDLE NOT NUMERIC INPUTS
    except ValueError:
        print("That's not a number!")
        time.sleep(1)
        start()

start()
