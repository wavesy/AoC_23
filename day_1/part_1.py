import sys
import string

def get_calib_num(line: str) -> int:
    """
    Parses a string and finds the first and last numerical, 
    then compounds them into a new two-digit number.
    """

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
                line = line[1:]

        if not last_num:
            if end.isdigit():
                last_num = end
            elif line:
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