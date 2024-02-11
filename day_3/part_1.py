import sys
import typing as T

class Occurence:
    def __init__(self, start: tuple[int, int], end: tuple[int, int], number: int):
        # start(x, y), end(x, y)
        self.start = start
        self.end = end
        self.number = number

    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def get_number(self):
        return self.number


def create_2d_from_file(filename: str) -> tuple:
    # Collect stripped lines in a list first
    tuples_list = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.rstrip()
            tuples_list.append(tuple(line))

    tuples_2d = tuple(tuples_list)
    return tuples_2d


def get_num_occurences(map_2d: tuple[tuple]) -> list[Occurence]:
    for y in map_2d:
        for x in y:
            
    pass



def main() -> None:
    input_file_name = sys.argv[1]
    char_map = create_2d_from_file(input_file_name)


if __name__ == "__main__":
    main()