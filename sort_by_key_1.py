import random
import statistics

#  Filtering Capital Cities                        5       3   4       5         6        6         5         8
capitals: list[str] = [ "Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
# for w in capitals:
#     print(f" len {w} = {len(w)}")

print(capitals)
print()
print(sorted(capitals, key=lambda c:  len(c)))# filtering by len capital
print(sorted(capitals, key=lambda c:  len(c.split())))# filtering by numer word in capital
print(sorted(capitals, key=lambda c:  c[-1]))# filtering by last carter
print(sorted(capitals, key=lambda c:  c[::-1]))# filtering by city oppsite direction
print(sorted(capitals, key=lambda c:  c.count("a")))# filtering by letter a appears

#distance_between_countries solution f
d_b_c = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
]

print(d_b_c)
print()
print(sorted(d_b_c, key=lambda d: d[1]))# filtering by distance
print(sorted(d_b_c, key=lambda d: d[1], reverse=True))# filtering by reverse distance
print(sorted(d_b_c, key=lambda d: d[2]))# filtering by continent name
print(sorted(d_b_c, key=lambda d: (d[2], (d[1]))))# filtering by continent name

#generate 50 random numbers
list50 = [random.randint(1, 100) for _ in range(50)]
print()
print(list50," ",statistics.mean(list50))
print(sorted(list50, key=lambda i: i))# filtering by number
print(sorted(list50, key=lambda i: statistics.mean(list50)))# filtering by distance evrage

#-----------------------------------------------------------------------------
print()
print(" solution 2 dict")
print("Assuming the period at the end of a sentence is not included in one of the questions, I will ignore the period and space.")
source_block = "This chocolate cake is rich, moist, and full of delicious chocolate flavor. To make the cake, you will need chocolate, flour, sugar, eggs, and butter. After baking the chocolate cake, let the cake cool before adding the chocolate frosting."
words: list[str] = source_block.replace(",", "").replace(".", "").split()
print(words)
dict_count_words: dict[str, int] = dict()
for w in words:
    dict_count_words[w] = dict_count_words.get(w, 0) + 1
print(dict_count_words)
value = max(dict_count_words.values())
key = next((k for k, v in dict_count_words.items() if v == value), None)
print(f" {key} appears {value} times")

letters: str = source_block.replace(",", "").replace(".", "").replace(" ", "")
print("Assuming you mean only letter not char and not different between uppercase to lowercase.")
print(letters)
dict_count_letters: dict[str, int] = dict()
for l in letters:
    dict_count_letters[l.lower()] = dict_count_letters.get(l.lower(), 0) + 1
print(dict_count_letters)
dict_min_letters: dict[str, int] = dict()
value = min(dict_count_letters.values())
dict_min_letters = {k: v for k, v in dict_count_letters.items() if v == value}
print(dict_min_letters)

#-----------------------------------------------------------------------------
print()
print(" solution 3 dict")
dict_power3: dict[int, int] = {base: base ** 3 for base in range(1, 21)}
print(dict_power3)

base: int = int(input("enter base number to check if it exist in the dict :"))
print({k: v for k, v in dict_power3.items() if k == base} or "Not exist")









