f = open("ord.txt", "r")
list_of_lines = f.readlines()

data_list = []

for i in range(len(list_of_lines)):
    if (list_of_lines[i].endswith(";sb.\n")):
        data_list.append(list_of_lines[i].replace(";sb.\n", "").replace("1. ", "").replace("2. ", ""))

f = open("filTilNina.txt", "a")
for i in range(len(data_list)):
    f.write(data_list[i] + ",")
