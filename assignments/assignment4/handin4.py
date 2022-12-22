def wordfile_to_list(filename):
    f = open(filename, "r")
    list_of_words = f.readlines()
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].replace("\n", "")
    return list_of_words

def wordfile_to_dict(filename):
    dict_of_words = {}

    with open(filename, "r") as lines:
        for line in lines:
            dict_of_words[line.replace("\n", "")] = None
    
    return dict_of_words

def wordfile_to_set(filename):
    set_of_words = set(line.replace("\n", "") for line in open(filename, "r"))

    return set_of_words

def wordfile_differences_list_search(filename1, filename2):
    wordlist1 = wordfile_to_list(filename1)
    wordlist2 = wordfile_to_list(filename2)

    diffList = []

    for i in wordlist1:
        notExists = True
        for j in wordlist2:
            if (i == j):
                notExists = False
                break
    
        if(notExists):
            diffList.append(i)

    return diffList

def wordfile_differences_dict_search(filename1, filename2):
    wordlist = wordfile_to_list(filename1)
    worddict = wordfile_to_dict(filename2)

    diffList = []

    for i in wordlist:
        if i not in worddict.keys():
            diffList.append(i)
    
    return diffList

def wordfile_differences_set_search(filename1, filename2):
    wordset1 = wordfile_to_set(filename1)
    wordset2 = wordfile_to_set(filename2)

    diffSet = wordset1.difference(wordset2)

    return list(diffSet)
