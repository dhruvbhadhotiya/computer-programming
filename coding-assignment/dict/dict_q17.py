 
#  How can you count the occurrence of words in a list using a dictionary?

words = ['apple', 'banana', 'apple', 'orange', 'banana']
word_count = {word: words.count(word) for word in set(words)}
print(word_count)

