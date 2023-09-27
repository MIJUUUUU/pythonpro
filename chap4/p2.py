import random

hero. HP = random.randrange(50,100)
monster.HP= random.randrange(50,100)
att = random.randrange(-10,20)
att.count=0 

while( hero.HP >0 and monster.HP >0):

    hero.HP = hero.HP - att
    monster.HP = monster - att

    if att <0:
    continue
      
    att.count = att.count + 1

    if hero > monster:
        print("hero win!!!")
    else 
        print("monster win!!!")

print("-----------------------")
print("Total phase: " + att.count) 
