# 1. D1587739_蔡融頫_digits.py 

def digit_sum(n):
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)

# 2. D1546938_魏劭宇_lifenum.py 

def life_number(n):
    if n < 10:
        return n
    return life_number(digit_sum(n))

# 3. D1546822_連奕然_people.py

def build_numbers(names, birthdays):
    result = {}
    for i in range(len(names)):
        result[names[i]] = life_number(birthdays[i])
    return result

# 4. D1546985_林璿祺_tally.py 

def count_numbers(numbers):
    counts = {}
    for target in range(1, 10):
        total = 0
        for num in numbers:
            if num == target:
                total += 1
        if total > 0:
            counts[target] = total
    return counts

# 5. D1515375_鍾允碩_main.py 

def main():
    n = int(input())
    names = []
    birthdays = []
    
    for _ in range(n):
        line = input().split()
        names.append(line[0])
        birthdays.append(int(line[1]))
        
    person_nums = build_numbers(names, birthdays)
    num_counts = count_numbers(list(person_nums.values()))
    
    for name in names:
        print(f"{name}：生命靈數 {person_nums[name]}")
        
    for num, count in num_counts.items():
        print(f"靈數 {num}：{count} 人")

main()