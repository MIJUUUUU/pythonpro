
try:
 num = float(input("Enter a number: "))
except:
 print("Something went wrong!")
try:
 num = float(input("\nEnter a number: "))
except:
 print("That was not a number!")

print("")
for value in (None, "Hi!"):
  try:
   print("Attemping th convert",value, "->",end="")
   print(float(value))
  except(TypeError, ValueError):
   print("Something went wrong!")
  
print("") 
for value in (None, "Hi!"):
  try:
   print("Attemping th convert",value, "->",end="")
   print(float(value))
  except(TypeError):
   print("I can only convert a string or a number!")
  except(ValueError):
   print("I can only convert a string of digits!")

print("")
try:
 num = float(input("\nEnter a number: "))
except ValueError as e:
 print("That was not a number! Or as Python would say\n",e)

print("")
try:
 num = float(input("\nEnter a number: "))
except(ValueError):
 print("That was not a number!")
else:
 print("You entered the number", num)

print("Press the enter key to exit.")
while True:
 n = input("")
 if n =="":
  break;
