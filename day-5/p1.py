from sys import argv
import re


num_regex = r"(\d+)"


def apply_map(input, map):
    for dest_start, src_start, rng_len in map:
        if input in range(src_start, src_start+rng_len):
            return dest_start + input - src_start
    return input


def apply_all_maps(seed):
    output = seed
    for map in maps.values():
        output = apply_map(output, map)
    return output


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

    outputs = [ apply_all_maps(seed) for seed in seeds ]
    print("----------")
    print(min(outputs))
