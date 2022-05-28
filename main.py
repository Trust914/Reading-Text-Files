# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename , "r")
    read_file = file.read()
    file.close()
    return read_file
    


def count_words(sentence):
    # [assignment] Add your code here
    sentence = sentence.lower()
    words = sentence.split() #isolate the words from the sentence and store them in the list: words
    text = ((read_file_content("I4g+Zuri_ Tech_Training_10\Python\Reading-Text-Files\story.txt")).lower()).split()
    counter = {}
   
    for the_word in words:
        if the_word in text:
            counter[the_word] = text.count(the_word)
    
    return counter
print(count_words("This is interesting" ))
