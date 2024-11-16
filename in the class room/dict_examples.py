numbers: list[int] = [1, 1, 4, 7, 80, 200, 80, 4, 200, 12, 4000, 1]

dict_count: dict[int, int] = dict()
for num in numbers:
    dict_count[num] = dict_count.get(num, 0) + 1
    # if num in dict_count:
    #     dict_count[num] += 1
    # else:
    #     dict_count[num] = 1
print(dict_count)
print('4000 count', dict_count[4000])
print('80 count', dict_count[80])

emoji_dict = {
    'love': '❤️',
    'pizza': '🍕',
    'cats': '🐱',
    'dog': '🐶',
    'happy': '😊',
    'sad': '😢'
}

sentence = "I love pizza and cats"
#print(sentence.split())  # ['I', 'love', 'pizza', 'and', 'cats']
for word in sentence.split():
    # 1
    if word in emoji_dict:
        print(emoji_dict[word], end = " ")
    else:
        print(word, end = " ")
    # 2
    print(emoji_dict.get(word, word), end = " ")

print()

# 'a' -> '@'
# 'e' -> '3'
# 'i' -> '!'
# 'o' -> '0'
# 's' -> '$'
# password -> p@$$w0rd

#                           key: value
dict_enc: dict[str: str] = {'a': '@',
                            'e': '3',
                            'i': '!',
                            'o': '0',
                            's': '$'}
pwd: str = "password"
for c in pwd:
    # if c in dict_enc:
    #     print(dict_enc[c], end="")
    # else:
    #     print(c, end="")
    print(dict_enc.get(c, c), end="")
print()

# day: int = int(input('enter day (1-7)'))
# match day:
#     case 1: print("Sunday")

numbers_to_days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
print(numbers_to_days.get(8, "invalid day"))
print(numbers_to_days.keys())
print(numbers_to_days.get(list(numbers_to_days.keys())[0]))
#print(numbers_to_days[numbers_to_days.keys()[0]])

months_days = {
    "january": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "november": 30,
    "December": 31
}
print(months_days.get("November".lower(), "invalid month"))