from pathlib import Path
import datetime
def calculate_parking_fee(start_str, end_str):
    fmt = "%Y-%m-%d %H:%M:%S"
    t1 = datetime.datetime.strptime(start_str, fmt)
    t2 = datetime.datetime.strptime(end_str, fmt)

    diff = t2 - t1
    mins = int(diff.total_seconds() / 60)

    if mins < 0: return "Error"
    if mins <= 30: return "0 forint"

    if mins >= 1440:
        return "10000 forint"
    
    hours = (mins + 59) // 60
    if hours <= 3:
        total = hours * 300
    else:
        total = 900 + (hours - 3) * 500 
    return str(total) + " forint"       


def main():
    f = open("input.txt", "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    output = []

    for i in range(2, len(lines)):
        line = lines[i].strip()
        if not line: continue
        parts = line.split()
        if len(parts) >= 5:
            plate = parts[0]
            time1 = parts[1] + " " + parts[2]
            time2 = parts[3] + " " + parts[4]

            price = calculate_parking_fee(time1, time2)
            output.append(plate + ": " + price)

    out_f = open("output.txt", "w", encoding="utf-8")
    for row in output:
        out_f.write(row + "\n")
    out_f.close()

    for r in output: print(r)


if __name__ == "__main__":
    main()
