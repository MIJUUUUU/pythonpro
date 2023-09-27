import random

hero.HP = random.randrange(50,100)
monster.HP= random.randrange(50,100)
att = random.randrange(-10,20)
mtt = random.randrange(-10,20) 
att.count=0 

while( hero.HP >0 and monster.HP >0):

    hero.HP = hero.HP - att 
    monster.HP = monster - mtt # left blood

    if (att <0 and mtt<0):
     print("hero(HP: "+(hero.HP+att)+ ", attct:"+ att + fail + "<-> monster(HP:"+( monster.HP+mtt)+", attct:"+ mtt+")"+ fail)  
    elif(att<0 and mtt >0
     print("hero(HP: "+(hero.HP+att)+ ", attct:"+ att + fail + "<-> monster(HP:"+ monster.HP+", attct:"+ mtt+")"success)  
    elif(att>0 and mtt >0)
     print("hero(HP: "+hero.HP+ ", attct:"+ att + success + "<-> monster(HP:"+ monster.HP+", attct:"+ mtt+")" success)  
    elif(att>0 and mtt <0)
     print("hero(HP: "+hero.HP+ ", attct:"+ att + fail + "<-> monster(HP:"+( monster.HP+mtt)+", attct:"+ mtt +")" fail)  
          
    att.count = att.count + 1
if hero.HP > monster.HP:
        print("hero win!!!")
        else 
        print("monster win!!!")

print("-----------------------")
print("Total phase: " + att.count) 
