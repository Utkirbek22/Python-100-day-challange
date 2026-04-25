def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)

class Athlete:
    def __init__(self, a_name, a_job=None, a_times=[]):
        self.name = a_name
        self.job = a_job
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self,time_value):
        self.time_value = time_value
        self.times.append(time_value)

    def add_times(self, time_list = []):
        self.time_list = time_list
        self.times.extend(time_list)
#         sfds
def get_coach(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(",")
        return Athlete(templ.pop(0),templ.pop(0),templ)
    except IOError as err:
        print("file error")
        return None
# jack = get_coach("jack.txt")
# print(jack.name + "'s fastest times are: " + str(jack.top3()) + str(jack.add_time(99)) + str(jack.add_times([33])))


bonu = Athlete("Husnida Bonu")
bonu.add_time("77.91")
print(bonu.top3())
bonu.add_times(["22.33", "43.32", "23.12"])
print(bonu.top3())