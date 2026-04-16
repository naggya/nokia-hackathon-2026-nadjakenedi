from pathlib import Path

def next_magic_num(value):
    length = len(value)
    cut = (length+1)//2
    first_half = value[:cut]

    if length % 2 == 0:
        guess = first_half + first_half[::-1]
    else:
        guess = first_half + first_half[:-1][::-1
        ]
    if int(guess)>int(value):
        return guess        

    converted_first_half = int(first_half)
    new_first_half = str(converted_first_half+1)

    if len(new_first_half)>len(first_half):
        return "1"+"0"*(length-1)+"1"
    if length %2 ==0:
        return new_first_half + new_first_half[::-1]
    else:
        return new_first_half + new_first_half[:-1][::-1]



def main():
    input_file = Path("magic_numbers/input.txt")
    lines = input_file.read_text(encoding="utf-8").splitlines()
    for line in lines:
        num_str = line.strip()
        if num_str and num_str.isdigit():
            print(next_magic_num(num_str))


if __name__ == "__main__":
    main()
