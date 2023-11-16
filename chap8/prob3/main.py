print("Input your string . . .")

while True:
 text_file = open("write_it.txt", "w")
  
 if (input(">> ") == 'Q'):
	 break;
 
text_file.close()
print("Your inputs are below ..\n")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()
 


