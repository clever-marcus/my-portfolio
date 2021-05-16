"""slicing => is the creating of a sub string by extracting elements from another string
                index[] or slice()
                start:stop:step"""

#INDEXING
name = "Smart Developer"

first_name = name[:5]
last_name = name[5:15]

funcky_name = name[::1]
reversed_name = name[::-1]
#print(reversed_name)

#SLICING
website1 = "www.itaxKenya.com"
website2 = "www.myPortfolio.com"
slicing = slice(4, -4)
print(website1[slicing])
print(website2[slicing])