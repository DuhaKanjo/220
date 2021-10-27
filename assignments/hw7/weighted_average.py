"""
Duha Kanjo
weighted_average.py
certification of authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    names = 0
    total_average = 0
    for line in infile:
        line_list = line.split(':')
        line_list = line_list[1].split()
        name = line.split(':')[0]

        weg = line_list[0:len(line_list):2]
        acc = 0
        for i in weg:
            integer_weight = int(i)
            acc = acc + integer_weight

        if acc == 100:
            names += 1
            first = 0
            acc1 = 0
            for i in range(0, len(line_list), 2):
                each_two = line_list[first:]
                product = int(each_two[0]) * int(each_two[1])
                first = first + 2
                acc1 += product
            weg = acc1/100
            rounded_weg = round(weg, 1)

            total_average += weg
            outfile.write(name + "'s average: " + str(rounded_weg) + "\n")
        else:
            if acc < 100:
                outfile.write(name + "'s average" + ":" + " Error: The weights are less than 100.\n")
            else:
                outfile.write(name + "'s average" + ":" + " Error: The weights are more than 100.\n")

    final_answer = round(total_average / names, 1)
    outfile.write("Class average" + ":" + " " + str(final_answer) + "\n")


def main():
    weighted_average("grades.txt", "avg.txt")


if __name__ == '__main__':
    main()



