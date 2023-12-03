
N_RED = 12
N_GREEN = 13
N_BLUE = 14

def question_1():
    with open("./day_2_input.txt") as file:
        total = 0
        for i, line in enumerate(file):
            is_ok = True
            line = line.replace(";", ",")
            line = line.replace(":", ",")
            line = line.strip("\n")
            line = line.split(", ")

            is_ok = checker(line[1:])

            if is_ok:
                print(i+1)
                total += i+1


            print(i+1, line[1:])
        print(total)


def checker(games):
    is_ok = True
    for string in games:
        if "red" in string:
            string = string.strip(" red")
            if int(string) > N_RED:
                is_ok = False

        if "green" in string:
            string = string.strip(" green")
            if int(string) > N_GREEN:
                is_ok = False

        if "blue" in string:
            string = string.strip(" blue")
            if int(string) > N_BLUE:
                is_ok = False

    return is_ok


def question_2():
    with open("./day_2_input.txt") as file:
        power = 0
        for i, line in enumerate(file):
            is_ok = True
            line = line.replace(";", ",")
            line = line.replace(":", ",")
            line = line.strip("\n")
            line = line.split(", ")

            power += calculate_power(line[1:])


        print(power)

def calculate_power(line):
    red_power = 0
    green_power = 0
    blue_power = 0
    for string in line:
        if "red" in string:
            string = string.strip(" red")
            if int(string) > red_power:
                red_power = int(string)

        if "green" in string:
            string = string.strip(" green")
            if int(string) > green_power:
                green_power = int(string)

        if "blue" in string:
            string = string.strip(" blue")
            if int(string) > blue_power:
                blue_power = int(string)

    return red_power * green_power * blue_power