def read_data3(filename, year_range: tuple = (0, 10000)):
    data_list = {}
    f = open(filename, "r")
    list_of_lines = f.readlines()

    for i in range(len(list_of_lines)):
        temp = list_of_lines[i].strip() and list_of_lines[i].split()
        if (len(temp) > 0 and temp[0] != "%" and int(temp[0]) >= year_range[0] and int(temp[0]) < year_range[1]):
            key = int(list_of_lines[i][2:6])
            data = list_of_lines[i][6:].split(" ")
            while(" " in data):
                data.remove(" ")
            while('' in data):
                data.remove('')
            new_data = []
            for j in data:
                new_data.append(float(j))
            data_list[key] = new_data
    return data_list
