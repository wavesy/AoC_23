import part_1
import sys


def find_colours_max(results: list) -> tuple:
    """
    Takes list of dicts {'red': x, 'green': y, 'blue': z} as param.
    Returns a tuple with minimum counts needed for each colour in order red, green, blue.
    """
    max_red = max_green = max_blue = 0
    for result in results:
        if result['red'] > max_red:
            max_red = result['red']

        if result['green'] > max_green:
            max_green = result['green']

        if result['blue'] > max_blue:
            max_blue = result['blue']

    return (max_red, max_green, max_blue)


def main() -> None:
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as input_file:
        prod_sum = 0
        for line in input_file:
            results = part_1.parse_draws(line)
            max_colours = find_colours_max(results)
            max_red, max_green, max_blue = max_colours
            prod = max_red * max_green * max_blue
            print(prod)
            prod_sum += prod

        print(f"Sum of prods: {prod_sum}")


if __name__ == "__main__":
    main()
