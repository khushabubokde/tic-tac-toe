import random
n = random.randint(1,100)
a=-1
guesses=0
while(a != n):
    guesses += 1
    a= int(input("Guess the number:"))
    if(a>n):
        print("Lower no. please:")
    else:
        print("Heigher no. please")

print(f"You have guess the no. correctly in {guesses} attemptss")