#tuple => this is a collection which is ordered and unchangeable
#       => they are used to group together related data

student = ("marcus", 21, "male", "Epic_programming")

print(student.count("marcus"))
print(student.index("Epic_programming"))

for x in student:
    print(x)
if "marcus" in student:
    print("Marcus is an EpicProgrammer")
else:
    pass
