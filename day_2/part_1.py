
N_RED = 12
N_GREEN = 13
N_BLUE = 14

def parse_game(file_path: str) -> dict:
    # TODO: this function
    game_result = {}


    return game_result


def check_validity(game_result: dict) -> bool:
    return game_result['red'] <= N_RED and\
           game_result['green'] <= N_GREEN and\
           game_result['blue'] <= N_BLUE


def main():
    input_file_path = "./input.txt"

    with open(input_file_path, 'r') as file:
        for line in file:
            game_result = parse_game(line)
            if not check_validity(game_result):
                invalid_sum += game_result['id']

    print(invalid_sum)

    return 0


if __name__ == "__main__":
    main()