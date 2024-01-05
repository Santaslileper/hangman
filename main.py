import asksii
import os


def cls():os.system("cls")


#1
found_indices = []
tryed = []
attempts = -1
max_attempts = 12
word = input("Pick a word: ").lower()
cls()

def draw():
   try:cls();[print(i) for i in asksii.ascii_art_list[::-1][attempts] if attempts != -1]
   except:
      next

if not (word.isalpha()):
  print("Invalid input. Please enter a single letter.")
  word = input("Pick a word: ").lower()

while attempts <= max_attempts:
    attempt = input("Pick a letter: ").lower()
    if not (attempt.isalpha() and len(attempt) == 1):
      print("Invalid input. Please enter a single letter.")
      if not attempt not in tryed:
        print("you have tryed",attempt)
      continue
    tryed.append(attempt)
    if attempt not in word:
        attempts += 1
        draw()

    print("tryed",",".join(tryed)[::-1])
    if attempt in word:
        indices = [index for index, letter in enumerate(word) if letter == attempt]
        found_indices.extend(indices)
        draw()


    if found_indices:
        result = ''.join([word[i] if i in found_indices else '-' for i in range(len(word))])
        print(result,"with",len(tryed),"number of attempts")
        if result == word:print("you win");break

    if attempts == max_attempts:
      print("you lost the word was",word)
      break



#test code
#0
# found = []

# maxattempts = len(asksii.ascii_art_list)
# attempts = 0
# word = input("pick a word ")
# while attempts <= maxattempts:
#   attempt = input("pick a letter ")
#   if attempt not in word:
#         attempts +=1
#         os.system("cls")
#         [print(i) for i in asksii.ascii_art_list[::-1][attempts]]
#   if attempt in word:
#       found.append(attempt)
#   if found != None:
#       print(found)