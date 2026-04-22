with open("james.txt","w") as james_file:
    content = james_file.write("[2-34, 3:21, 2.34, 2.45, 3.01, 3.02, 2.02, 2-22]")

with open("james.txt", "r") as f:
    cont = f.read()
    james = cont.strip()[1:-1].split(",")


cleaned = []
for item in james:
    item = item.replace("-",".").replace(":",".")
    cleaned.append(float(item))

data = sorted(cleaned)
print(type(data))

# data = [6,3,1,2,4,5]
# data.sort()
# print(data)
#

