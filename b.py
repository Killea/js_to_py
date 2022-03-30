from array import array


print(1)

d1 = {}
print(d1)



list1 = [[1,2], [3,4]]
def flatten(l):
    return [item for sublist in l for item in sublist]
print(flatten(list1))



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
print ( {"d":4} | dict2)