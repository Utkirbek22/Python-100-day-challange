with open("james.txt","w") as james_file:
    content = james_file.write("[2-34,3:21,2.34,2.45,3.01,3.02,2.02,2-22]")
    print(content)

with open("james.txt", "r") as f:
    cont = f.read()
    james = cont.strip().split(",")
    print(james)