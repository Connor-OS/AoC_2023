TEST = False
in_file = "./resources/day_22_test.txt" if TEST else "./resources/day_22_input.txt"

from copy import deepcopy as copy

class Brick:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def bottom(self):
        return min(self.z1, self.z2)

    def top(self):
        return max(self.z1, self.z2)

    def drop(self):
        self.z1 -= 1
        self.z2 -= 1


    def __str__(self):
        return f"x1 {self.x1}-{self.x2}, y1 {self.y1}-{self.y2}, z1 {self.z1}-{self.z2}"


def file_lines():
    with open(in_file) as file:
        bricks = []
        for line in file:
            """Custom iteration logic goes here"""
            b1, b2 = line.strip().split("~")

            b1 = [int(i) for i in b1.split(",")]
            b2 = [int(i) for i in b2.split(",")]
            bricks.append(Brick(*b1, *b2))

    return bricks


def question_1():
    """Answer to the first question of the day"""
    bricks = file_lines()

    bricks = sorted(bricks, key=lambda x: x.bottom())

    # construct pile of bricks
    brick_pile = []
    for brick in bricks:
        brick_pile.append(drop_brick(brick, brick_pile))

    brick_pile = sorted(brick_pile, key=lambda x: x.bottom())

    resting = {brick:[] for brick in brick_pile}
    for i, brick in enumerate(brick_pile):
        for other_brick in brick_pile[:i]:
            if brick.bottom() - other_brick.top() == 1 and collision(brick, other_brick):
                resting[brick].append(other_brick)

    final_arrangement = {brick: resting for brick, resting in resting.items()}

    for brick in resting:
        if len(resting[brick]) == 1:
            if resting[brick][0] in final_arrangement:
                final_arrangement.pop(resting[brick][0])


    return len(final_arrangement)


def drop_brick(brick, brick_pile):
    brick_pile = sorted(brick_pile, key=lambda x: x.top(), reverse=True)

    for top_brick in brick_pile:
        while brick.bottom() > top_brick.top()+1:
            brick.drop()
        if collision(top_brick, brick):
            brick_pile.append(brick)
            return brick

    while brick.bottom() > 1:
        brick.drop()
    brick_pile.append(brick)
    return brick


def collision(b1, b2):
    if (max(b1.x1, b1.x2) >= min(b2.x1, b2.x2) and max(b2.x1, b2.x2) >= min(b1.x1, b1.x2)
    and max(b1.y1, b1.y2) >= min(b2.y1, b2.y2) and max(b2.y1, b2.y2) >= min(b1.y1, b1.y2)):
        return True


def question_2():
    """Answer to the second question of the day"""
    bricks = file_lines()

    bricks = sorted(bricks, key=lambda x: x.bottom())

    # construct pile of bricks
    brick_pile = []
    for brick in bricks:
        brick_pile.append(drop_brick(brick, brick_pile))

    brick_pile = sorted(brick_pile, key=lambda x: x.bottom())

    structure = {brick:[] for brick in brick_pile}
    for i, brick in enumerate(brick_pile):
        for other_brick in brick_pile[:i]:
            if brick.bottom() - other_brick.top() == 1 and collision(brick, other_brick):
                structure[brick].append(other_brick)

    total = 0
    for i in range(len(structure)):
        print(i)
        collapse_structure = copy(structure)
        brick = [_ for _ in collapse_structure.keys()][i]

        total += collapse(brick, collapse_structure)
    return total


# @cache
def collapse(collapse_brick, structure):
    collapse_total = 0
    for brick in structure:
        if collapse_brick in structure[brick]:
            structure[brick].remove(collapse_brick)
            if structure[brick] == []:
                collapse_total += 1
                collapse_total += collapse(brick, structure)
    return collapse_total


if __name__ == '__main__':
    # answer_1 = question_1()
    # print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
