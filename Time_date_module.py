import time

#print(time.ctime(1000000))    #convert a time expressed in seconds since epoch to a readable string
                        #epoch  = when your computer thinks time began(reference point)

#print(time.time())  #return current seconds since epoch

#print(time.ctime(time.time()))

time_object = time.localtime()
#print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)

time_object = time.gmtime()
#print(time_object)
"""Coordinated Universal Time or UTC is the primary time standard by which
    the world regulates clocks and time.
    It is within about 1 second of mean solar time at 0degrees longitude,
    and is not adjusted for daylight saving time"""

"""time.strptime() this function will parse a string representation and a time or date
                    and return a time object
time_string = "27 April, 2021"
time_OB = time.strptime(time_string, "%d %B, %Y")
print(time_OB)"""

"""time.asctime()->this function accepts tuple of a time representation of a relative time
    (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)"""
time_tuple = (2021, 4, 27, 9, 23, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)


"""this will take a tuple representation of a time or time object and convert it into seconds in epoch"""
"""(year, month, day, hours, minutes, secs, day of the week, day of the year, dst)"""
time_tuple = (2021, 4, 27, 9, 23, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

