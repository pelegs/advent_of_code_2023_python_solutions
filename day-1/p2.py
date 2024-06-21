from sys import argv
import regex


digit_regex = regex.compile(
    r"(?P<fdig>one|two|three|four|five|six|seven|eight|nine|\d)"
)
digits_dict = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
    "6": "6", "7": "7", "8": "8", "9": "9", 
}


def get_digits(s: str) -> list[str]:
    return regex.findall(digit_regex, s, overlapped=True)


if __name__ == "__main__":
    filename = argv[1]
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        digits = get_digits(line)
        first_digit = int(digits_dict[digits[0]])
        last_digit = int(digits_dict[digits[-1]])
        line_val = 10*first_digit + last_digit
        sum += line_val
        print(f"{line}: {first_digit}, {last_digit}; val={line_val}")

    print("---------------------------")
    print(f"sum = {sum}")
