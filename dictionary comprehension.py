#dictionary comprehension => create dictionaries using an expression
#                           can replace for loops and certain lambda function

#dictionary = {key: expression for (key,value) in iterable}
#dictionary = {key: expression for (key,value) in iterable if conditional}
#dictionary = {key: (if/else) for (key,value) in iterable}
#dictionary = {key: function(value) for (key,value) in iterable}

#------------------------------------------------------------------------------------------------

#temp_in_Fahrenheit = {'Nairobi': 32, 'Kampala': 75, 'Dodoma': 100, 'Lesotho': 50}
#temp_in_Celcius = {key: round((value-32)*(5/9)) for (key,value) in temp_in_Fahrenheit.items()}
#print(temp_in_Celcius)
#-----------------------------------------------------------------------------------------------

"""weather = {'New York': "snowing", 'Boston': "sunny", 'LA': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key:value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)"""

#-------------------------------------------------------------------------------------------------

"""cities = {'New York': 32, 'Boston': 75, 'LA': 100, 'Chicago': 50}
desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key,value) in cities.items()}
print(desc_cities)"""

#----------------------------------------------------------------------------------------------------


def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


cities = {'New York': 32, 'Boston': 75, 'LA': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_cities)





