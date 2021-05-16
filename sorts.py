#sort() method = used with lists
#sort() function = used with iterables

#family_guy = ["Peter Griffin", "Lois Griffin", "Brian Griffin", "Meg Griffin", "Stewie", "quagmire", "Joe", "Cliveland"]

#family_guy.sort()   #if you use reverse=True it will rearrange the list from bottom to top alphabetically
#sorted_family_guy = sorted(family_guy)

#for i in sorted_family_guy:
    #print(i)

"""family_guy = [("peter", "F", 60),
              ("Lois", "A", 33),
              ("Brian", "D", 18),
              ("Meg", "B", 17),
              ("Stewie", "C", 3),
              ("quagmire", "E", 56)]"""

#TO SORT BY THEIR FIRST COLUMN
#family_guy.sort()
#for i in family_guy:
    #print(i)

#TO SORT BY THEIR THIRD COLUMN
#age = lambda ages:ages[2]
#family_guy.sort(key=age)


#sort() function (Tuple of tuples)
family_guy = (("peter", "F", 60),
              ("Lois", "A", 33),
              ("Brian", "D", 18),
              ("Meg", "B", 17),
              ("Stewie", "C", 3),
              ("quagmire", "E", 56))
age = lambda ages:ages[2]

sorted_family = sorted(family_guy, key=age)

for i in sorted_family:
    print(i)