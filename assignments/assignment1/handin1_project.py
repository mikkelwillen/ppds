f = open("Land_and_Ocean_summary.txt", "r")
list_of_lines = f.readlines()

for i in range(len(list_of_lines)):
    temp = list_of_lines[i].strip() and list_of_lines[i].split()
    if (len(temp) > 0 and temp[0] != "%" and int(temp[0]) >= 2000):
        print(list_of_lines[i], end="")