# people = {}
# person = dict()
#
# print(type(people))
#
# print(type(person))
#
# person["Jack"] = "Utkirbek"

def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + "." + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(".")
        return ({'Name': templ.pop(0),
                 "Job": templ.pop(0),
                 "Times": str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    except IOError as err:
        print("File error: " + str(err))
        return (None)

jack = get_coach_data("jack.txt")

print(jack["Name"] + "'s fastest times are: " + jack["Times"])