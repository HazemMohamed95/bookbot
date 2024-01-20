def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_text = text.lower()
    num_words = get_num_words(text)
    words = lower_text.split()
    num_letters = get_num_letters(words)
    letters = get_num_letters(words)
    # print(f"{num_words} words found in the document kelma tenta7 kelma!! (ps:gada3 ala aHazem ala!)")
    # print(f"{num_letters}")

    print(f"--- Begin report of books/{book_path}---")
    print(f"{num_words} words was found in this document")
    print('   ')
    print(letter_report(letters))
    print("--- End report ---")


def letter_report(letters):
    ls_letters = list(letters.keys())
    ls_numbers = list(letters.values())
    for key in letters:
        if key.isalpha():
            print (f"the {key} character was found {letters[key]} times")
        else:
            pass
    


def get_num_words(words):
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(words):
    letters = {}
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
    return letters

        


# def get_book_text(path):
#     with open(path) as f:
#         # return f.read()
#         words = f.read().split()
#         return len(words)


main()