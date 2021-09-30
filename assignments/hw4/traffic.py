"""
Name: Duha Kanjo
traffic.py
certification of authenticity:
I certify that this assignment is entirely my own work.
"""
# we need to make nested loop
# first loop should have the number of roads
# second loop should have the number of days
def main():
    number_of_roads = eval(input("How many roads were surveyed?"))
    acc = 0
    for i in range(1, number_of_roads + 1):
        number_of_days = eval(input("How many days was road" + str(i) + "surveyed?"))
        acc1 = 0
        for j in range(1, number_of_days + 1):
            number_of_cars = eval(input("How many cars traveled on day" + str(j) + "?"))
            acc += number_of_cars
            acc1 += number_of_cars
            answer1 = round((acc1 / number_of_days), 2)
            answer2 = round((acc / number_of_roads), 2)
        print("Road" + str(i) + "average vehicles per day:" + str(answer1))
    print("Total number of vehicles traveled on all roads:", acc)
    print("Average number of vehicles per road:", answer2)

if __name__ == '__main__':
    main()
