#Definition of a function - specifying what it is an what it does
#paramiter = data given in to the function
def calc_area(h = 8, b = 1):
  area = 0.5*h*b
  return area
  
#Return value = data produce by function and given back to the caller

  
#Call to the function - to make it run
calc_area(2,10)
calc_area(7)
calc_area()
print(f"The area is {calc_area(80.20)} cm^2")