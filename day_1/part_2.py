import sys
import string




def get_calib_num(line: str) -> int:
    """
    Parses a string and finds the first and last numerical, 
    then compounds them into a new two-digit number.
    """

    def _parse_for_literal(line: str, direction: str) -> int or None:
        """
        Check if start of line is a digit literal.
        If yes, return corresponding integer.
        """

        literals_to_nums = {"one":    '1',
                            "two":    '2',
                            "three":  '3',
                            "four":   '4',
                            "five":   '5',
                            "six":    '6',
                            "seven":  '7',
                            "eight":  '8',
                            "nine":   '9'}

        for literal in literals_to_nums:
            if direction == "start" and line.startswith(literal):
                return literals_to_nums[literal]

            elif direction == "end" and line.endswith(literal):
                return literals_to_nums[literal]
        
        return None
    
    
    # Remove whitespace.
    line = line.rstrip().lstrip()
    
    first_num = None
    last_num = None

    while line:
        begin = line[0]
        end = line[-1]
        
        if not first_num:
            if begin.isdigit():
                first_num = begin
            else:
                first_num = _parse_for_literal(line, "start")
                if not first_num:
                    line = line[1:]

        if not last_num:
            if end.isdigit():
                last_num = end
            elif line:
                last_num = _parse_for_literal(line, "end")
                if not last_num:
                    line = line[:-1]

        if first_num and last_num:
            return int(first_num + last_num)

    return 0


def main():
    file_path = sys.argv[1]
    calib_nums = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            calib_nums.append(get_calib_num(line))
    
    calib_val = 0
    for num in calib_nums:
        calib_val += num

    print(calib_val)

    return 0

if __name__ == "__main__":
    main()