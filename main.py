def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
  print(file_contents)

def wordcount():
  wordcount = 0
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
  for word in words:
    wordcount += 1
  print(wordcount)

# main()
wordcount()