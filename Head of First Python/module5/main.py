with open("james.txt", "w") as james_file:
    content = james_file.write("[2-34, 3:21, 2.34, 2.45, 3.01, 3.02, 2.02, 2-22]")

with open("james.txt", "r") as f:
    cont = f.read()
    james = cont.strip()[1:-1].split(",")


#  cleaner version with if else

def sanitize(time_string):
    time_string = time_string.strip()
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins,secs) = time_string.split(splitter)

    return (mins + "." + secs)

cleaned = sorted([float(sanitize(t)) for t in james])
print(cleaned)

without_dup = []

for i in cleaned:
    if i not in without_dup:
        without_dup.append(i)

print(without_dup[0:3])



def get_coach(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return (data.strip().split(","))
    except IOError as err:
        print(f"File error: + str{err}")
        return None

james = get_coach("james.txt")

print(james)


#
# dirty = ["2-22","2:22","2.22"]
# clean = [sanitize(t) for t in dirty]
# print(clean)

#  cleaner version with replace method
# cleaned = []
# for item in james:
#     item = item.replace("-",".").replace(":",".")
#     cleaned.append(float(item))
#

#  list comprehension with replace method
#
# cleaned = [item.replace("-",":").replace(".",":") for item in james]
# data = sorted(cleaned)
# print(data)






# data = [6,3,1,2,4,5]
# data.sort()
# print(data)
#

