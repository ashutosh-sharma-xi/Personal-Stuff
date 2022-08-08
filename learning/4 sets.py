"""
SETS -  sets can store values like tuples or lists but sets does not retain similar value
"""
#creating sets
set1 = set()
set2 = set([1,2,3])    # creating a set from a list
a= min(set2)
# adding values into set
set2.add(4)
# creating list and casting it in set
list = [5,6,7]
set3 = set(list)

# removing a set element from a set 
set3.remove(7)  # remove will remove the element from set if it exist else will give error

print(a,"\n",set2)
print(type(set2))

# this also have the properties of the sets like unions and the intersections

set2.union(set3)
print(set2.union(set3))
print(set2.intersection(set3))
print(set2.isdisjoint(set3))
print(set2.difference(set3))
print(set2.(set3))

# functions like min() max() len() etc can also be applied to sets
print(min(set2))
print(max(set2))
print(len(set2))


# other functions of sets 
remove()
discard()
































