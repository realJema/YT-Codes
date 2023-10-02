import random
import string
import re
import dictionary

def generate_words(string):
  """Generates all the possible English words from a string of random characters."""
  words = []
  for i in range(len(string)):
    for j in range(i, len(string)):
      word = string[i:j + 1]
      if word.isalpha() and dictionary.is_word(word):
        words.append(word)
  return words

def main():
  """Gets an anagram from a user and generates all the possible words."""
  anagram = input("Enter an anagram: ")
  words = generate_words(anagram)
  print("The possible words are:")
  for word in words:
    print(word)

if __name__ == "__main__":
  main()