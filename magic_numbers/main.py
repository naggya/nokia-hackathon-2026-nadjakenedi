from pathlib import Path

def make_palindrom(half,even_lengt):
    if even_lengt:
        return half + half[::-1]
    else:
        return half+half[:-1][::-1]    
def next_magic_num(value):
    length = len(value)
    cut = (length+1)//2
    first_half = value[:cut]

    iseven=(length%2==0)
    first_attempt=make_palindrom(first_half,iseven)

    if int(first_attempt)>int(value):
        return first_attempt        

    converted_first_half = int(first_half)+1
    new_first_half = str(converted_first_half+1)

    if len(new_first_half)>len(first_half):
        return "1"+"0"*(length-1)+"1"
    return make_palindrom(new_first_half,iseven)


from pathlib import Path


def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    print(data, end="")


if __name__ == "__main__":
    main()
