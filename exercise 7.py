# let's make a def function

def word_counter(sentence, word):
    return sentence.count(word)

# make a variable and write the given sentence 
str_x = "Emma is a good developer. Emma is a writer"
# make a variable for the word that you want to count in the sentence 
the_word = "Emma"

# print the result 
print(f"{the_word} appeared {word_counter(str_x,the_word)} times")