print("Input your string . . .")

while True:
 text_file = open("write_it.txt", "w")
 text_file.write = input(">> ")	
 
 if (input(">> ") == 'Q'):
	 break;

print("Your inputs are below ..\n")
text_file = open("write_it.txt", "r")
for line in text_file:
		print (line)
text_file.close()
 


