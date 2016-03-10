#!/usr/bin/env python

from pulp import *

def solve(x_0, x_1, x_2, x_3, x_4, x_5, day):
    prob = LpProblem("best fit curve for temps in corvallis", LpMinimize)

    # LP variables
    x0 = LpVariable("x0", int(x_0))
    x1 = LpVariable("x1", int(x_1))
    x2 = LpVariable("x2", int(x_2))
    x3 = LpVariable("x3", int(x_3))
    x4 = LpVariable("x4", int(x_4))
    x5 = LpVariable("x5", int(x_5))

    # Objective
    prob += x0 + \
           (x1 * day) + \
           (x2 * math.cos((2 * math.pi * int(day)) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * int(day)) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * int(day)) / 365.25)) + \
           (x4 * math.cos((2 * math.pi * int(day)) / (365.25 * 10.7))) + \
           (x5 * math.sin((2 * math.pi * int(day)) / (365.25 * 10.7)))

    # Contraints
    prob +=





def parse_data(file_name):
    data = []
    with open(file_name, 'r') as f:
        # Remove top line
        f.readline()
        for line in f:
            data.append(tuple(line.strip('\n').strip('\r').split(';')))

    return data

if __name__ == "__main__":
    data = parse_data('Corvallis_data.csv')

