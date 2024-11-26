TEST = False
in_file = "./resources/day_24_test.txt" if TEST else "./resources/day_24_input.txt"

import numpy as np
from z3 import Solver, Int, IntVector

if TEST:
    lb = 7
    ub = 27
else:
    lb = 200000000000000
    ub = 400000000000000

def file_lines():
    with open(in_file) as file:
        particles = []
        for line in file:
            """Custom iteration logic goes here"""
            line = line.strip()
            pos, dir = line.split(" @ ")
            pos = [int(i) for i in pos.split(", ")]
            dir = [int(i) for i in dir.split(", ")]
            particles.append((pos, dir))
        return particles


def question_1():
    """Answer to the first question of the day"""
    particles = file_lines()

    equations = [([-dir[1]/dir[0], 1], pos[1] - dir[1]/dir[0] * pos[0]) for pos, dir in particles]

    count = 0
    for i, line_a in enumerate(equations):
        for j, line_b in enumerate(equations[i+1:]):
            xy = np.array([line_a[0], line_b[0]])
            c = np.array([line_a[1], line_b[1]])
            try:
                intersection = np.linalg.solve(xy, c)
            except:
                print("lines don't intersesct")
                continue
            x, y = intersection

            pos_i, dir_i = particles[i]
            pos_j, dir_j = particles[i+j+1]

            if ((x - pos_i[0]) * dir_i[0] > 0 and
                (x - pos_j[0]) * dir_j[0] > 0 and
                 lb <= x <= ub and lb <= y <= ub):
                count += 1

    return count


def question_2():
    """Answer to the second question of the day"""
    particles = file_lines()

    # Define symbolic variables
    ts = IntVector("t", len(particles))
    px = Int('px')
    py = Int('py')
    pz = Int('pz')
    vx = Int('vx')
    vy = Int('vy')
    vz = Int('vz')

    s = Solver()

    for t, (position, velocity) in zip(ts, particles):
        x, y, z = position
        v1, v2, v3 = velocity

        s.add(px + t * vx == x + t * v1)
        s.add(py + t * vy == y + t * v2)
        s.add(pz + t * vz == z + t * v3)

    s.check()
    m = s.model()

    px_value = int(str(m[px]))
    py_value = int(str(m[py]))
    pz_value = int(str(m[pz]))

    return px_value + py_value + pz_value


if __name__ == '__main__':
    answer_1 = question_1()
    print(f"Question 1 answer is: {answer_1}")

    answer_2 = question_2()
    print(f"Question 2 answer is: {answer_2}")
