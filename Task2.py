import random
import string
from collections import defaultdict

list_dicts = []  # initialization variable to collect all dictionaries
number_dict = random.randint(2, 10)  # initialization and generation random value

def dict_sort(my_dict: dict):
    return dict(sorted(my_dict.items()))

while True:  # Loop for filling in list by dicts
    rand_dict = {}  # initialization dict
    while True:  # Loop for filling in the dict
        rand_dict[random.choices(string.ascii_lowercase)[0]] = random.randint(0, 100)  # adding random char as
        # a key and random int in range 0-100 as a pair into the dict
        if len(rand_dict) == number_dict:  # Check if required amount of keys are already generated
            break  # Closing the loop filling the dict
    rand_dict = dict_sort(rand_dict)  # Sorting generated dict by function dict_sort
    list_dicts.append(rand_dict)  # Adding generated dict to the list of dicts

    if len(list_dicts) >= number_dict:  # Check length of list with dicts is less than required
        break  # break for loop when list will be filled up appropriate count times
for current_dict in list_dicts:      # print to console all the dicts separately
    print(current_dict)

# Using defaultdict to get dict with all the keys and list of all value for this key
# It was used to find elements, that has the greatest values at first appearance to not to loose the data
dict_with_all_values = defaultdict(list)
for sub_dict in list_dicts:      # Iterate threw the list of dicts
    for key in sub_dict:            # Iterate threw the keys of iterated dict
        dict_with_all_values[key].append(sub_dict[key])     # append value of the key to existed or created key


new_dict = {}  # Initialization new dict variable
dict_changed = {}  # Initialization dict variable for changed elements (key = key, value = dict number)

for number_of_dict in range(len(list_dicts)):  # Loop for detecting duplicates in keys
    list_of_keys_in_current_dict = list(list_dicts[number_of_dict])  # initialization variable to hold list of dicts
    current_dict = list_dicts[number_of_dict]  # initialization temporary variable holding current dictionary
    keys_for_current_dict = list(current_dict.keys())  # initialization temporary variable to hold keys of current dict
    for key_number in range(len(list_of_keys_in_current_dict)):  # loop for filling in new_dict with all values
        # dict_for_changed_elements_flags[keys_for_current_dict[key_number]] = 0
        if list_of_keys_in_current_dict[key_number] in new_dict:  # check for presence of the key in the common dict
            if list_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]] > new_dict[list_of_keys_in_current_dict[key_number]]:  #
                # check for bigger value to that key
                new_dict[list_of_keys_in_current_dict[key_number]] = list_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]]  #
                # adding value to new_dick
                dict_changed[keys_for_current_dict[key_number]] = number_of_dict + 1  # adding dict number to proper dict
                # dict_for_changed_elements_flags[keys_for_current_dict[key_number]] += 1
        else:
            new_dict[list_of_keys_in_current_dict[key_number]] = list_dicts[number_of_dict][list_of_keys_in_current_dict[key_number]]  # adding
            # if key has more than one appearance in all dicts
            if len(dict_with_all_values[list_of_keys_in_current_dict[key_number]]) != 1:
                # add dict number to the special dict
                dict_changed[keys_for_current_dict[key_number]] = number_of_dict + 1

print(new_dict)

final_dict = {}  # dict variable for items with proper key names
keys_for_new_dict = list(new_dict.keys())  # variable initialization with list of keys from new_dict
keys_for_dict_for_changed_elements = list(dict_changed.keys())  # variable initialization with list
for key_number in range(len(new_dict)):  # loop for creating dict with proper keys
    if keys_for_new_dict[key_number] in dict_changed:  # check if key is present in dict for keys should be changed
        final_dict[str(keys_for_new_dict[key_number]) + "_" + str(dict_changed[keys_for_new_dict[key_number]])] = new_dict[keys_for_new_dict[key_number]]  #
        # adding key-value pair with proper key name and max value
    else:
        final_dict[keys_for_new_dict[key_number]] = new_dict[keys_for_new_dict[key_number]]  # adding key-value pair with unchanged
        # key and value

final_dict = dict_sort(final_dict)  # sorting final dict
print(final_dict)  # print final result - can be deleted
