import statistics
import random

# ========================= FILTER

def add_x_100(x: int) -> int:
    return x + 100

add_x_100 = lambda x: x + 100

numbers: list[int] = [random.randint(1, 100) for _ in range(50)]

bigger_50: list[int] = []
for num in numbers:
    if num > 50:
        bigger_50.append(num)
def is_bigger_50(x: int) -> int:
    # 1
    if x > 50:
        return True
    else:
        return False
    # 2
    return x > 50

#compr = [num for num in numbers if num > 50]
print(list(filter(is_bigger_50, numbers)))
print(list(filter(lambda x: x > 50, numbers)))
print(list(filter(lambda x: x % 7 == 0, numbers)))
print(list(filter(lambda x: 10 <= x <= 99, numbers)))
print(list(filter(lambda x: 10 <= x <= 99 and \
                  x % 10 == x // 10, numbers)))
print(list(filter(lambda x: x % 10 + x // 10 == 9, numbers)))
avg_num = statistics.mean(numbers)
print(list(filter(lambda x: x > avg_num, numbers)))
half_max = max(numbers) / 2
print(list(filter(lambda x: x > half_max, numbers)))

print(list(filter(lambda x: random.choice([True, False]), \
                  numbers)))

games = ["Fortnite", "Grand Theft Auto V", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(f"bigger 8 {list(filter(lambda w: len(w) > 8, games))}")
print(list(filter(lambda w: w.upper().startswith("F"), games)))
print(list(filter(lambda w: len(w.split()) == 2, games)))
v_games = list(filter(lambda w: 'V' in w.upper(), games))
print(v_games)

# ========================= MAP
nums: list[int] = [random.randint(-50, 50) for _ in range(50)]
print(nums)
print(list(map(lambda x: x ** 3, nums)))
print(list(map(lambda x: abs(x) % 10, nums)))
print(list(map(lambda x: x * (9/5) + 32, nums)))
print(list(map(lambda x: 'positive/zero' if x >= 0 else 'negative',
               nums)))
# x = 1
# str1: str = ''
# if x >= 0:
#     str1 = 'positive/zero'
# else:
#     str1 = 'negative'
# str1 = 'positive' if x >= 0 else 'negative'
#print(f"{'YES' if x > 0 else 'NO'}")
#x = 1 if y > 0 else 2
#if y > 0:
#    x = 1
#else:
#    x = 2

fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print(fruits)
print(list(map(lambda f: f[::-1], fruits)))
print(list(map(lambda f: f[0], fruits)))
print(list(map(lambda f: f.upper(), fruits)))
print(list(map(lambda f: f[len(f) // 2], fruits)))
print(list(map(lambda f: f + '!' if f[-1] == 's' else f, fruits)))

def print_x() -> None:
    # global x
    # x += 1
    print(x)

x: int = 10  # global x
print_x()
print(x)  # 11





