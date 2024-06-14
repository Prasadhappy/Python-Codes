# for loop
# while loop

# example

# for loop

# numbers = [0, 1, 2, 3, 4, 5, 6]

# for num in numbers:
#   num = num *2
#   print(num)

# While Loop

# counter = 0

# while counter < 10:
#   counter = counter + 1
#   print(counter)

# items = ["steak", 'apple', "bread", "butter", "Pineapple"]

# Write a 'for loop' that loops through the above list and prints "item is a fruit" or "item is not a fruit", etc
# Note that it should not say item but the name of the fruit. So 'steak is not a fruit', 'apple is a fruit', etc.

# for item in items:
#   if item == "apple" or item == "Pineapple":
#     print(item, "is a fruit")
#   else:
#     print(item, "is not a fruit")

# Write a while loop starting with a counter = 1 that multiples two to your counter, prints the counter, but breaks the loop after the counter reaches 1000

# counter = 1

# while counter < 1000:
#   counter = counter * 2
#   print(counter)


counter = 1

while True:
  counter *= 2
  print(counter)

  if counter >1000:
    break


