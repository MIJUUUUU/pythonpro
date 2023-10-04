import random
print("I sence your energy. Your true emotions are coming acroos my screen")

mood = random.randrange(3) 
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
    
if mood == 1:
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|    ---    |")
    print("|  -     -  |")
    print("| -        -|")
    print("-------------")
    print("...today.    ")
#sad
if mood ==2:    
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|           |")
    print("|     0     |")
    print("|           |")
    print("-------------")
    print("...today.    ")
#surprise
if mood == 3:
    print("-------------")
    print("| 0      0  |")
    print("|     <     |")
    print("|           |")
    print("|     3     |")
    print("|           |")
    print("-------------")
    print("...today.    ")
#playful
if mood == 4:
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
    
