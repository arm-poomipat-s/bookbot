def count_word(book):
    
    word_list = book.split()
    nums_word = len(word_list)

    return nums_word
    
def count_charactor(book):
    
    count_char = {}
    lower_book = book.lower()
    list_count_char = []
    
    for char in lower_book:
        
        if char not in count_char and char.isalpha():
            count_char[char] = 1
            
        elif char.isalpha():
            count_char[char] += 1
            
    
    for char in count_char:
        list_count_char.append({"char_name": char, "nums": count_char[char]})
            
    return list_count_char


def sort_on(dict):
    return dict["nums"]
        

def main():
    
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        
    word_in_book = count_word(file_contents)
    char_in_book = (count_charactor(file_contents))
    char_in_book.sort(reverse=True, key=sort_on)
    
    # print(char_in_book)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_in_book} words found in the document")
    print()
    
    for char in char_in_book:
        print(f"The '{char["char_name"]}' character was found {char["nums"]} times")
    
        
    print("--- End report ---")
    
    
main()

