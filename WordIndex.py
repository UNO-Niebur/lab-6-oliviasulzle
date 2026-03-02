#WordIndex.py
#Name: Olivia Sulzle
#Date: 3/1/26
#Assignment: Lab 6


def main():
  filename = input("Enter the filename: ")
  textFile = open(filename, 'r')
 
  words = {} #create an empty dictionary
  lineNum = 0
 
  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()
    for w in wordList:
      w = w.lower()
      w = w.replace(",","")
      w = w.replace(".","")
   
      if w in words:
        if lineNum not in words[w]:
          words[w].append(lineNum)
      else:
        words[w] = [lineNum]


  for word in words:
    print(word, words[word])




if __name__ == '__main__':
  main()
  