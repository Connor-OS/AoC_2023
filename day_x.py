TEST = True
in_file = "./resources/day_4_test.txt" if TEST else "./resources/day_4_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            yield line


def question_1():
    """Answer to the first question of the day"""
    answer = None
    for line in file_lines():
        print(line)

    return answer


def question_2():
    """Answer to the second question of the day"""
    answer = None

    return answer


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    # answer_2 = question_2()
    # print(f"Question 2 answer is: {answer_2}")
