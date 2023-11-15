print("Input your string . . .")

while True:
 text_file = open("write_it.txt", "w")
 text_file.write = input(">> ")	
  
 if (input(">> ") == 'Q'):
	 

print("Your inputs are below ..\n")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()
 


