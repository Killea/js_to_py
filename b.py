from array import array


print(1)

d1 = {}
print(d1)



list1 = [[1,2], [3,4]]
def flatten(l):
    return [item for sublist in l for item in sublist]
print(flatten(list1))



list2 = [1, 2, 3]
map1 = list(map(lambda x: x*2, list2))
print(map1)

filter1 = list(filter(lambda x: x>1, list2))
print(filter1)