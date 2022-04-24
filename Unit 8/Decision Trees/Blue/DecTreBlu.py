import csv
from math import log2

data = []
with open('play_tennis.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)

headers = data[0]
data.pop(0)


def calculate_entropy_diff(header):
    initial_entropy = 0
    total_yes = 0
    total_no = 0
    for point in data:
        if point[len(point) - 1] == "Yes":
            total_yes += 1
        else:
            total_no += 1
    num_points = len(data)
    total_yes /= num_points
    total_no /= num_points
    try:
        initial_entropy = -1 * (total_yes * log2(total_yes) + total_no * log2(total_no))
    except:
        initial_entropy = 0
    categories = set()
    for point in data:
        categories.add(point[header])
    categories = list(categories)
    count_categories = dict()
    entropy_calculations = dict()
    for category in categories:
        count_categories[category] = 0
        entropy_calculations[category] = 0
    for point in data:
        count_categories[point[header]] += (1/(len(data)))
    for category in categories:
        yes_num = 0
        no_num = 0
        total = round(count_categories[category] * 14)
        for point in data:
            if point[header] == category:
                if point[len(point) - 1] == "Yes":
                    yes_num += 1
                else:
                    no_num += 1
        yes = yes_num/total
        no = no_num/total
        try: 
            entropy_calculations[category] = -1 * (yes * log2(yes) + (no) * log2(no))
        except:
            entropy_calculations[category] = 0
    final_calc = 0
    for category in categories:
        final_calc += (count_categories[category] * entropy_calculations[category])
    return initial_entropy - final_calc


print(calculate_entropy_diff(3))

