import pickle

with open("myfile.txt","wb") as mysavedata:
    pickle.dump([1,2,3,5,"three"], mysavedata)

with open("myfile.txt","rb") as mysavedata:
    a_list = pickle.load(mysavedata)
print(a_list)