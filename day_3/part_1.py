import sys
import typing as T


def create_2d_from_file(filename: str) -> tuple(tuple):
    # Collect stripped lines in a list first
    tuples_list = []
    with open(filename, 'r') as file:
        # Reference for line length, to check if each line is same length
        line_length = len(file[0].rstrip())
        for line in file:
            # Check that line length is uniform
            if len(line) != line_length:
                raise IndexError("Input file lines should be same length.")
            line = line.rstrip()
            tuples_list.append(tuple(line))

    tuples_2d = tuple(tuples_list)
    return tuples_2d



def main() -> None:
    input_file_name = sys.argv[1]
    char_map = create_2d_from_file(input_file_name)


if __name__ == "__main__":
    main()