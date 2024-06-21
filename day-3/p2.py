from sys import argv
from itertools import product
import re


numbers_re = re.compile(r"(\d+)")
star_re = re.compile(r"\*")


class Star:
    def __init__(self, row, col, neighbor_idices, num_matrix):
        self.row = row
        self.col = col
        self.neighbor_idices = neighbor_idices
        self.num_matrix = num_matrix
        self.adjacent_numbers = set()
        self.find_adjacent_numers()
        self.is_gear = ( len(self.adjacent_numbers) == 2 )
        if self.is_gear:
            x, y = self.adjacent_numbers
            self.ratio = x.value * y.value

    def find_adjacent_numers(self):
        for i, j in self.neighbor_idices:
            if self.num_matrix[i][j] is not None:
                self.adjacent_numbers.add(self.num_matrix[i][j])

    def __str__(self):
        return (f"row: {self.row}, col: {self.col}, "
                f"neighbor indices: {self.neighbor_idices}")


class Number:
    def __init__(self, value, row, span, data_matrix):
        self.value = value
        self.row = row
        self.span = span
        for col in range(*span):
            data_matrix[row][col] = self

    def __str__(self):
        return f"value: {self.value}, row: {self.row}, span: {self.span}"


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


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        data = [line.strip() for line in f.readlines()]
    N = len(data)
    M = len(data[0])
    data_matrix = [
        [ None for _ in range(N) ]
        for _ in range(M)
    ]

    numbers = []
    for i, row in enumerate(data):
        matches = re.finditer(numbers_re, row)
        numbers += [
            Number(int(match.group(1)), i, match.span(), data_matrix)
            for match in matches
        ]
    
    stars = []
    for i, row in enumerate(data):
        star_matches = re.finditer(star_re, row)
        stars += [
            Star(
                i, int(match.span()[0]),
                get_neighbor_indices(i, int(match.span()[0])),
                data_matrix
            )
            for match in star_matches
        ]

    valid_gears = [ star for star in stars if star.is_gear ]
    sum_gear_ratios = sum([ gear.ratio for gear in valid_gears ])
    print("--------------------------")
    print(f"Sum of gear ratios: {sum_gear_ratios}")
