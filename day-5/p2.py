from sys import argv
import re
from tqdm import tqdm
from copy import deepcopy


num_regex = r"(\d+)"


def apply_map(input, map):
    for dest_start, src_start, rng_len in map:
        if input in range(src_start, src_start+rng_len):
            return dest_start + input - src_start
    return input


def apply_all_maps(seed, maps):
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
        range(first, last) for first, last in zip(seeds_raw[::2], seeds_raw[1::2])
    ]

    maps = {
        data[i][0].replace(" map:", ""): [
            [ int(y) for y in x.split() ]
            for x in data[i][1:]
        ]
        for i in range(1, 8)
    }

    inv_maps = deepcopy(maps)
    for map in inv_maps.values():
        for rng in map:
            rng[:2] = reversed(rng[:2])
    inv_maps = {
        key: inv_maps[key]
        for key in reversed(inv_maps)
    }

    # for seed in seeds_raw:
    #     output = apply_all_maps(seed, maps)
    #     seed_back = apply_all_maps(output, inv_maps)
    #     print(f"{seed} --> {output} --> {seed_back}")

    sorted_location_ranges = sorted(maps["humidity-to-location"])
    for location_range in tqdm(sorted_location_ranges):
        dest, _, num = location_range
        for location in tqdm(range(dest, dest+num), leave=False):
            seed = apply_all_maps(location, inv_maps)
            if seed in seed_ranges:
                print(f"Seed: {seed} --> location: {location}")
                exit(0)
