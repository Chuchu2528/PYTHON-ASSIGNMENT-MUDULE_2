# Input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
'''
Write a Python program to count the occurrences of each word in a
given sentence
'''

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")
