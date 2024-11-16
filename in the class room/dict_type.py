
grades = [['moshe', 89], ['danny', 94], ['zeev', 55], ['maya', 75]]

# hash-map
# key, value
# maya, danny

for i in grades:
    if i[0] == 'maya':
        print(i[1])

# create
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
print(grades_d['maya'])
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
