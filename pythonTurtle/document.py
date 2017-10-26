import pickle
my_list = [123, 3.14,"甲鱼", ["another list"]]
pickle_file = open("my_list.pkl")
pickle_file = open("my_list.pkl", "wb")
pickle.dump(my_list, pickle_file)
pickle_file.close()
7