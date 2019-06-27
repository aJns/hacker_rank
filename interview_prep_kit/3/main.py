import os

import common


def jumpingOnClouds(c):
    jumps = 0

    i = 0
    arr_count = len(c)

    while i + 1 < arr_count:
        cand = i + 2
        if cand >= arr_count or c[cand] != 0:
            cand = i + 1
        i = cand
        jumps = jumps + 1

    return jumps


if __name__ == '__main__':
    input_path = os.path.abspath("testdata/input.txt")
    output_path = os.path.abspath("testdata/output.txt")
    common.test_solution(jumpingOnClouds, input_path, output_path)
