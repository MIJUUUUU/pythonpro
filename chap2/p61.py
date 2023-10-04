print('                      Trust Fund Buddy                      ')



print("Totals your monthly spending so that your trust fund doesn't run out")
print("<and you're forced to get a real job>")
print("Please enter the requested, monthly costs.  Since you're rich, ignore pennies and use only dollar amounts.\n")
tune = int(input("Lamborghini Tune-Ups: "))
rent = int(input ("Manhattan Apartment: "))
jet = int(input ("Private Jet Rental: "))
gifts = int(input ("Gifts: "))
food = int(input ("Dinig Out: "))
staff = int(input ("Staff (butlers, chef, driver, assistant): "))
guru = int(input ("Perconal Guru and Coach: "))
games = int(input ("Computer Games: "))

print("\nGrand total : ",tune + rent + jet + gifts + food + staff + guru + games)
