
lucky_numbers = [4, 6, 8, 16, 79]
friends = ["Monica", "Rachel", "Ross", "Joey", "Chandler", "Phoebe"]

friends.append("Mike")
friends.insert(1, "Bob")
friends.remove("Chandler")
friends.extend(lucky_numbers)
lucky_numbers.reverse()

print(friends.index("Ross"))
print(friends)
print(lucky_numbers)