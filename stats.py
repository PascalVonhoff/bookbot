def count_words(text):
    list_of_single_words = text.split() # Der gesamte Inhalt von text wird in eine Liste umgewandelt, die nach jedem Leerzeichen (' ') ein neues Element der Liste hinzufügt. Es wird also jedes einzelne Wort aus text in einer Liste (list_of_single_words) gespeichert.
    total_words = len(list_of_single_words)
    return total_words

def print_total_words(total_words):
    print(f"{total_words} words found in the document")

def number_of_each_character(book_text):
    lowercase_text = book_text.lower()
    dictionary_all_letters = {}
    for letter in lowercase_text:
        if letter in dictionary_all_letters:
            dictionary_all_letters[letter] += 1
        else: dictionary_all_letters[letter] = 1
    return dictionary_all_letters 

   


