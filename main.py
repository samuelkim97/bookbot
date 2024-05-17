char_dic= {}

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


def main():
    # open text file
    with open("./books/frankenstein.txt") as file:
        file_contents = file.read()

    # count items in list
    # create single char list
    f_word_list = []
    f_word_list = file_contents.split()
    # count items
    num_of_items = count_items(f_word_list)
    print(num_of_items)

    # make lowercase
    lower_txt(file_contents)

    # make dictionary
    char_dic = make_dic(lower_txt(file_contents))
    print(char_dic)

    # testing
    convert_to_list_of_dic(char_dic)





main()
