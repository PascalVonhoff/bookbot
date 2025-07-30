filepath = "books/frankenstein.txt"

def get_book_text(filepath):        
    with open(filepath) as f:       
        file_contents = f.read()    
    return file_contents            

book_text = get_book_text(filepath)

from stats import count_words
from stats import print_total_words
from stats import number_of_each_character

def main(): 
    text = get_book_text(filepath)
    total_words = count_words(text)
    print_total_words(total_words)
    print(number_of_each_character(text))

main()
        


