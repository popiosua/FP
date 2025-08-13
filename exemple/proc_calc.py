"""
   A teacher (client) needs a program for students (users) who learn or use rational numbers.
  The program shall help students to make basic arithmetic operation
"""


def gcd(a, b):
    """
    Return the greatest common divisor of two positive integers.
    a,b integer numbers
    return an integer number, the  greatest common divisor of a and b
    """
    if a < 0 or b < 0:
        raise ValueError("a and b must be greater than 0")
    if a == 0 and b == 0:
        raise ValueError("gcd(0, 0) is undefined")
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def rational_add(a1, a2, b1, b2):
    """
    Return the sum of two rational numbers.
    a1,a2,b1,b2 integer numbers, a2<>0 and b2<>0
    return a list with 2 integer numbers, representing a rational number a1/b2 + b1/b2
    Raise ValueError if the denominators are zero.
    """
    if a2 == 0 or b2 == 0:
        raise ValueError("0 denominator not allowed")
    c = [a1 * b2 + a2 * b1, a2 * b2]
    d = gcd(c[0], c[1])
    c[0] = c[0] / d
    c[1] = c[1] / d
    return c

#we store here the current total of the calculator
calc_total = [0, 1]
#we store here a history of current totals (for undo)
undolist = []

def calc_get_total():
    """
      Current total
      return a list with 2 elements representing a rational number
    """
    return calc_total

def undo():
    """
      Undo the last user operation
      post: restore the previous current total
      raise ValueError if no operation is available
    """
    global undolist
    global calc_total
    if len(undolist)==0:
        raise ValueError("No operation to restore")
    calc_total = undolist[-1]
    undolist = undolist[:-1]

def undoCalc():
    """
      Undo the last user operation
      post: restore the previous current total      
    """
    try:
        undo()
    except ValueError as e:
        print(e)
        
def calc_add(a, b):
    """
      add a rational number to the current total
      a, b integer number, b<>0
      post: add a/b to the current total
    """
    global undolist
    global calc_total
    #add the current total to the undo list
    undolist.append(calc_total)
    calc_total = rational_add (calc_total[0], calc_total[1], a, b)


def reset_calc():
    """
      Reset the calculator
      post: the curent total equal 0/1
    """
    global calc_total
    calc_total = [0, 1]

    global undolist
    undolist = []

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
    
def addToCalc():
    """
      Read a rational number and add to the current total
    """
    m = input("Give nominator:")
    n = input("Give denominator:")
    try:
        calc_add (int(m), int(n))        
    except ValueError:
        print ("Enter integers for m, n, with not null n")
        
def run():
    """
      Implement the user interface
    """
    reset_calc()
    finish = False    
    while not finish:
        printCurrent()
        printMenu()
        m = input().strip()
        if (m == 'x'):
            finish = True
        elif (m == '+'):
            addToCalc()
        elif (m=='c'):
            reset_calc()            
        elif (m=='u'):
            undoCalc()
        else:
            print ("Invalid command")

    print ("By!!!")


### test cases

def test_gcd():
    """
      test function for gdc
    """
    assert gcd(0, 2) == 2
    assert gcd(2, 0) == 2
    assert gcd(2, 3) == 1
    assert gcd(2, 4) == 2
    assert gcd(6, 4) == 2
    assert gcd(24, 9) == 3
    try:
        gcd(-2, 0)
        assert False
    except ValueError:
        assert True
    try:
        gcd(0, -2)
        assert False
    except ValueError:
        assert True
    try:
        gcd(0, 0)
        assert False
    except ValueError:
        assert True
        

def test_rational_add():
    """
      Test function for rational_add
    """
    assert rational_add(1, 2, 1, 3) == [5, 6]
    assert rational_add(1, 2, 1, 2) == [1, 1]

def test_calculator_add():
    """
      Test function for calculator_add
    """
    reset_calc()
    assert calc_get_total() == [0, 1]
    calc_add(1, 2)
    assert calc_get_total() == [1, 2]
    calc_add(1, 3)
    assert calc_get_total() == [5, 6]
    calc_add(1, 6)
    assert calc_get_total() == [1, 1]

def test_undo():
    """
      Test function for undo
    """
    reset_calc()
    calc_add(1, 3)
    undo()
    assert calc_get_total() == [0, 1]
    reset_calc()
    calc_add(1, 3)
    calc_add(1, 3)
    calc_add(1, 3)
    undo()
    assert calc_get_total() == [2, 3]


#run the test - invoke the test function
test_gcd()

test_rational_add()
test_calculator_add()
test_undo()

run()
