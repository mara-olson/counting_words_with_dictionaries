"""Count words in file."""


# put your code here. 

import pwd


word_count_dict = {}
    
for line in open("test.txt"):
    for word in line.rstrip().split(" "):
        word_count_dict[word] = word_count_dict.get(word, 0) + 1
     
for words, count in word_count_dict.items():
    print(words, count)


    


#print(count_words("test.txt"))
  

# def make_letter_counts_dict(phrase):
#     """Return dict of letters and # of occurrences in phrase."""

#     letter_counts = {}

#     for letter in phrase:
#         letter_counts[letter] = letter_counts.get(letter, 0) + 1

#     return letter_counts

# >>> for animal, number in animals.items():
# ...    print(f'{animal}: {number}')
# ...
# goat: 6
# pony: 1
# duck: 14