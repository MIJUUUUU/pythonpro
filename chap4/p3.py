print("              Welcome to 'Guess My Number!!!          ")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

num = random.randrange(1,100)
count =0

mynum=""

while num == mynum:
 print("Take a guess : ",mynum)
 if mynum < num:
    print("Lower . . .")
 elif mynum > num:
    print("Higher . . .")

 count +=1

 elif mynum == num:
   print("You gueesed it ! The number was ", num)
   print("And it only took you ", count , " tries !")
 

