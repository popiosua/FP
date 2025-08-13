"""
  The user interface of the calculator
  Contains functions related to the user interaction (console)
"""
from domain.calculator import *


def printMenu():
    """
      Print out the main menu of the calculator
    """
    print ("Calculator menu:")
    print ("   + for adding a rational number")
    print ("   c to clear the calculator")
    print ("   u to undo the last operation")
    print ("   x to close the calculator")

def printCurrent():
    """
      Print the current total
    """
    print ("Total:", calc_get_total())

def run():
    """
      Implement the user interface
    """
    reset_calc()
    finish = False
    printCurrent()
    while not finish:
        printMenu()

        m = input().strip()
        if (m == 'x'):
            finish = True
        elif (m == '+'):
            m = input("Give nominator:")
            n = input("Give denominator:")
            try:
                calc_add (int(m), int(n))
                printCurrent()
            except ValueError:
                print ("Enter integers for m, n, with not null n")
        elif (m=='c'):
            reset_calc()
            printCurrent()
        elif (m=='u'):
            undo()
            printCurrent()
        else:
            print ("Invalid command")

    print ("By!!!")
