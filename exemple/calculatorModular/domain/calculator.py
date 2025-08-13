"""
  Calculator module, contains functions related to the calculator
"""

from domain.rational import *


calc_total = [0, 1]
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
    """
    global undolist
    global calc_total
    calc_total = undolist[-1]
    undolist = undolist[:-1]

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


test_rational_add()
test_calculator_add()
test_undo()
