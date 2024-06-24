from sys import argv
import re


num_regex = r"(\d+)"


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        data = [
            x.split("\n")
            for x in f.read().split("\n\n")
        ]
    # print(data)
    seeds = [ int(x) for x in re.findall(num_regex, data[0][0]) ]
    maps = {
        data[i][0].replace(" map:", ""): [
            [ int(y) for y in x.split() ]
            for x in data[i][1:]
        ]
        for i in range(1, 8)
    }
    # print(maps)
