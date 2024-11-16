words: list[str] = ["zzzzz", "b", "abc", "cba", "bac", "cccc", "bb", "t"]
print(sorted(words))
print(sorted(words, key=lambda w: w )) # abc
print(sorted(words, key=lambda w: len(w))) # len
print(sorted(words, key=lambda w: len(w), reverse=True)) # len reverse
print(sorted(words, key=lambda w: (len(w), w))) # len abc, not clear

# ["a b c", "z b", "x y", "z" ] sort by num of words
# [89, 91, 23, 34, 15, 98, 71, 99, 101]
# sort by ahadot , second sort by the number itself

print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 10, x)))
print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 2, x)))

sum_a_b = lambda a,b:a+b
print(sum_a_b(7,3))

print(f" 1491789 // 1000 = {1491789 // 1000}")
print(f" 1491789 % 1000 = {1491789 % 1000}")
print(f" 1491789 / 1000 = {1491789 / 1000}")

# הדפסה של אורך מילה
       # [    5  ,   3  ,           15     ,  1 ] sort by len words
for w in ["a b c", "z b", "x yyyyyyyyyyyyy", "z" ]:
    print(f" len {w} = {len(w)}")
print(sorted(["a b c", "z b", "x yyyyyyyyyyyyy", "z" ], key=lambda w: len(w)))  # sort by len words

print(sorted(["a b c", "z b", "x yyyyyyyyyyyyy", "z" ], key=lambda w: len(w.split())))  # number of words
# sort by ahadot , in tie first the smaller
#              9   1   3   4   5   8   1   9    1
print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 10, x)))

# sort even first then odd
# 0 1
#              1   1   1   0   1   0   1   1    1
print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 2,x)))  # zugi=0 e-zigu=1

print("abba" == "abba"[::-1])# print True
# palindrom = string which is equal to its reverse
print()
# False = 0, True = 1
# sorted order First 0 then 1
print(["acaaca", "abba", "cd", "d", "drrrd", "12z2", "12321" ])
print(sorted(["acaaca", "abba", "cd", "d", "drrrd", "12z2", "12321" ], key=lambda w: w == w[::-1], reverse=True))  # len of word
#                True  False True True     False    True
#                   1  0     1    1        0        1
#                   0  0     1    1        1        1

words = ["acaaca", "abba", "cd", "d", "drrrd", "12z2", "12321" ]
result = sorted(words, key=lambda w: w == w[::-1])
result_with_flags = [(word, word == word[::-1]) for word in result]
#cd:False ,12z2:False ,abba:True ,d:True ,drrrd:True ,12321:True
for word, is_palindrome in result_with_flags:
    print(f"{word}:{is_palindrome}", end=" "+",")

print()
print()
#                   89             94            55
#          ['zeev', 55]  ['moshe', 89]  ['danny', 94]
grades = [['moshe', 89], ['danny', 94], ['zeev', 55]]
print(sorted(grades, key=lambda name_grade: name_grade[1]))
print(sorted(grades, key=lambda name_grade: name_grade[0]))

grades_d: dict[str, int] =  {'moshe': 89, 'danny': 94, 'zeev': 55, 'maya': 75}

personal: dict[str, any] = {'f_name': "danny", 'l_name': "cohen",
                               "age": 25, "smoker": True, 'siblings': [20, 24, 30],
                               'address': {
                                   'city': 'tel aviv',
                                   'street': 'ben yehuda',
                                   'number': 90,
                                   'zipcode': 90210
                               }}
# 1 fill the data
# 2 get the age value using  [ ], and using get function
# 3 change the smoker to False
# 4 del key-value l_name
# 5 get first age of siblings
# 6 get zip code
# 7 update the address.number with same value + 1
# 8 del address.zipcode
# print the new dict
# print(personal['address']['zipcode'])

# get by key
print(f" maya grade = {grades_d['maya']}")
#print(grades_d['mayaa'])  # error when not found
print(grades_d.get('mayaa'))  # None
print(grades_d.get('mayaa', -1))  # -1

# update/ insert
# dict  [key] = value
grades_d['sharon'] = 100  # add if not exist, overwrite if exists
print(grades_d)
grades_d['sharon'] = 99  # add if not exist, overwrite if exists
print(grades_d)
grades_d.update({'sharon': 50, 'ranny': 30})
print(grades_d)

grades_d.setdefault('sharon2', 99)  # insert only if not exist
print(grades_d)

# delete
del grades_d['ranny']
print(grades_d)

dict_nums: dict[int, int] = dict()  # prefer this over {}
dict_nums[1] = 20
print(dict_nums)

print()
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
print(dict_count)

emoji_dict = {
    'love': '❤️',
    'pizza': '🍕',
    'cats': '🐱',
    'dog': '🐶',
    'happy': '😊',
    'sad': '😢'
}
sentence = "I love pizza and cats"
# print(sentence.split()) # ['I', 'love', 'pizza', 'and', 'cats']
for word in sentence.split():
    # 1
    if word in emoji_dict:
        print(emoji_dict[word], end = " ")
    else:
        print(word, end = " ")
 # 2
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
print(list(numbers_to_days.values()))
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

d = {'a': 1, 'b': 2}

# יצירת איטרטור על מפתחות המילון
keys_iter = iter(d.keys())

# שינוי המילון בזמן האיטרציה עלול להוביל ל-RuntimeError
d['c'] = 3
try:
    print(next(keys_iter))
except RuntimeError as e:# Error: dictionary changed size during iteration
    print(f"Error: {e}")

#print abc letters
print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1)))

