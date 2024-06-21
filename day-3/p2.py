from sys import argv
from itertools import product
import re


numbers_re = re.compile(r"(\d+)")
excluded_chars = "0123456789."


def get_unique_indices(lst):
    """
    Generate unique combination of all the neighbor indices of each of the
    digits of a matched number: this is done using a union.
    Taken from:
    https://stackoverflow.com/questions/2151517/pythonic-way-to-create-union-of-all-values-contained-in-multiple-lists
    """
    return set().union(*lst)


def get_neighbor_indices(i, j):
    def adjacent_indices(k, max_k):
        return range(max(0, k-1), min(k+1, max_k-1)+1)

    row_neighbors = adjacent_indices(i, M)
    col_neighbors = adjacent_indices(j, N)
    return [
        coords
        for coords in product(row_neighbors, col_neighbors)
        if coords != (i, j)
    ]


def get_values(indices_list, data):
    return [
        data[i][j]
        for i, j in indices_list
        if data[i][j] not in excluded_chars
    ]


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        data = [line.strip() for line in f.readlines()]
    N = len(data)
    M = len(data[0])

    part_nums = []
    for i, row in enumerate(data):
        numbers = re.finditer(numbers_re, row)
        for match in numbers:
            match_indices = [x for x in range(*match.span())]
            indices_list = get_unique_indices(
                [get_neighbor_indices(i, j) for j in match_indices]
            )
            if len(get_values(indices_list, data)) != 0:
                part_nums.append(int(match.group(1)))
    print("-------------------------------")
    print(f"Sum of part nums: {sum(part_nums)}")
