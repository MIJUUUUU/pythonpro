name = input("Hi what's your name?")
age = int(input("And how old are you?"))
weigh = int(input("Okay, last question. How many pounds do you weigh?" ))
print("Did you know that you're just", age // 7,"in dog year?")

print("But you're also over", age * 365 * 24 * 60 * 60,"seconds old.")

print("If a small child were trying to get your attention, your name would become:")
for i in range(5):
    print(name,end="")

print("Did you know that on the moon you would weigh only", weigh / 6,"pounds?")
print("But on the sun, you'd weigh", weigh * 27.3,"<but, ah... not for long>.\n")
