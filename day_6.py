TEST = False
in_file = "./resources/day_6_test.txt" if TEST else "./resources/day_6_input.txt"

A = 1 #mm3


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split(":")[1]
            line = line.split()
            line = [int(i) for i in line]

            yield line


def file_lines2():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split(":")[1]
            line = line.split()
            line = "".join(line)
            line = int(line)

            yield line


def question_1():
    """Answer to the first question of the day"""
    a = []
    for i in file_lines():
        a.append(i)
    time, dist = a

    races = []
    for t,d in [i for i in zip(time,dist)]:
        print(t,d)
        total = 0
        for v in range(1, t-1):
            if win := v*(t-v) > d:
                print(v)
                print(win)
                total += 1
        races.append(total)

    answer = races[0]
    for i in races[1:]:
        answer *= i
    return answer


def question_2():
    """Answer to the second question of the day"""
    a = []
    for i in file_lines2():
        a.append(i)
    time, dist = a

    upper = int(time/2)
    lower = 0
    mid = int((upper + lower) / 2)
    while (upper-lower) > 1:
        mid = int((upper + lower) / 2)
        if mid*(time-mid) > dist:
            upper = mid
        else:
            lower = mid

    return time - 2*(mid-1)-1


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
