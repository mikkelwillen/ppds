from handin4 import *
import time

wordlist_british = wordfile_to_list("british-english_a-e")

wordlist_american = wordfile_to_list("american-english_a-e")

start_time = time.time()
differences_list_search = wordfile_differences_list_search("british-english_a-e", "american-english_a-e")
time_spent_list_search = time.time() - start_time

start_time = time.time()
differences_dict_search = wordfile_differences_dict_search("british-english_a-e", "american-english_a-e")
time_spent_dict_search = time.time() - start_time

start_time = time.time()
differences_set_search = wordfile_differences_set_search("british-english_a-e", "american-english_a-e")
time_spent_set_search = time.time() - start_time

print(differences_dict_search)
print(differences_set_search)

print(time_spent_dict_search, time_spent_set_search)