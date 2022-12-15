data_list = []
f = open("Land_and_Ocean_summary.txt", "r")
list_of_lines = f.readlines()

for i in range(len(list_of_lines)):
    temp = list_of_lines[i].strip() and list_of_lines[i].split()
    if (len(temp) > 0 and temp[0] != "%"):
        data_list.append(list_of_lines[i])

def read_data(filename):
    data_list = []
    f = open(filename, "r")
    list_of_lines = f.readlines()

    for i in range(len(list_of_lines)):
        temp = list_of_lines[i].strip() and list_of_lines[i].split()
        if (len(temp) > 0 and temp[0] != "%"):
            data_list.append(list_of_lines[i])
    return data_list

def read_data2(filename, year_range: tuple = (0, 10000)):
    data_list = []
    f = open(filename, "r")
    list_of_lines = f.readlines()

    for i in range(len(list_of_lines)):
        temp = list_of_lines[i].strip() and list_of_lines[i].split()
        if (len(temp) > 0 and temp[0] != "%" and int(temp[0]) >= year_range[0] and int(temp[0]) < year_range[1]):
            data_list.append(list_of_lines[i])
    return data_list

# read_data2("Land_and_Ocean_summary.txt", (2000, 2010))