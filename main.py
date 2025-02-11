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
  return wordcount

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

def sort_on(dict):
  return dict['num']

def report(book):
  char_dict = charcount(book)
  report_list = []
  for key, value in char_dict.items():
    if key.isalpha():
      report_list.append({'char': key, 'num': value})
  report_list.sort(reverse=True, key=sort_on)
  for item in report_list:
    char = item['char']
    count = item['num']
    print(f"The '{char}' character was found {count} times")


# main("books/frankenstein.txt")
# wordcount()
# char_count = charcount("books/frankenstein.txt")
# print(report("books/frankenstein.txt"))
print("-- Begin report of books/frankenstein.txt")
word_count = wordcount("books/frankenstein.txt")
print(f"{word_count} words found in the document")
report("books/frankenstein.txt")
print("--- End report ---")
