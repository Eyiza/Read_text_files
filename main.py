# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    file_content = []
    with open(filename) as f:
        for line in f:
            word = line.split()
            file_content.append(word)
    return file_content

def count_words():
    text = read_file_content("story.txt")
    word_counter = {}    
    for word in text:
        for line in word: 
            if line not in word_counter:
                word_counter[line.lower()] = 1
            else:
                word_counter[line] += 1    
    return word_counter
    #return {"as": 10, "would": 20}

print(count_words())
