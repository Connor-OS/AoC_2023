TEST = False
in_file = "./resources/day_15_test.txt" if TEST else "./resources/day_15_input.txt"


def file_lines():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split(",")
            for i in line:
                yield i

def file_lines_2():
    with open(in_file) as file:
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            line = line.split(",")
            for i in line:
                if "-" in i:
                    yield i[:-1], i[-1:]
                else:
                    yield i[:-2], i[-2:]


def question_1():
    """Answer to the first question of the day"""
    total = 0
    for line in file_lines():
        total += hash(line)
    return total


def hash(line):
    answer = 0
    for char in line:
        answer += ord(char)
        answer *= 17
        answer = answer % 256
    return answer


def question_2():
    """Answer to the second question of the day"""
    boxes = {}

    for label, action in file_lines_2():
        box_hash = hash(label)
        if "-" in action:
            if box := boxes.get(box_hash):
                boxes[box_hash] = [i for i in box if label not in i]
        else:
            if box := boxes.get(box_hash):
                replace = False
                for i, lens in enumerate(box):
                    if label in lens:
                        box[i] = (label, action)
                        replace = True
                if not replace:
                    box.append((label, action))
                boxes[box_hash] = box
            else:
                boxes[box_hash] = [(label, action)]

    total = 0
    for box, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            answer = 0
            _, focal = lens
            answer += (box+1)*(i+1)*int(focal.strip("="))
            total += answer

    return total


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
