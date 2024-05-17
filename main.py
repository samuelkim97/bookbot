def count_items(list):
    count = 0
    for word in list:
        count += 1
    return count

def main():
    with open("./books/frankenstein.txt") as file:
        file_contents = file.read()

    f_word_list = []
    f_word_list = file_contents.split()

    num_of_items = count_items(f_word_list)

    print(num_of_items)

main()
