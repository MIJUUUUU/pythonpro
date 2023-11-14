print("Creating a text file with the write<> method.\n")
print("Reading the newly created file.")

text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line2\n")
text_file.write("That makes this line 3\n")
print("")

print("Creating a text file with the writeline<> method.")
print("")
print("Reading the newly created file.\n")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line3\n"]
text_file.writelines(lines)
print("")
print("")

print("Press the enter key to exit.")
put = input()
while True:
  n = input("")
  if n == "":
   break;
