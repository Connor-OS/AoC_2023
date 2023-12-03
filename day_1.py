numbers = ["1","2","3","4","5","6","7","8","9","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number_map = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

from copy import deepcopy as copy

def question_1():
    with open("./day_1_input.txt") as f:
        total = 0
        for line in f:
            for letter in line:
                if letter in numbers:
                    number_1 = letter
                    break
            for letter in line[::-1]:
                if letter in numbers:
                    number_2 = letter
                    break
            total += int(number_1 + number_2)
    print(total)
def question_2():
    lines = []
    with open("./day_1_input.txt") as f:
        for line in f:
            lines.append(line)


    for word in number_map.items():

        for i, line in enumerate(lines):
            lines[i] = line.replace(word[0], f"{word[0]}{word[1]}{word[0]}")

    for line in lines:
        print(line)

    total = 0
    for line in lines:
        for letter in line:
            if letter in numbers:
                number_1 = letter
                if number_1 in number_map.keys():
                    number_1 = number_map[number_1]
                break
        for letter in line[::-1]:
            if letter in numbers:
                number_2 = letter
                if number_2 in number_map.keys():
                    number_2 = number_map[number_2]
                break
        total += int(number_1 + number_2)
    print(total)