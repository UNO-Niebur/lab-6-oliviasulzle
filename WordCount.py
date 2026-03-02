#WordCount.py
#Name: Olivia Sulzle
#Date: 3/1/26
#Assignment: Lab 6


def main():
  filename = input("Enter the filename: ")
  try:
    with open(filename, 'r') as textFile:
      lineCount = 0
      wordCount = 0
      letterCount = 0
     
      for line in textFile:
        lineCount = lineCount + 1
        words = line.split()
        for w in words:
          wordCount = wordCount + 1
          letterCount = letterCount + len(w)
   
    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Letters:", letterCount)


  except FileNotFoundError:
    print("File not found.")
 


if __name__ == '__main__':
  main()


