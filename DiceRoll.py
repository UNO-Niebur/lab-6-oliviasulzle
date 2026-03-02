#DiceRoll.py
#Name: Olivia Sulzle
#Date: 3/1/26
#Assignment: Lab 6
import random


def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  num_rolls = 10000
  #Create two dice values ranging from 1 - 6 each
  for i in range(num_rolls):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
 
  #find the sum total of the two dice
    roll_sum = die1 + die2
    rolls[roll_sum] += 1
 
  #print statictics for dice rolls
  print("Sum | Count | Percent")
  for roll_sum in range (2,13):
    percent = (rolls[roll_sum] / num_rolls) * 100
    print(f"{roll_sum}\t{rolls[roll_sum]}\t{percent:.2f}%")
 


if __name__ == '__main__':
  main()
