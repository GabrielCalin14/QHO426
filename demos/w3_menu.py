print("Please choose one of the following options:\n\n1-NiceMessage\n2-Area of Rectangle\n3-Area of Triangle\n4-Times Table")
opt = int(input())

if opt == 1:
  print("You do not smell bad today")
elif opt == 2:
  w = float(input("Enter width: "))
  h = float(input("Enter height: "))
  area = w*h
  print("The area is {}" .format(area))
elif opt == 3:
  b = float(input("Enter base: "))
  h = float(input("Enter height: "))
  area = 0.5*b*h
  print("The area is {}".format(area))
elif opt == 4:
  n = (input("Enter whole number: "))
  for i in range(1,11):
      print(f"{i}x{n} = {i*n}")
  print("Thats's all folks!") 

def dimensions():
  w = float(input("Enter the width: "))
  l = float(input("Enter the lenght: "))
  return w, l #returning a tuple

def calc_area(l, w):
  return l*w

def r_name():
  return input("Enter name of the room: ")

def price(name, area):
  if name.lower() == "bathroom":
    return 20*area
  elif name.lower() == "bedroom":
    return 10*area
  elif name.lower() == "kitchen":
    return 30*area
  elif name.lower() == "living room":
    return 25*area
  else:
    return 50*area

def run():
  t_price = 0
  num = int(input("How many rooms to decorate? "))
  for i in range(num):
    name = r_name()
    x, y = dimensions()
    area = calc_area(x,y)
    t_price += price(name, area)
