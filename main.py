# return txt which is all lower case
def lower_txt(txt):
    new_txt_list = []
    for char in txt:
        new_txt_list.append(char.lower())

    return new_txt_list

# make dictionary which refers key to character and value to occurence
def make_dic(txt):
    txt_dic = {}
    for char in txt:
        if char in txt_dic:
            txt_dic[char] += 1
        else:
            txt_dic[char] = 1
    return txt_dic

# count number of item in given list
def count_items(list):
    count = 0
    for word in list:
        count += 1
    return count

# convert dictionary to list of dictionaries
def convert_to_list_of_dic(dic):
    new_list = []
    for key in dic:
        new_list.append({key: dic[key]})
    return new_list

# function for sort()
def sort_by_value(dic):
    return list(dic.values())[0]

# return only alphabet list
def only_alphabet(given_list):
    new_list = []
    for dict in given_list:
        if list(dict)[0].isalpha():
            new_list.append(dict)
    return new_list

# final print function
def print_message(num, path, given_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num} words found in the document\n")
    # print loop
    for dictionary in given_list:
        print(f"The '{list(dictionary.keys())[0]}' character was found {list(dictionary.values())[0]} times")
    print("--- End report ---")


# MAIN
def main():
    path = "./books/frankenstein.txt"
    # open text file
    with open(path) as file:
        file_contents = file.read()

    ## COUNT ITEM IN LIST ##

    # create single char list
    f_word_list = []
    f_word_list = file_contents.split()

    # count items
    num_of_items = count_items(f_word_list)


    ## COUNT CHAR IN TEXT FILE ##

    # make lowercase
    lower_txt(file_contents)

    # make dictionary
    char_dic = make_dic(lower_txt(file_contents))

    # convert dic to list of dic
    converted_list = convert_to_list_of_dic(char_dic)

    # get rid of non alphabet
    converted_list = only_alphabet(converted_list)

    # sort dic
    converted_list.sort(reverse=True, key=sort_by_value)
    print(converted_list)


    ## PRINT TO CONSOLE ##

    # print out to console
    print_message(num_of_items, path, converted_list)

main()
