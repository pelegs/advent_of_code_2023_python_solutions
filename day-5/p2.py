from sys import argv
import re
from tqdm import tqdm


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


def flatten_list(lst):
    """
    Taken from
    https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
    return [
        x
        for xs in lst
        for x in xs
    ]


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        data = [
            x.split("\n")
            for x in f.read().split("\n\n")
        ]
    seeds_raw = [ int(x) for x in re.findall(num_regex, data[0][0]) ]
    seed_ranges = [
        range(start, start+end)
        for start, end in zip(seeds_raw[::2], seeds_raw[1::2])
    ]
    maps = {
        data[i][0].replace(" map:", ""): [
            [ int(y) for y in x.split() ]
            for x in data[i][1:]
        ]
        for i in range(1, 8)
    }
    
    with open("minimums.txt", "w") as f:
        for i, rng in enumerate(tqdm(seed_ranges)):
            min = -1
            for seed in tqdm(rng, leave=False):
                output = apply_all_maps(seed)
                if output < min or min == -1:
                    min = output
            f.write(f"Part {i}: {min}\n")
