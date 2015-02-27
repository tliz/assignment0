mixed_list =[256, 'Kigali', 250, 250, 'nairobi', 'Kampala']

city_code = []

cities = []

print "before loop"
print city_code
print cities

for item in mixed_list:
    if type(item) == int:
        city_code.append(item)
    elif type(item) == str:
        cities.append(item)

print "after loop"
print city_code
print cities
