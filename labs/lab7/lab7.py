"""
Name: Duha Kanjo

lab7.py
"""
import math

def cash_conversion():
    x = eval(input("enter an integer: "))
    print('${:.2f}'. format(x))

def encode():
    message = input(" enter the message :")
    key = eval(input("enter the key :"))
    acc = ""
    for i in message:
        x = ord(i)
        y = x + key
        z = chr(y)
        acc += z
    print(acc)

def encode_better():
    s = input("enter the message")
    k = input("enter the key")
    acc = ''
    for i in range(len(s)):
        c = s[i]
        key = k[i]
        key = ord(key) -97
        y = ord(c) + key
        z = chr(y)
        acc += z
    print(acc)

def sphereArea(radius):
    return 4 * math.pi * radius **2
def sphereVolum(radius):
    return (4/3) * math.pi * radius **3


def sumN(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
def sumCubes(n):
    total = 0
    for i in range(1, n+1):
        total  = i**3
    return total

def main():
    print(sphereVolum(5))
    print(sphereArea(2))
    print(sumN(6))
    print(sumCubes(7))
    encode_better()
    encode()
    cash_conversion()
main()
