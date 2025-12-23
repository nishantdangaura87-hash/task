# QN.1
user_input = input("Enter any word or sentence: ")

vowels = set()
check = "aeiouAEIOU"

for i in user_input:
    if i in check:
        vowels.add(i.lower())
print("Unique vowels found:", vowels)
print("Total number of unique vowels =", len(vowels))


# QN.2
dictionary = {}
unique_words = set()
user_input = int(input("How many words do you want to add : "))
for i in range(1, user_input + 1):
    choice = int(input("1. Add\n2. Display \n3. Remove\n4.Exit "))
    if choice == 1:
        word = input("Enter the word: ")
        if word in unique_words:
            print(f"{word} already exists in the dictionary.")
        else:
            meaning = input("Enter the meaning: ")
            dictionary[word] = meaning
            unique_words.add(word)
    elif choice == 2:
        for i, j in dictionary.items():
            print(i, " ", j)
    elif choice == 3:
        word = input("Enter the word to remove: ")
        if word not in unique_words:
            print(f"{word} does not exist in the dictionary.")
        else:
            dictionary.pop(word)
            unique_words.remove(word)
    else:
        break
print(unique_words)


# QN.3

import random

quiz_questions = {
    1: {
        "question": "What is the capital of Nepal?",
        "options": {
            "A": "Kathmandu",
            "B": "Pokhara",
            "C": "Biratnagar",
            "D": "Lalitpur",
        },
        "answer": "A",
    },
    2: {
        "question": "Python was developed by?",
        "options": {
            "A": "James Gosling",
            "B": "Elon Musk",
            "C": "Guido van Rossum",
            "D": "Bill Gates",
        },
        "answer": "C",
    },
    3: {
        "question": "Which programming language are we learning?",
        "options": {"A": "Java", "B": "Python", "C": "PHP", "D": "C"},
        "answer": "B",
    },
}
question_keys = list(quiz_questions.keys())
random.shuffle(question_keys)
score = 0

for key in question_keys:
    print("\n" + quiz_questions[key]["question"])
    for opt in quiz_questions[key]["options"]:
        print(opt, ":", quiz_questions[key]["options"][opt])
    ans = input("Enter your answer (A/B/C/D): ").upper()
    if ans == quiz_questions[key]["answer"]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
print("\nYour final score is:", score)


# QN.4

total_items = int(input("Enter total number of items: "))

prices = []

for i in range(total_items):
    price = float(input("Enter price of item " + str(i + 1) + ": "))
    prices.append(price)

total_cost = sum(prices)

print("Total cost of all items =", total_cost)


# QN.5

sentence = input("Enter a sentence: ")

words = sentence.split()

total_words = len(words)

unique_set = set()

for w in words:
    unique_set.add(w.lower())

print("Total number of words:", total_words)
print("Total unique words:", len(unique_set))


# QN.6

sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = {}

for w in words:
    w = w.lower()
    word_count[w] = word_count.get(w, 0) + 1

print("\nWord frequency in alphabetical order:")

for word in sorted(word_count):
    print(word, ":", word_count[word])
