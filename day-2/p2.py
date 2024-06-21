import regex
from sys import argv
from copy import deepcopy
from math import prod


cubes_regex = r"(\d+) (blue|red|green)"
game_regex = r"Game (\d+):"

colors = ["red", "green", "blue"]
cubes_dict = { "red": 0, "green": 0, "blue": 0 }
total_cubes_dict = { "red": 12, "green": 13, "blue": 14 }


def get_game_data(s):
    m = regex.match(game_regex, s)
    if m:
        game_num = int(m.group(1))
        game_data = s.replace(m.group(0), "").strip()
        return game_num, game_data
    return None, None


def count_cubes(grab_text):
    cubes_dict_local = deepcopy(cubes_dict)
    m = regex.findall(cubes_regex, grab_text)
    for data in m:
        num_str, color = data
        num = int(num_str)
        cubes_dict_local[color] += num
    return cubes_dict_local


def get_grab_validity(grab_dict):
    return all(
        grab_dict[color] <= total_cubes_dict[color]
        for color in colors
    )


def get_game_validity(game_data):
    grab_texts = [x.strip() for x in game_data.split(";")]
    for grab_text in grab_texts:
        grab_dict = count_cubes(grab_text)
        if not get_grab_validity(grab_dict):
            return False
    return True


def get_min_num_cubes(game_data):
    min_num_cubes_dict = deepcopy(cubes_dict)
    grab_texts = [x.strip() for x in game_data.split(";")]
    for grab_text in grab_texts:
        grab_dict = count_cubes(grab_text)
        for color in colors:
            min_num_cubes_dict[color] = max(
                grab_dict[color], min_num_cubes_dict[color]
            )
    return min_num_cubes_dict


def power(min_num_cubes_dict):
    return prod(val for val in min_num_cubes_dict.values())


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        games_text = [line.strip() for line in f.readlines()]

    game_powers_list = []
    for game_text in games_text:
        game_num, game_data = get_game_data(game_text)
        min_num_cubes_dict = get_min_num_cubes(game_data)
        game_power = power(min_num_cubes_dict)
        print(f"Game #{game_num}: {game_data}; {min_num_cubes_dict}; power={(game_power)}")
        game_powers_list.append(game_power)

    print("----------------------")
    print(f"Sum of the powers of all games: {sum(game_powers_list)}")
