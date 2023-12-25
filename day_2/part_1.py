import re
import sys

N_RED = 12
N_GREEN = 13
N_BLUE = 14


def accumulate_scores(scores_and_colors: list) -> dict:
    """
    For each pair in list, add score to corresponding color
    in result dict. Return the accumulated dict.
    """
    result = {'red': 0, 'green': 0, 'blue': 0}

    for pair in scores_and_colors:
        pair = pair.split(' ')
        color = pair[1]
        score = 0

        try:
            score = int(pair[0])
        except ValueError as e:
            print(e)
            continue

        if color in result:
            result[color] += score

    return result


def parse_game(line: str) -> dict:
    """
    NOTE: Doesn't comply with part 1 specs, don't use
    Parse a line that contains game results, return point sums
    """
    pattern = re.compile(r'\d+\s+(red|green|blue)')
    matches = pattern.finditer(line)

    scores_and_colors = [match.group() for match in matches]

    return accumulate_scores(scores_and_colors)


def parse_draws(line: str) -> list:
    pattern = re.compile(r'\d+\s+(red|green|blue)')

    draws = line.split(':')[1]
    draws = draws.split(';')
    results = []

    for draw in draws:
        matches = pattern.finditer(draw)
        scores = [match.group() for match in matches]
        results.append(accumulate_scores(scores))

    return results


def check_validity(result: dict) -> bool:
    return result['red'] <= N_RED and\
           result['green'] <= N_GREEN and\
           result['blue'] <= N_BLUE


def main():
    input_file_path = sys.argv[1]
    line_cnt = 1
    valid_sum = 0

    with open(input_file_path, 'r') as file:
        for line in file:
            results = parse_draws(line)

            is_valid = True
            for result in results:
                if not check_validity(result):
                    is_valid = False
                    break

            if is_valid:
                print(f"Valid game ID: {line_cnt}")
                valid_sum += line_cnt

            line_cnt += 1

    print(valid_sum)

    return 0


if __name__ == "__main__":
    main()