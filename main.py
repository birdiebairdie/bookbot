def main(book):
  file_contents = ""
  with open(book) as f:
    file_contents = f.read()
  return file_contents

def wordcount(book):
  wordcount = 0
  #with open("books/frankenstein.txt") as f:
  #  file_contents = f.read()
  words = main(book).split()
  for word in words:
    wordcount += 1
  print(wordcount)

def charcount(book):
  char_dict = {}
  lowercase_book = main(book).lower()
  char_list = list(lowercase_book)
  for char in char_list:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict

# main("books/frankenstein.txt")
# wordcount()
char_count = charcount("books/frankenstein.txt")
print(char_count)
