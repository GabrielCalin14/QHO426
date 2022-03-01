age = int(input("Enter age: "))
ch = int(input("Enter number of children: "))

if age > 25 and ch > 0:
   print("You are a young parent!")
   print("Next year, you will be {age + 1} years old though")
elif age > 55 and ch > 0:
   print("Your children will support you in old age")
elif age < 18 or ch == 0:
 print("There is still time to have a child, if you want!")
else:
  print("You are not so young :(")
  print("we are going to live a long life anyway")