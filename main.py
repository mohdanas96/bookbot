def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        char_dict = count_characters(file_contents)
        print_report(num_words, char_dict)

def count_words(text):
    text_list = text.split()
    num_of_words = len(text_list)

    return num_of_words

def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def print_report(num_words, char_dict):

    char_dict_list = []

    for char in char_dict:
        dict = {}
        if char.isalpha():
            dict["char"] = char
            dict["num"] = char_dict[char]
            char_dict_list.append(dict)

    char_dict_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} of words found in the document")
    print("")
    
    for char_dict in char_dict_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found '{num}' times")

    

def sort_on(dict):
    return dict["num"]    

main()