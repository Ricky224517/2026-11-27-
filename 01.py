# 1 D1587739_蔡融頫_cups.py 

def build_cups(teams, givers, counts):
    cups = {}
    for team in teams:
        cups[team] = 0
    for i in range(len(givers)):
        giver = givers[i]
        if giver in cups:
            cups[giver] += counts[i]
    return cups

# 2 D1546938_魏劭宇_pyramid.py

def cups_needed(h):
    if h <= 0:
        return 0
    return h + cups_needed(h - 1)

# 3 D1546822_連奕然_height.py

def max_height(cups, h):
    if cups_needed(h) > cups:
        return h - 1
    return max_height(cups, h + 1)

# 4 D1546985_林璿祺_report.py


def make_report(cups):
    lines = []
    for team, total in cups.items():
        h = max_height(total, 1)
        if h == 0:
            lines.append(f"{team}：杯子不夠疊一層")
        else:
            lines.append(f"{team}：疊{h}層，剩{total - cups_needed(h)}個")
    return lines

# 5 D1515375_鍾允碩_main.py 

def main():
    teams = input().split()
    n = int(input())
    givers = []
    counts = []
    for _ in range(n):
        data = input().split()
        givers.append(data[0])
        counts.append(int(data[1]))

    cups = build_cups(teams, givers, counts)
    report_lines = make_report(cups)
    for j in report_lines:
        print(j)

if __name__ == "__main__":
    main()