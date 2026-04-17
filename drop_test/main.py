from pathlib import Path
def min_num_of_drops(number_of_devices, tower_height):
    max_possible_attempts= tower_height
    table=[]

    for x in range(max_possible_attempts+1):
        row=[]
        for y in range(number_of_devices+1):
            row.append(0)
        table.append(row)    

    for attempt in range(1,max_possible_attempts+1):
        for device in range(1,number_of_devices+1):
            broken_case= table[attempt-1][device-1]
            survived_cas=table[attempt-1][device] 

            current_max_height = broken_case + survived_cas +1
            table[attempt][device]= current_max_height

        if table[attempt][number_of_devices]>=tower_height:
            return attempt    





def main():
    input_file = Path("drop_test/input.txt")
    lines = input_file.read_text(encoding="utf-8").splitlines()
    for line in lines:
        parts=line.split(",")
        device = int(parts[0].strip())
        height = int(parts[1].strip())
        print(min_num_of_drops(device,height))


if __name__ == "__main__":
    main()
