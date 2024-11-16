
nums: list[int] = [1, 5, 10, -100, 20, 0]
print(sorted(nums, reverse=True))  # abc, reverse

words: list[str] = ["zzzzz", "b", "abc", "cba", "bac", "cccc", "bb", "t"]
print(sorted(words))
print(sorted(words, key=lambda w: w))  # abc
print(sorted(words, key=lambda w: len(w)))  # len
print(sorted(words, key=lambda w: len(w), reverse=True ))
print(sorted(words, key=lambda w: (len(w), w)))  # len, abc

def sum_a_b(a: int, b: int) -> int:
    """
    sum 2 numbers
    :param a: number1
    :param b: number2
    :return: sum of number1 and number2
    """
    return a + b
sum_a_b_lm = lambda a, b: a + b

# ["a b c", "z b", "x y", "z" ] sort by num of words
print(sorted(["a b c", "z b", "x yyyyyyyyyyyyy", "z" ], key=lambda w: len(w.split())))  # number of words
#              5        3      15~                1
print(sorted(["a b c", "z b", "x yyyyyyyyyyyyy", "z" ], key=lambda w: len(w)))  # len of word
# [89, 91, 23, 34, 15, 98, 71, 99, 101]
# 71, 91, 101, 23, 34, 15, 98, 89, 99
# sort by ahadot , in tie first the smaller
#              9   1   3   4   5   8   1   9    1
print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 10, x)))

# sort even first then odd
# 0 1
#              1   1   1   0   1   0   1   1    1
print(sorted([89, 91, 23, 34, 15, 98, 71, 99, 101], key=lambda x: (x % 2, x)))  # zugi=0 e-zigu=1
#             34  98  89  91 ...
#              0   0   1   1
print("abba" == "abba"[::-1])
# palindrom = string which is equal to its reverse
print(sorted(["abba", "cd", "d", "drrrd", "12z2", "12321" ], key=lambda w: w == w[::-1]))  # len of word
#                True  False True True     False    True
#                   1  0     1    1        0        1
#                   0  0     1    1        1        1

#                   89             94            55
#          ['zeev', 55]  ['moshe', 89]  ['danny', 94]
grades = [['moshe', 89], ['danny', 94], ['zeev', 55]]
print(sorted(grades, key=lambda name_grade: name_grade[1]))
print(sorted(grades, key=lambda name_grade: name_grade[0]))






