import pickle
import shelve

print("Pickling lists.\n")
print("Unpickling lists.")

variety = ["sweet","hot","dill"]
pickle_file = open("pickles1.dat","wb")
pickle.dump(variety,pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat","rb")
variety = pickle.load(pickle_file)
print(variety)
pickle_file.close()

print("Retrieving the lists from a sheleved file:")
pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet","hot","dill"]
pickles.sync()
for key in pickles.key()
	print(key, "-", pickles[key])
pickles.close()
