import pickle
import shelve

print("Pickling lists.\n")
print("Unpickling lists.")

variety = ["sweet","hot","dill"]
shape = ["whole","spear","chip"]
brand = ["Claussen", "Heinz","Ulassic"]
pickle_file = open("pickles1.dat","wb")
pickle.dump(variety,pickle_file)
pickle.dump(shape,pickle_file)
pickle.dump(brand,pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat","rb")
variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)
print(variety)
print(shape)
print(brand)
pickle_file.close()

print("")
print("Retrieving the lists from a shelved file:")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet","hot","dill"]
pickles["shape"] = ["whole","spear","chip"]
pickles["brand"] = ["Claussen", "Heinz","Ulassic"]
pickles.sync()
for key in pickles.keys():
	print(key, "-", pickles[key])
pickles.close()
print("")

print("Press the enter key to exit.")
while True:
 n = input("")
 if n == "":
  break;
