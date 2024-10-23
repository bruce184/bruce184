# Open and Read the 'story.txt' file 
with open("story.txt", "r") as str:
    story = str.read()

words = []
start_of_word = -1 

# Define variables to notify if we ilterate at the start and end of a missing word
start = '<'
end = '>'


# Ilterate through each missing word 
for i, char in enumerate(story): 
    if char == start: 
        start_of_word = i

    if char == end and start_of_word != -1:
        # this is a slice operator (inside the bracket) - a sub section of the string
        word = story[start_of_word: i + 1] # 'i + 1' to include the ending index (bracket)
        words.append(word)
        start_of_word = -1 # reset for the next missing word

print(words)