"""
Name: Duha Kanjo
lab8
Functions.py
"""
from seperate_file import encode_better

def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1

    for lines in infile:
        new_line = lines.split()
        for word in new_line:
            outfile.write(str(i) + "" + word + "\n")
            i += 1
    infile.close()
def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write("".join(new_line)+ "\n")
    infile.close()
def calc_check_sum(isbn):
    isbn =isbn.split()
    sum = 0
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10-i)
        sum += num
    return sum%11
def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".py", "w+")
    for line in infile:
        outfile.write(line+"\n")

def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt" , "w+")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "\n")

def encode(message, key):
    acc = ""
    for i in message:
        x = ord(i)
        y = x + key
        z = chr(y)
        acc += z
    return acc

def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".py", "w")
    for line in infile:
        outfile.write(line + "\n")

def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".py" , "w")
    padfile = open(pad, "r")
    key = padfile.read()
    for line in infile:
        new_line = encode_better(line, key)
        outfile.write(new_line + "\n")




def main():
    number_words("infile.py", "happy.py" )
    hourly_wages("hourly_wage_txt.py", "five.py")
    calc_check_sum("0072946520")
    send_message("infile.py", "sami.txt")
    send_safe_message("infile.py", "Duha", 1234)
    send_uncrackable_message("seperate_file.py", "sam", "pad.txt.py")

main()





