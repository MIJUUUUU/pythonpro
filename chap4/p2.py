import random

hero = random.randrange(50,100)
monster= random.randrange(50,100)

count=0 
hero_HP =0
monster_HP =0

print("hero HP: ",hero ,"monster HP: ", monster)

while hero >0 and monster >0:
  
 att = random.randrange(-10,20)
 mtt = random.randrange(-10,20) 

 hero_HP = hero - att 
 monster_HP = monster - mtt

 result = ""
 
 print("hero(HP: ",hero, ", attct:", att ,result,end='')
 if att <=0:
       print("fail",result,end='')
 else:
     print("success",result,end='')
 
 print("<-> monster(HP:",monster, ", attct:", mtt, ")" ,result,end='')
 if mtt<0:
       print("fail",result)
 else:
     print("success",result)
     
 count +=1
 
 hero=hero_HP
 monster=monster_HP
  
print("-----------------------")
print("Total phase : ", count)
if hero > monster:
        print("hero win!!!")
else:
        print("monster win!!!")
        


