import time

def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    print(result)

def another():
    print("Do you want to try another? (Y/N)")
    another = input("Input: ").lower()
    
    while another != "n" and another != "y":
        another = input("Input: ").lower()

    start() if another == "y" else exit()
def start():
    print("Give me a number, I'll give the factorial of it: ")
    time.sleep(1)
    try:
        n = int(input("Input: "))
        time.sleep(1)
        factorial(n)
        another()
    except ValueError:
        print("That's not a number!")
        time.sleep(1)
        start()

start()
