# Functions

# Runs only when you call it

# def make_some_eggs():
#   print("New order of eggs")


# make_some_eggs()  # Calling the function


# def make_some_eggs(egg_type):  # Calling an argument - here argument is egg_type
#   print("New order of", egg_type, "eggs")


# make_some_eggs("scambled")

# make_some_eggs("boiled")

# def make_some_eggs(quantiy, egg_type):  # multiple arguments - here arguments are egg_type and quantity
#   print("New order of",quantiy, "", egg_type, "eggs")


# make_some_eggs("3", "scambled")

# make_some_eggs("2", "boiled")

# make_some_eggs("6", "over_easy")        


def counter_loop(start, end):
  counter = start

  while True:
    counter *= 2
    print(counter)

    if counter > end:
      break
         
counter_loop(1, 100)

