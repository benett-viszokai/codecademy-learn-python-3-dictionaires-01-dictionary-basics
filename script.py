songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Creating a dictionary with dict comprehension
plays = {songs:playcounts for songs, playcounts in zip(songs, playcounts)}

# Adding a new key:value pair
plays["Purple Haze"] = 1

# Updating an existing key:value pair
plays["Respect"] = 94

# Creating a new dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
