print("Input your string . . .")
with open("write_it.txt", "w") as text_file:
    while True:
        user_input = input(">> ")
        
        if user_input.upper() == 'Q':
            break
        
        text_file.write(user_input + '\n')

print("Your inputs are below...\n")

with open("write_it.txt", "r") as text_file:
    print(text_file.read())
