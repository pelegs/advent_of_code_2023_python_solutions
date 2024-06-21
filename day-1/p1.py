from sys import argv
import re


first_digit_regex = re.compile(r"^[a-z]*(?P<fdig>\d)")


def get_first_digit(s: str) -> int:
    m = re.match(first_digit_regex, s).group(1)
    return int(m)


if __name__ == "__main__":
    filename = argv[1]
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        first_digit = get_first_digit(line)
        last_digit = get_first_digit(line[::-1])
        sum += first_digit*10 + last_digit

    print(sum)
