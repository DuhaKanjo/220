"""
Name: Duha Kanjo
lab2.py

"""
import math
def sum_of_threes():
    bound = eval (input ("enter the bound:"))
    total = 0
    for x in range(0,bound+1,3):
        total = total + x
    print (total)


def multiplication_table():
    for h in range (1,11):
        for L in range (1,11):
            print(h * L, end=" ")
        print()

def triangle_area():
    a = eval (input ("Enter a:"))
    b = eval (input ("Enter b:"))
    c = eval (input ("Enter c:"))
    s = (a+b+c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print (A)

def sumSquares():
    low = eval(input("enter low:"))
    high = eval(input("enter high:"))
    acc = 0
    for x in range (low, high + 1):
       acc = x**2+acc
    print(acc)

def power():
    base = eval (input("enter base:"))
    exponent = eval (input("enter exponent:"))
    acc = 1
    for x in range(exponent):
        acc*= base
    print(acc)
