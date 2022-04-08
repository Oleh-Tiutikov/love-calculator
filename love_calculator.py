print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1_low = name1.lower()
name2_low = name2.lower()


t = name1_low.count('t')
r = name1_low.count('r')
u = name1_low.count('u')
e = name1_low.count('e')
true = t + r + u + e


l = name2_low.count('l')
o = name2_low.count('o')
v = name2_low.count('v')
e = name2_low.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90 :
  print(f"Your score is  {love_score}, you go together like coke and mentos.")
  
if love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together")
