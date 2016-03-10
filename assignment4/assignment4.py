#!/usr/bin/env python

from pulp import *
import math

def solve(avg, day):
    print "avg = {}, day = {}".format(avg, day)
    prob = LpProblem("best fit curve for temps in corvallis", LpMinimize)

    # LP variables
    x0 = LpVariable("x0", 0)
    x1 = LpVariable("x1", 0)
    x2 = LpVariable("x2", 0)
    x3 = LpVariable("x3", 0)
    x4 = LpVariable("x4", 0)
    x5 = LpVariable("x5", 0)

    # Objective
    prob += x0 + \
           (x1 * day) + \
           (x2 * math.cos((2 * math.pi * day) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) + \
           (x4 * math.cos((2 * math.pi * day) / (365.25 * 10.7))) + \
           (x5 * math.sin((2 * math.pi * day) / (365.25 * 10.7)))

    # Contraints
    prob += x0 - \
           (x1 * day) - \
           (x2 * math.cos((2 * math.pi * day) / 365.25)) - \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) - \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) - \
           (x4 * math.cos((2 * math.pi * day) / (365.25 * 10.7))) - \
           (x5 * math.sin((2 * math.pi * day) / (365.25 * 10.7))) <= avg

    # Contraints
    prob += x0 + \
           (x1 * day) + \
           (x2 * math.cos((2 * math.pi * day) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) + \
           (x3 * math.sin((2 * math.pi * day) / 365.25)) + \
           (x4 * math.cos((2 * math.pi * day) / (365.25 * 10.7))) + \
           (x5 * math.sin((2 * math.pi * day) / (365.25 * 10.7))) >= avg

    status = prob.solve()
    print LpStatus[status]
    # print value(prob.objective)

    print value(x0)
    print value(x1)
    print value(x2)
    print value(x3)
    print value(x4)
    print value(x5)


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
    # print data[0][7:]
    solve(float(data[0][7]), int(data[0][8]))
