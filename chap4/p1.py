import random
print("I sence your energy. Your true emotions are coming acroos my screen")

mood=random.randrange(2) 
if mood == 0:
    print("You are..    ")
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("| -       - |")
    print("|  -     -  |")
    print("|    ---    |")
    print("-------------")
    print("...today.    ")
#happy
    
  
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|    ---    |")
    print("|  -     -  |")
    print("| -        -|")
    print("-------------")
    print("...today.    ")
#sad
    
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|           |")
    print("|     0     |")
    print("|           |")
    print("-------------")
    print("...today.    ")
#surprise
    
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|           |")
    print("|     3     |")
    print("|           |")
    print("-------------")
    print("...today.    ")
#playful

    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|///     ///|")
    print("|           |")
    print("|           |")
    print("-------------")
    print("...today.    ")
#shy
else:
    print("Illegal mood value!")
    print(mood)
    
