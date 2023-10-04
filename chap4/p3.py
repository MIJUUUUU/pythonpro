import random


print("              Welcome to 'Guess My Number!!!          ")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

num = random.randrange(1,101)
count =0


while num<=100 and num >=1:

   mynum=int(input("Take a guess "))
   count +=1
   if mynum < num:
    print("Upper . . .")
   
   elif  mynum > num:
    print("Lower . . .")

   else:
    break

print("You gueesed it ! The number was ", num)
print("And it only took you ", count , " tries !")
 

