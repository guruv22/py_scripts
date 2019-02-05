#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    #val = round(meal_cost + (tip_percent*int(meal_cost)/100) + (tax_percent*int(meal_cost)/100))
    val = int(round(meal_cost + (tip_percent*meal_cost/100) + (tax_percent*meal_cost/100)))
    print val

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)

