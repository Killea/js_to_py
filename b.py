
print(1)

d1 = {}
print(d1)



# list1 = [[1,2], [3,4]]
# def flatten(l):
#     return [item for sublist in l for item in sublist]
# print(flatten(list1))

list1 = [[1,2], [3,4]]
list3 = []
[list3.extend(item) for item in list1]
print(list3)

list2 = [1, 2, 3]
map1 = [ x*2 for x in list2]
print(map1)
# map2 = list(map(lambda x: x*2, list2))
# print(map2)

filter1 = [ x for x in list2 if x > 1]
print(filter1)
# filter2 = list(filter(lambda x: x>1, list2))
# print(filter2)




# [print(x) for x in list2] 
# enumerate(list2) to have the index/value
for x in list2:
    print(x)








dict2 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for x in dict2.keys():
    print(x)
for (k,v) in dict2.items():
    print(k,v)
for v in dict2.values():
    print(v)
dict3  = {"d":4} | dict2
print (dict3)



# deep copy
import copy
x = {}
y = copy.deepcopy(x)









# python version? does it support the simlar syntax?

cond = True

dict9 = { 
    "a": "b",
    "c":  cond if "d" else "e",
}

d1 = { "a": "a"}
cond2 = False
d4 = d1 | ({ "b": "b"} if cond2 else {})
