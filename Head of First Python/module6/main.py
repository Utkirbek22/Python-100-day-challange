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
        return (data.strip().split(","))
    except IOError as err:
        print("File error:" + str(err))
        return (None)

jack = get_coach_data("jack.txt")
#
# (jack_name, jack_day) = jack.pop(0),jack.pop(0)
#
# print(jack_name + "'s fastest time are: " + str(sorted(set([sanitize(t) for t in jack])) [0:3]))

jack_data = {}
jack_data["name"] = jack.pop(0)
jack_data["jack_day"] = jack.pop(0)
jack_data["times"] = jack

print(jack_data["name"] + "'s fastest time are:" + str(sorted(set([sanitize(t) for t in jack_data["times"]]))[0:3]))
