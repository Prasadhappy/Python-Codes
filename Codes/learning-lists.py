birds = ["robin", "bluebird", "sparrow", "cardinal"]

print (birds[2])

birds.insert(3, "woodpecker")

print(birds)

# reversing using inbuilt method
# birds.reverse()
# print (birds)

# Save the first two birds only into a new variable called two_birds

two_birds = birds[0:2]

print(two_birds)

# Print woodpecker and cardinal using negative indices

print (birds[-2:])
