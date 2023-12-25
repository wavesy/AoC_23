import part_1
import sys

def main():
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            results = part_1.parse_draws(line)

    return 0


if __name__ == "__main__":
    main()
