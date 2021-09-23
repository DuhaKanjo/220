"""
Name: Duha Kanjo
means.py

problem: calculate monthly interest charge.

certification of authenticity:
I certify that this assignment is entirely my own work.
"""
import math
# first we need to ask the user to enter the number of the values
# second we use for loop to ask the user to give the values
# third we need to compute the mean
# then we square root the mean to get the rms average and we round the answer
# the harmonic mean = to the total number of value over the accumulator of x starting with 0
# the geometric mean = the accumulator starting with 1 to the power of the reciprocal of the
# number of value
# last step is to round all the answers to the 1000tn
def main():
    value = eval(input("enter the value to be entered"))
    acc1 = 0
    acc2 = 0
    acc3 = 1
    for i in range(value):
        entered_values = eval(input("enter value" + str(i+1) + ":"))
        acc1 = acc1 + (entered_values ** 2)
        rms_average = round(math.sqrt(acc1/value), 3)
        acc2 = acc2 + 1 / entered_values
        harmonic_mean = round(value / acc2, 3)
        acc3 *= entered_values
        geometric_mean = round(acc3 ** (1/value), 3)
    answer1 = round(rms_average, 3)
    answer2 = round(harmonic_mean, 3)
    answer3 = round(geometric_mean, 3)

    print(answer1)
    print(answer2)
    print(answer3)
