def read_word_file(filename):
    f = open(filename, "r")
    list_of_lines = f.readlines()
    
    word_list = []

    for i in range(len(list_of_lines)):
        word_list.append((i, list_of_lines[i].replace("\n", "")))
    
    return word_list

def read_word_file2(filename, word_stem=""):
    f = open(filename, "r")
    list_of_lines = f.readlines()

    word_list = []

    for i in range(len(list_of_lines)):
        if word_stem in list_of_lines[i] or word_stem == "":
            word_list.append((i, list_of_lines[i].replace("\n", "")))
    
    return word_list