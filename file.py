from collections import Counter
import csv


def mean(total_weight, total_entries):
    mean = total_weight / total_entries
    print(f"Mean (Average) is -> {mean:2f}")


def median(entries,data):
    if entries % 2 == 0:
        median1 = float(data[entries//2])
        #changed to entries - u had written float(data[data//2 - 1])
        median2 = float(data[entries//2 - 1])
        median = (median1 + median2) / 2
    else:
        median = float(data[entries//2])
    #Indentation was wrong for print  
    print(f"Median is -> {median:2f}")
    

def mode(data):
    data = Counter(data)

    mode_for_data = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0

    }
# changed weight to float(weight) otherwise it was not comparing
    for weight, occurence in data.items():
        if 75 < float(weight) < 85:
            mode_for_data["75-85"] += occurence
        elif 85 < float(weight) < 95:
            mode_for_data["85-95"] += occurence
        elif 95 < float(weight) < 105:
            mode_for_data["95-105"] += occurence
        elif 105 < float(weight) < 115:
            mode_for_data["105-115"] += occurence
        elif 115 < float(weight) < 125:
            mode_for_data["115-125"] += occurence
        elif 125 < float(weight) < 135:
            mode_for_data["125-135"] += occurence
        elif 135 < float(weight) < 145:
            mode_for_data["135-145"] += occurence
        elif 145 < float(weight) < 155:
            mode_for_data["145-155"] += occurence
        elif 155 < float(weight) < 165:
            mode_for_data["155-165"] += occurence
        elif 165 < float(weight) < 175:
            mode_for_data["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_for_data.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")

with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    data_files = list(reader)

data_files.pop(0)

weight = 0
entries = len(data_files)
sorted_data = []
for i in data_files:
    #u were correct it was supposed to be i as i is each row
    weight += float(i[2])
    sorted_data.append(i[2])

sorted_data.sort()

mean(weight, entries)
median(entries, sorted_data)
mode(sorted_data)
