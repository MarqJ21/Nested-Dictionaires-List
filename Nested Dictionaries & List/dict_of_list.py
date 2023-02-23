dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    number_of_locations = len(dojo['locations'])
    number_of_instructors = len(dojo['instructors'])
    print(number_of_locations, " LOCATIONS")
    for value in dojo["locations"]:
        print(value)
    print(number_of_instructors, " INSTRUCTORS")
    for value in dojo["instructors"]:
        print(value)

printInfo(dojo)