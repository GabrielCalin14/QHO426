giname = input("your name: ")

#len() - 

if len(name) > 9:
     print ("Your name is way tooo long to remeber . Can i use a nickname please?")
     print("This print too")
elif len(name) <= 3:
      print("that is very short - easy to remeber!")
else:
      print("Oh , your name is pretty short!")

print("Nice to meet you anyway, {}!" .format(name))