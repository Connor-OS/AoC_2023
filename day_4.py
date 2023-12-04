TEST = False
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4_input.txt"


def question_1(lines):
    """Answer to the first question of the day"""
    lines = lines.splitlines()
    total = 0
    for line in lines:
        score = 0
        line = line.split(":")[1]
        win_numbers, my_numbers = line.split("|")

        win_numbers = win_numbers.strip().split()
        my_numbers = my_numbers.strip().split()

        for num in win_numbers:
            if num in my_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total += score

    return total


def question_2(lines):
    """Answer to the second question of the day"""
    lines = lines.splitlines()
    copies = [1] * len(lines)
    pos = 0
    for line, copy in zip(lines, copies):

        matches = 0
        line = line.split(":")[1]
        win_numbers, my_numbers = line.split("|")

        win_numbers = win_numbers.strip().split()
        my_numbers = my_numbers.strip().split()

        for num in win_numbers:
            if num in my_numbers:
                matches += 1

        for i in range(1, matches + 1):
            copies[pos + i] += 1 * copy
        pos += 1

    return sum(copies)


if __name__ == '__main__':
    with open(in_file) as data:
        answer = question_1(data.read())
        print(answer)

    with open(in_file) as data:
        answer = question_2(data.read())
        print(answer)
