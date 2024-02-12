with open('madlib-game/story.txt','r') as f:
    story = f.read()
print(story)

words = []
start_word = -1

target_start = "<"
target_end = ">"

for i , char in enumerate():
    if char == target_start:
        start_word = i
    if char == target_end and start_word != -1:
        word = story[start_word: i +1]
        words.append(word)
        start_word = -1
