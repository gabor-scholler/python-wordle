import random

word_list = ["cloud","award","drama","dream","black","basic"]
user_word = []
word_word = []
user_guess = ""
count = 0

random = random.randint(0,len(word_list)-1)

for i in word_list[random]:
  word_word.append(i)

while user_word != word_word:
  user_word = []
  user_guess = input("\nInsert Guess: ")
  while len(user_guess) != 5:
    print("\nInput must be five letters long!")
    user_guess = input("Insert Guess: ")

  for i in user_guess:
    user_word.append(i)

  for i in range(0,5):
    if user_word[i] in word_word:
      if user_word[i] == word_word[i]:
        print("Letter " + str(i + 1) + " is correct!")
      else: 
        print("Letter " + str(i + 1) + " is in word!")

print("\n\nCorrect Answer!")
