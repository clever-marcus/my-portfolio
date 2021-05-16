#Set => is a colletcion which is unordered, unindexed and has no duplicate values.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "glass", "chillies", "knife"}

"""we can add an item to a set
utensils.add("napkin")
utensils.remove("fork")
utensils.clear()"""


"""we can add one set to another by using the update() method"""
#utensils.update(dishes)
"""we can also compare the difference of two sets"""
#print(dishes.difference(utensils))

"""these will connect the two sets using the common item between them"""
print(utensils.intersection(dishes))

"""we can also join two or more sets together"""
#dinner_table = utensils.union(dishes)
#for x in dinner_table:
 #   print(x)