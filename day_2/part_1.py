import re
import sys

N_RED = 12
N_GREEN = 13
N_BLUE = 14

def parse_game(line: str) -> dict:
    """
    Parse a line that contains game results, return point sums
    """
    pattern = re.compile(r'\d+\s+(red|green|blue)')
    game_result = {'red': 0, 'green': 0, 'blue': 0}
    matches = pattern.finditer(line)

    for match in matches:
        # Get the actual match string from match object
        match = match.group()
        match = match.split(' ')
        color = match[1]
        score = 0

        try:
            score =  int(match[0])
        except ValueError:
            # In case of score N/A jump to next
            continue

        if color in game_result:
            game_result[color] += score

    return game_result


def check_validity(game_result: dict) -> bool:
    return game_result['red'] <= N_RED and\
           game_result['green'] <= N_GREEN and\
           game_result['blue'] <= N_BLUE


def main():
    input_file_path = sys.argv[1]
    line_cnt = 1
    valid_sum = 0

    with open(input_file_path, 'r') as file:
        for line in file:
            game_result = parse_game(line)
            if check_validity(game_result):
                print(f"Valid game ID: {line_cnt}")
                valid_sum += line_cnt
            line_cnt += 1

    print(valid_sum)

    return 0


if __name__ == "__main__":
    main()