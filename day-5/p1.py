from sys import argv


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        data = f.read().split("\n\n")
    print(data)
