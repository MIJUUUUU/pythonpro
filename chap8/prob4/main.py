import cPickle
print("Pickling lists.")
print("Unpickling lists.")

variety = ["sweet","hot","dill"]
pickle_file = open("pickles1.dat","w")
cPickle.dump(variety,pickle_file)
pickle_file.close()

pickle_file = open("pickles1.dat","r")
variety = cPickle.load(pickle_file)
print(variety)
pickle_file.close()
