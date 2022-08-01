full_name = "Mateo Hunter"
nickname = "Beikofasso"
age = 16
has_used_python = False

hobbies = ["playing the drums", "playing video games", "watching anime", "playing sports"]

fav_things = {
  "movie": "Rushmore",
  "food": "fries",
  "hobby": hobbies[0],
  "animal": " a frog" 
}

print(f"Hello! My name is {full_name}, but my favorite nickname is {nickname}. I am {age} years old.")
print()
for key in fav_things.keys():
    print(f"My favorite {key} is {fav_things[key]}.")
print()
print(f"My other hobbies are: {hobbies}")
all_vars = dict(vars())