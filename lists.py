friends = ["zach", "robert"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
friends[1] = "lolipop"
print(friends)
friends.append("Creed")
print(friends.sort())
print(friends.reverse())
friends.extend(lucky_numbers)
friends.insert(1,"Pam")
friends.remove("zach")
print(friends.pop())
print(friends.index("Pam"))
friends.clear()
friends.insert(1,"Pam")
friends.insert(1,"Pam")
friends.insert(1,"Pam")
print(friends.count("Pam"))
friends2 = friends.copy()
print(friends2)
