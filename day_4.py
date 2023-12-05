TEST = True
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            line = line.split(":")[1]
            win_numbers, my_numbers = line.split("|")
            win_numbers = win_numbers.strip().split()
            my_numbers = my_numbers.strip().split()
            yield win_numbers, my_numbers


def file_length():
    with open(in_file) as file:
        return len([i for i in file])


def question_1():
    """Answer to the first question of the day"""
    total = 0
    for win_numbers, my_numbers in file_lines():
        score = 0
        for num in win_numbers:
            if num in my_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2

        total += score

    return total


def question_2():
    """Answer to the second question of the day"""

    copies = [1] * file_length()
    pos = 0
    for line, copy in zip(file_lines(), copies):
        win_numbers, my_numbers = line

        matches = 0
        for num in win_numbers:
            if num in my_numbers:
                matches += 1

        for i in range(1, matches + 1):
            copies[pos + i] += 1 * copy
        pos += 1
    return sum(copies)


if __name__ == '__main__':
    answer = question_1()
    print(answer)

    answer = question_2()
    print(answer)
