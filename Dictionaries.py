"""Dictionary => It is a changeable, unordered collection of unique key:values pairs
                they're fast because they use hashing, allow us to access a value quickly"""

"""dictionaries are mutable"""
capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
#print(capitals['India'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
capitals.update({'Kenya': 'Nairobi'})
capitals.update({'India': 'Mumbai'})
capitals.pop('USA')
capitals.clear()

for key,value in capitals.items():

    print(key,value)